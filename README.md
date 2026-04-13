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

## � Struttura del Progetto

```text
asustor-weather-app/
├── app.py                 # Backend Flask con Open-Meteo API e database
├── database.py           # Modulo SQLite per dati storici
├── apkg.xml              # Configurazione ASUSTOR App Central
├── requirements.txt      # Dipendenze Python
├── version.py            # Versione dell'app
├── install.sh            # Script installazione
├── uninstall.sh          # Script disinstallazione
├── start.sh              # Script avvio
├── stop.sh               # Script stop
├── build_apk.sh          # Script build pacchetto APK
├── templates/
│   ├── index.html        # Interfaccia principale meteo
│   └── stats.html        # Pagina statistiche con grafici
├── static/
│   ├── style.css         # Stili CSS
│   ├── app.js            # Script frontend principale
│   └── stats.js          # Script grafici Chart.js
├── weather_data.db       # Database SQLite (creato automaticamente)
├── README.md             # Documentazione
├── CHANGELOG.md          # Storico versioni
└── LICENSE               # Licenza GPLv3
```

## � Creazione del pacchetto APK

Per creare il file `.apk` installabile su ASUSTOR NAS:

### Prerequisiti

- Linux/macOS/WSL con Bash
- Python 3.8+
- tar (installato di default sulla maggior parte dei sistemi)

### Procedura

1. Clona il repository:

   ```bash
   git clone https://github.com/Nsfr750/asustor-weather-app.git
   cd asustor-weather-app
   ```

2. Esegui lo script di build:

   ```bash
   bash build_apk.sh
   ```

3. Lo script eseguirà automaticamente:
   - Lettura della versione da `version.py`
   - Creazione della directory di build
   - Copia di tutti i file necessari
   - Impostazione dei permessi di esecuzione
   - Creazione dell'archivio `.apk` (formato tar.gz)

4. Al termine troverai il file `weather-app-{versione}.apk` nella directory principale.

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
- Pagina dedicata `/stats` con andamenti e riepiloghi
- Archiviazione automatica dati ad ogni ricerca
- Compatibilità ADM estesa alla 2.0+

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
