#!/bin/bash
# Stop script for ASUSTOR NAS Weather App
# © Copyright 2024-2026 Nsfr750 - All rights reserved.
# Licensed under GPLv3

APP_DIR="/usr/local/AppCentral/weather-app"
PID_FILE="${APP_DIR}/weather-app.pid"

if [ ! -f "${PID_FILE}" ]; then
    echo "Weather App is not running"
    exit 0
fi

PID=$(cat "${PID_FILE}")

if kill -0 "${PID}" 2>/dev/null; then
    echo "Stopping Weather App (PID: ${PID})..."
    kill "${PID}"
    sleep 2
    
    # Force kill if still running
    if kill -0 "${PID}" 2>/dev/null; then
        kill -9 "${PID}"
    fi
    
    echo "Weather App stopped"
else
    echo "Weather App was not running"
fi

rm -f "${PID_FILE}"

exit 0
