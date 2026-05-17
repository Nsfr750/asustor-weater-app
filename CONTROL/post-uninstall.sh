#!/bin/sh

# post uninstall script here
# Remove icon from ADM desktop location
rm -f /usr/local/AppCentral/ADM/desktop/weather-app.png 2>/dev/null || true

exit 0
