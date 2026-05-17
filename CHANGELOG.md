# Changelog

All significant changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/lang/it/spec/v2.0.0.html).

## [1.2.0] - 2026-05-17

### Added

- Updated CONTROL scripts for correct file paths
- Updated all documentation to English language
- Fixed version consistency across all configuration files
- Improved package build scripts and installation process

## [1.1.0] - 2026-04-13

### Added (v1.1.0)

- **SQLite database** for storing historical data
- **Statistics page** (`/stats`) with interactive charts (Chart.js)
- **Automatic storage** of weather data with every search
- **Historical charts**: temperature (max/avg/min), humidity, pressure, wind
- **Hourly trend** for the last 24 hours with dual axes
- **Summary cards** with key statistics
- **Multilingual support (IT/EN)** with language selector in the navigation menu
- **Complete internationalization system** (backend + frontend)
- API endpoints for language management (`/api/language`, `/api/translations`)
- Period selector: 7, 30, 90 days, or 1 year
- Navigation menu between Home and Statistics
- API endpoints for statistical data (`/api/stats/*`)
- Automatic cleanup of old data (configurable)

### Changed

- ADM compatibility extended to version 2.0+ (previously 4.0+)
- Removed screenshot requirement from `apkg.xml` for ADM 2.0
- Project structure: files divided into `CONTROL/` and `data/` (standard ASUSTOR APK format)
- Added `icon-enable.png` and `icon-disable.png` icons for ADM desktop view
- Automatic installation: app launches automatically upon completion of installation
- Improved `install.sh` script for copying files to the app root (`CONTROL/` and `data/`)
- Updated `uninstall.sh` script for removing the ADM desktop symlink

## [1.0.0] - 2026-04-10

### Added - 2026-04-10

- Initial release of the Weather app for ASUSTOR NAS
- **Migration to Open-Meteo API** - No API key required
- Current weather support with descriptions in Italian
- 5-day forecast with minimum/maximum temperatures
- Italian interface
- Integrated SVG weather icons with a modern design
- Support for any city worldwide
- User preferences (city) saved in localStorage
- Multilingual support (Italian/English)
- ASUSTOR APK package compatible with App Central
- Automated installation, startup, and shutdown scripts

### Technical Features

- Python Flask backend
- HTML5, CSS3, and vanilla JavaScript frontend
- RESTful API for weather data
- Compatibility with ASUSTOR ADM 2.0+
- Configurable port 8000
- Built-in SQLite database

---

© Copyright 2024-2026 Nsfr750 - All rights reserved.
