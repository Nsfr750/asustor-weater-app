# Meteo ASUSTOR - Weather App for ASUSTOR NAS

Applicazione meteo per ASUSTOR NAS Lockerstor 6604T (e altri modelli compatibili). Visualizza condizioni meteo attuali e previsioni a 5 giorni.

© Copyright 2024-2026 Nsfr750 - All rights reserved.  
Licenza: GPLv3

## 📋 Caratteristiche

- Visualizzazione condizioni meteo attuali
- Previsioni meteo a 5 giorni con min/max temperature
- **Statistiche storiche** con grafici interattivi (temperatura, umidità, pressione, vento)
- **Database SQLite** per archiviazione dati giornalieri e orari
- **Pagina dedicata** (`/stats`) con andamenti e riepiloghi
- **Supporto multilingua IT/EN** con selettore lingua nel menu
- **Sistema di internazionalizzazione** (i18n) completo
- Interfaccia web moderna e responsive
- Supporto per città in tutto il mondo
- **Nessuna API key richiesta** - Gratuita e open source
- Salvataggio preferenze città (localStorage)
- Dati forniti da [Open-Meteo](https://open-meteo.com)

## 🚀 Installazione

### Metodo 1: App Central (Consigliato)

1. Scarica il file `.apk` dalla sezione [Releases](https://github.com/Nsfr750/asustor-weather-app/releases)
2. Apri App Central sul tuo ASUSTOR NAS
3. Clicca su "Installazione manuale"
4. Seleziona il file `.apk` scaricato
5. Segui la procedura guidata

### Metodo 2: Manuale via SSH

1. Connettiti al NAS via SSH:

   ```bash
   ssh admin@tuo-nas-ip
   ```

2. Scarica l'applicazione:

   ```bash
   cd /usr/local/AppCentral
   git clone https://github.com/Nsfr750/asustor-weather-app.git weather-app
   cd weather-app
   ```

3. Installa le dipendenze:

   ```bash
   python3 -m pip install -r requirements.txt --user
   ```

4. Avvia l'applicazione:

   ```bash
   ./start.sh
   ```

5. Accedi all'app: `http://tuo-nas-ip:8000`

## ⚙️ Configurazione

### Cambio Lingua

L'app supporta Italiano 🇮🇹 e English 🇬🇧:

1. Usa il selettore lingua nel menu di navigazione
2. La lingua scelta viene salvata automaticamente
3. Tutte le stringhe dell'interfaccia si aggiornano in tempo reale

### Prima Configurazione

L'app non richiede configurazione. Al primo avvio:

1. Inserisci il nome della città desiderata
2. Clicca su "Cerca"
3. La città viene salvata automaticamente per i prossimi accessi

## � Statistiche e Grafici

L'app include una pagina dedicata alle statistiche storiche:

- **Accesso**: Clicca su "📊 Statistiche" nel menu di navigazione o vai a `http://tuo-nas-ip:8000/stats`
- **Dati archiviati**: Ogni ricerca meteo salva automaticamente i dati in database SQLite
- **Periodi disponibili**: 7, 30, 90 giorni o 1 anno
- **Grafici disponibili**:
  - Andamento temperature (max, media, min)
  - Umidità media
  - Pressione atmosferica
  - Velocità del vento
  - Andamento orario ultime 24 ore

**Nota**: I dati si accumulano automaticamente ad ogni ricerca. Più spesso cerchi il meteo, più dati avrai nei grafici!

## 📁 Struttura del Progetto

```text
asustor-weather-app/
├── CONTROL/              # File di controllo ASUSTOR (apkg-tools)
│   ├── config.json       # Configurazione pacchetto ASUSTOR
│   ├── apkg-version      # Versione dell'app
│   ├── icon.png          # Icona app
│   ├── icon-enable.png   # Icona attiva (ADM desktop)
│   ├── icon-disable.png  # Icona disattiva (ADM desktop)
│   ├── install.sh        # Script installazione
│   ├── uninstall.sh      # Script disinstallazione
│   ├── start.sh          # Script avvio
│   ├── stop.sh           # Script stop
│   ├── changelog.txt     # Changelog per ASUSTOR
│   └── description.txt   # Descrizione breve
├── data/                 # File applicazione
│   ├── app.py            # Backend Flask con Open-Meteo API e database
│   ├── database.py       # Modulo SQLite per dati storici
│   ├── lang/             # Sistema internazionalizzazione
│   │   ├── __init__.py
│   │   ├── translations.py    # Dizionari IT/EN
│   │   └── language_manager.py # Gestione lingua backend
│   ├── requirements.txt  # Dipendenze Python
│   ├── version.py        # Versione dell'app
│   ├── templates/
│   │   ├── index.html    # Interfaccia principale meteo
│   │   └── stats.html    # Pagina statistiche con grafici
│   ├── static/
│   │   ├── style.css     # Stili CSS
│   │   ├── app.js       # Script frontend principale
│   │   ├── stats.js     # Script grafici Chart.js
│   │   └── i18n.js      # Gestione lingua frontend
│   ├── README.md         # Documentazione
│   ├── CHANGELOG.md      # Storico versioni
│   └── LICENSE           # Licenza GPLv3
├── apkg-tools_py3.py     # Tool ASUSTOR per creazione APK (opzionale)
└── weather_data.db       # Database SQLite (creato automaticamente)
```

## 📦 Creazione del pacchetto APK

Per creare il file `.apk` installabile su ASUSTOR NAS:

### Metodo 1: apkg-tools_py3.py (Consigliato)

Usa il tool ufficiale ASUSTOR per creare il pacchetto:

1. Clona il repository:

   ```bash
   git clone https://github.com/Nsfr750/asustor-weather-app.git
   cd asustor-weather-app
   ```

2. Aggiorna la versione in `CONTROL/apkg-version` e `data/version.py`

3. Esegui il tool ASUSTOR:

   ```bash
   python apkg-tools_py3.py create . --destination .
   ```

4. Al termine troverai il file `weather-app_{versione}_any.apk` nella directory principale.

### Metodo 2: Script Bash (Alternativo)

Su Linux/macOS/WSL puoi usare lo script shell:

```bash
bash -c '
VERSION=$(python3 -c "from data.version import __version__; print(__version__)")
echo "Building weather-app-${VERSION}.apk..."
echo "${VERSION}" > CONTROL/apkg-version
cd CONTROL && tar -czf ../control.tar.gz . && cd ..
cd data && tar -czf ../data.tar.gz . && cd ..
tar -czf "weather-app-${VERSION}.apk" control.tar.gz data.tar.gz
rm control.tar.gz data.tar.gz
echo "Build completed: weather-app-${VERSION}.apk"
'
```

### Struttura APK

Il file `.apk` generato contiene:
- `control.tar.gz`: file di controllo ASUSTOR (config.json, scripts, icona)
- `data.tar.gz`: applicazione completa (Python, templates, static)
- `apkg-version`: file con la versione del pacchetto

### Installazione del pacchetto

1. Apri **App Central** sul tuo ASUSTOR NAS
2. Clicca su **"Installazione manuale"**
3. Seleziona il file `.apk` generato
4. Segui la procedura guidata

## �🔧 Requisiti

- ASUSTOR NAS con ADM 2.0+
- Python 3.8+
- Porta 8000 disponibile
- Connessione Internet (per dati meteo)
- 50MB spazio libero (per database storico)

## 🐛 Risoluzione Problemi

### L'app non si avvia

- Verifica che Python 3 sia installato: `python3 --version`
- Controlla i log: `/usr/local/AppCentral/weather-app/logs/app.log`
- Verifica che la porta 8000 sia libera

### Dati meteo non caricano

- Verifica la connessione Internet del NAS
- Verifica che il servizio Open-Meteo sia raggiungibile
- Prova con un'altra città (alcuni nomi possono avere varianti)

## 📝 Changelog

### v1.1.0 (2026-04-13)

- **Statistiche storiche** con grafici interattivi (Chart.js)
- **Database SQLite** per archiviazione dati meteo
- **Supporto multilingua IT/EN** con selettore lingua
- **Sistema di internazionalizzazione** completo (i18n)
- Pagina dedicata `/stats` con andamenti e riepiloghi
- Archiviazione automatica dati ad ogni ricerca
- Compatibilità ADM estesa alla 2.0+
- Struttura APK: CONTROL/ e data/ (formato ASUSTOR standard)
- Icone enable/disable per visualizzazione desktop ADM
- Avvio automatico app dopo installazione

### v1.0.0 (2026-04-10)

- Rilascio iniziale
- Supporto meteo attuale e previsioni
- Interfaccia in italiano

## 👤 Autore

## Nsfr750 - Tuxxle

- GitHub: [@Nsfr750](https://github.com/Nsfr750)
- Email: [NSFR750](mailto:nsfr750@yandex.com)
- Website: [https://www.tuxxle.org](https://www.tuxxle.org)

## 💰 Supporta lo sviluppo

- **PayPal**: [paypal.me/3dmega](https://paypal.me/3dmega)
- **Monero**: `47Jc6MC47WJVFhiQFYwHyBNQP5BEsjUPG6tc8R37FwcTY8K5Y3LvFzveSXoGiaDQSxDrnCUBJ5WBj6Fgmsfix8VPD4w3gXF`

## 📜 Licenza

Questo progetto è rilasciato sotto licenza **GPLv3**. Vedi file LICENSE per dettagli.

---

© Copyright 2024-2026 Nsfr750 - All rights reserved.
