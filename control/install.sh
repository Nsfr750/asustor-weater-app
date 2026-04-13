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

# Copy files from data/ subdirectory to app root (APK format compatibility)
if [ -d "${APP_DIR}/data" ]; then
    echo "Copying application files to app root..."
    cp -r "${APP_DIR}/data/"* "${APP_DIR}/"
    # Remove data/ directory after copying (optional - keep it for structure)
    # rm -rf "${APP_DIR}/data"
fi

# Copy files from CONTROL/ directory to app root (control.tar.gz contents)
if [ -d "${APP_DIR}/CONTROL" ]; then
    echo "Copying control files to app root..."
    cp -r "${APP_DIR}/CONTROL/"* "${APP_DIR}/"
fi

# Create symlink for ADM desktop visibility (ADM 2.0+)
if [ -d "/usr/share/appcentral" ]; then
    echo "Registering app with ADM App Central..."
    # Create desktop shortcut
    ln -sf "${APP_DIR}/icon-enable.png" "/usr/share/appcentral/weather-app-enable.png" 2>/dev/null || true
    ln -sf "${APP_DIR}/icon-disable.png" "/usr/share/appcentral/weather-app-disable.png" 2>/dev/null || true
fi

# Set permissions
chmod -R 755 "${APP_DIR}"
touch "${LOG_DIR}/app.log"
chmod 666 "${LOG_DIR}/app.log"
chmod +x /usr/local/AppCentral/weather-app/control/*.sh

# Install Python dependencies
echo "Installing Python dependencies..."
cd "${APP_DIR}"
python3 -m pip install -r requirements.txt --user

# Start the application automatically
echo "Starting Weather App..."
if [ -f "${APP_DIR}/start.sh" ]; then
    chmod +x "${APP_DIR}/start.sh"
    "${APP_DIR}/start.sh"
elif [ -f "${APP_DIR}/CONTROL/start.sh" ]; then
    chmod +x "${APP_DIR}/CONTROL/start.sh"
    "${APP_DIR}/CONTROL/start.sh"
fi

echo "Installation completed!"
echo "App will be available at http://[NAS-IP]:8000"

exit 0
