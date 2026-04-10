# Meteo ASUSTOR - Weather App for ASUSTOR NAS

Applicazione meteo per ASUSTOR NAS Lockerstor 6604T (e altri modelli compatibili). Visualizza condizioni meteo attuali e previsioni a 5 giorni.

© Copyright 2024-2026 Nsfr750 - All rights reserved.  
Licenza: GPLv3

## 📋 Caratteristiche

- Visualizzazione condizioni meteo attuali
- Previsioni meteo a 5 giorni con min/max temperature
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

## 📁 Struttura del Progetto

```text
asustor-weather-app/
├── app.py                 # Backend Flask con Open-Meteo API
├── apkg.xml              # Configurazione ASUSTOR App Central
├── requirements.txt      # Dipendenze Python
├── version.py            # Versione dell'app
├── install.sh            # Script installazione
├── uninstall.sh          # Script disinstallazione
├── start.sh              # Script avvio
├── stop.sh               # Script stop
├── build_apk.sh          # Script build pacchetto APK
├── templates/
│   └── index.html        # Interfaccia web
├── static/
│   ├── style.css         # Stili CSS
│   └── app.js            # Script frontend
├── README.md             # Documentazione
├── CHANGELOG.md          # Storico versioni
└── LICENSE               # Licenza GPLv3
```

## 🔧 Requisiti

- ASUSTOR NAS con ADM 4.0+
- Python 3.8+
- Porta 8000 disponibile
- Connessione Internet (per dati meteo)

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

### v1.0.0

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
