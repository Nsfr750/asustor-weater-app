#!/bin/bash
# Install script for ASUSTOR NAS Weather App
# © Copyright 2024-2026 Nsfr750 - All rights reserved.
# Licensed under GPLv3

echo "Installing Weather App for ASUSTOR NAS..."

APP_DIR="/usr/local/AppCentral/weather-app"
LOG_DIR="${APP_DIR}/logs"
PID_FILE="${APP_DIR}/weather-app.pid"

# Create necessary directories
mkdir -p "${LOG_DIR}"

# Set permissions
chmod -R 755 "${APP_DIR}"
touch "${LOG_DIR}/app.log"
chmod 666 "${LOG_DIR}/app.log"
chmod +x /usr/local/AppCentral/weather-app/control/*.sh

# Install Python dependencies
echo "Installing Python dependencies..."
cd "${APP_DIR}"
python3 -m pip install -r requirements.txt --user

echo "Installation completed!"
echo "App will be available at http://[NAS-IP]:8000"

exit 0
