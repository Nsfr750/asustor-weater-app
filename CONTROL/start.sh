#!/bin/bash
# Start script for ASUSTOR NAS Weather App
# © Copyright 2024-2026 Nsfr750 - All rights reserved.
# Licensed under GPLv3

APP_DIR="/usr/local/AppCentral/weather-app"
LOG_FILE="${APP_DIR}/logs/app.log"
PID_FILE="${APP_DIR}/weather-app.pid"

# Check if already running
if [ -f "${PID_FILE}" ]; then
    PID=$(cat "${PID_FILE}")
    if kill -0 "${PID}" 2>/dev/null; then
        echo "Weather App is already running (PID: ${PID})"
        exit 0
    fi
fi

# Start the application
echo "Starting Weather App..."
cd "${APP_DIR}"
nohup python3 app.py >> "${LOG_FILE}" 2>&1 &
NEW_PID=$!
echo ${NEW_PID} > "${PID_FILE}"

echo "Weather App started with PID: ${NEW_PID}"
echo "Access the app at http://[NAS-IP]:8000"

exit 0
