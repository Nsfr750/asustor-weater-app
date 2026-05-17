# Weather App for ASUSTOR NAS

Weather application for ASUSTOR NAS Lockerstor 6604T (and other compatible models). Displays current weather conditions and 5-day forecasts.

© Copyright 2024-2026 Nsfr750 - All rights reserved.
License: GPLv3

## 📋 Features

- Current weather conditions display
- 5-day weather forecasts with min/max temperatures
- **Historical statistics** with interactive charts (temperature, humidity, pressure, wind)
- **SQLite Database** for daily and hourly data storage
- **Dedicated page** (`/stats`) with trends and summaries
- **Multi-language support IT/EN** with language selector in menu
- **Complete internationalization system** (i18n)
- Modern and responsive web interface
- Support for cities worldwide
- **No API key required** - Free and open source
- City preferences saving (localStorage)
- Data provided by [Open-Meteo](https://open-meteo.com)

## 🚀 Installation

### Method 1: App Central (Recommended)

1. Download the `.apk` file from the [Releases](https://github.com/Nsfr750/asustor-weather-app/releases) section
2. Open App Central on your ASUSTOR NAS
3. Click on "Manual Installation"
4. Select the downloaded `.apk` file
5. Follow the guided procedure

### Method 2: Manual via SSH

1. Connect to NAS via SSH:

   ```bash
   ssh admin@your-nas-ip
   ```

2. Download the application:

   ```bash
   cd /usr/local/AppCentral
   git clone https://github.com/Nsfr750/asustor-weather-app.git weather-app
   cd weather-app
   ```

3. Install dependencies:

   ```bash
   python3 -m pip install -r requirements.txt --user
   ```

4. Start the application:

   ```bash
   ./start.sh
   ```

5. Access the app: `http://your-nas-ip:8000`

## Configuration

### Language Change

The app supports Italian  and English :

1. Use the language selector in the navigation menu
2. The chosen language is saved automatically
3. All interface strings update in real time

### First Configuration

The app requires no configuration. On first launch:

1. Enter the desired city name
2. Click on "Search"
3. The city is saved automatically for future access

## Statistics and Charts

The app includes a dedicated page for historical statistics:

- **Access**: Click on " Statistics" in the navigation menu or go to `http://your-nas-ip:8000/stats`
- **Stored data**: Every weather search automatically saves data to SQLite database
- **Available periods**: 7, 30, 90 days or 1 year
- **Available charts**:
  - Temperature trend (max, avg, min)
  - Average humidity
  - Atmospheric pressure
  - Wind speed
  - Hourly trend of last 24 hours

**Note**: Data accumulates automatically with every search. The more often you search for weather, the more data you'll have in the charts!

## 📁 Project Structure

```text
asustor-weather-app/
├── CONTROL/                    # ASUSTOR control files (apkg-tools)
│   ├── config.json             # ASUSTOR package configuration
│   ├── apkg-version            # App version
│   ├── icon.png                # App icon
│   ├── icon-enable.png         # Active icon (ADM desktop)
│   ├── icon-disable.png        # Disabled icon (ADM desktop)
│   ├── install.sh              # Installation script
│   ├── uninstall.sh            # Uninstallation script
│   ├── start.sh                # Start script
│   ├── stop.sh                 # Stop script
│   ├── changelog.txt           # Changelog for ASUSTOR
│   └── description.txt         # Short description
├── data/                       # Application files
│   ├── app.py                  # Flask backend with Open-Meteo API and database
│   ├── database.py             # SQLite module for historical data
│   ├── lang/                   # Internationalization system
│   │   ├── __init__.py
│   │   ├── translations.py     # IT/EN dictionaries
│   │   └── language_manager.py # Backend language management
│   ├── requirements.txt        # Python dependencies
│   ├── version.py              # App version
│   ├── templates/
│   │   ├── index.html          # Main weather interface
│   │   └── stats.html          # Statistics page with charts
│   └── static/
│       ├── style.css           # CSS styles
│       ├── app.js              # Main frontend script
│       ├── stats.js            # Chart.js charts script
│       └── i18n.js             # Frontend lang
├── apkg-tools.py               # ASUSTOR tool for APK creation (optional)
├── apkg-developer-guide.md     # ASUSTOR developer guide
├── apkg-version                # ASUSTOR package version
├── README.md                   # Documentation
├── CHANGELOG.md                # Version history
├── LICENSE                     # GPLv3 license
└── weather_data.db             # SQLite database (created automatically)
```

## 📦 APK Package Creation

To create the installable `.apk` file for ASUSTOR NAS:

### Method 1: apkg-tools.py (Recommended)

Use the official ASUSTOR tool to create the package:

1. Clone the repository:

   ```bash
   git clone https://github.com/Nsfr750/asustor-weather-app.git
   cd asustor-weather-app
   ```

2. Update the version in `CONTROL/apkg-version` and `data/version.py`

3. Run the ASUSTOR tool:

   ```bash
   python apkg-tools_py3.py create . --destination .
   ```

4. At the end you will find the file `weather-app_{version}_any.apk` in the main directory.

### Method 2: Bash Script (Alternative)

On Linux/macOS/WSL you can use the shell script:

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

### APK Structure

The generated `.apk` file contains:

- `control.tar.gz`: ASUSTOR control files (config.json, scripts, icon)
- `data.tar.gz`: complete application (Python, templates, static)
- `apkg-version`: file with package version

### Package Installation

1. Open **App Central** on your ASUSTOR NAS
2. Click on **"Manual Installation"**
3. Select the generated `.apk` file
4. Follow the guided procedure

## Requirements

- ASUSTOR NAS with ADM 2.0+
- Python 3.8+
- Port 8000 available
- Internet connection (for weather data)
- 50MB free space (for historical database)

## Troubleshooting

### App doesn't start

- Verify that Python 3 is installed: `python3 --version`
- Check logs: `/usr/local/AppCentral/weather-app/logs/app.log`
- Verify that port 8000 is free

### Weather data doesn't load

- Verify NAS internet connection
- Verify that Open-Meteo service is reachable
- Try with another city (some names may have variants)

## Changelog

### v1.2.0 (2026-05-17)

- Updated CONTROL scripts for correct file paths (app.py instead of ddns_updater.py)
- Updated apkg-tools.py for Weather App (removed No-IP references)
- Updated all documentation to English language
- Fixed version consistency across all configuration files
- Improved package build scripts and installation process

### v1.1.0 (2026-04-13)

- **Historical statistics** with interactive charts (Chart.js)
- **SQLite Database** for weather data storage
- **Multi-language support IT/EN** with language selector
- **Complete internationalization system** (i18n)
- Dedicated page `/stats` with trends and summaries
- Automatic data storage on every search
- Extended ADM compatibility to 2.0+
- APK structure: CONTROL/ and data/ (standard ASUSTOR format)
- Enable/disable icons for ADM desktop visualization
- Automatic app start after installation

### v1.0.0 (2026-04-10)

- Initial release
- Current weather and forecast support
- Italian interface

## 👤 Author

## Nsfr750 - Tuxxle

- GitHub: [@Nsfr750](https://github.com/Nsfr750)
- Email: [NSFR750](mailto:nsfr750@yandex.com)
- Website: [https://www.tuxxle.org](https://www.tuxxle.org)

## 💰 Support Development

- **PayPal**: [paypal.me/3dmega](https://paypal.me/3dmega)
- **Monero**: `47Jc6MC47WJVFhiQFYwHyBNQP5BEsjUPG6tc8R37FwcTY8K5Y3LvFzveSXoGiaDQSxDrnCUBJ5WBj6Fgmsfix8VPD4w3gXF`

## 📜 License

This project is released under **GPLv3** license. See LICENSE file for details.

---

© Copyright 2024-2026 Nsfr750 - All rights reserved.
