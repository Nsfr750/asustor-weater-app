#!/bin/bash
# Uninstall script for ASUSTOR NAS Weather App
# © Copyright 2024-2026 Nsfr750 - All rights reserved.
# Licensed under GPLv3

echo "Uninstalling Weather App..."

APP_DIR="/usr/local/AppCentral/weather-app"
PID_FILE="${APP_DIR}/weather-app.pid"

# Stop the application if running
if [ -f "${PID_FILE}" ]; then
    PID=$(cat "${PID_FILE}")
    if kill -0 "${PID}" 2>/dev/null; then
        echo "Stopping application (PID: ${PID})..."
        kill "${PID}"
        sleep 2
    fi
    rm -f "${PID_FILE}"
fi

echo "Uninstallation completed!"

exit 0
