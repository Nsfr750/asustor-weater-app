# Changelog

Tutte le modifiche significative a questo progetto saranno documentate in questo file.

Il formato è basato su [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
e questo progetto aderisce a [Semantic Versioning](https://semver.org/lang/it/spec/v2.0.0.html).

## [1.1.0] - 2026-04-13

### Aggiunto

- **Database SQLite** per archiviazione dati storici
- **Pagina Statistiche** (`/stats`) con grafici interattivi (Chart.js)
- **Archiviazione automatica** dati meteo ad ogni ricerca
- **Grafici storici**: temperatura (max/media/min), umidità, pressione, vento
- **Andamento orario** ultime 24 ore con doppio asse
- **Card riepilogative** con statistiche di sintesi
- **Supporto multilingua IT/EN** con selettore lingua nel menu navigazione
- **Sistema di internazionalizzazione** completo (backend + frontend)
- API endpoint per gestione lingua (`/api/language`, `/api/translations`)
- Selettore periodo: 7, 30, 90 giorni o 1 anno
- Menu navigazione tra Home e Statistiche
- API endpoint per dati statistici (`/api/stats/*`)
- Cleanup automatico dati vecchi (configurabile)

### Modificato

- Compatibilità ADM estesa dalla 2.0+ (precedentemente 4.0+)
- Rimosso requisito screenshot da `apkg.xml` per ADM 2.0
- Struttura progetto: file divisi in `CONTROL/` e `data/` (formato ASUSTOR APK standard)
- Aggiunte icone `icon-enable.png` e `icon-disable.png` per visualizzazione desktop ADM
- Installazione automatica: avvio app automatico al termine installazione
- Script `install.sh` migliorato per copia file in root app (`CONTROL/` e `data/`)
- Script `uninstall.sh` aggiornato per rimozione symlink desktop ADM

## [1.0.0] - 2026-04-10

### Aggiunto - 2026-04-10

- Rilascio iniziale dell'applicazione Meteo per ASUSTOR NAS
- **Migrazione a Open-Meteo API** - Nessuna API key richiesta
- Supporto meteo attuale con descrizioni in italiano
- Previsioni 5 giorni con min/max temperature
- Interfaccia in italiano
- Icone SVG meteo integrative con design moderno
- Supporto per qualsiasi città mondiale
- Salvataggio preferenze utente (città) in localStorage
- Supporto multilingua (Italiano/Inglese)
- Pacchetto ASUSTOR APK compatibile con App Central
- Script di installazione, avvio e stop automatizzati
- Documentazione completa in italiano

### Caratteristiche Tecniche

- Backend in Python Flask
- Frontend HTML5, CSS3, JavaScript vanilla
- API RESTful per dati meteo
- Compatibilità con ASUSTOR ADM 2.0+
- Porta 8000 configurabile
- Database SQLite integrato

---

© Copyright 2024-2026 Nsfr750 - All rights reserved.
