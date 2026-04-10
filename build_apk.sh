#!/bin/bash
# Build script for ASUSTOR APK package
# © Copyright 2024-2026 Nsfr750 - All rights reserved.
# Licensed under GPLv3

APP_NAME="weather-app"
VERSION=$(python3 -c "from version import __version__; print(__version__)")
BUILD_DIR="build"
APK_FILE="${APP_NAME}-${VERSION}.apk"

echo "========================================="
echo "  Building ASUSTOR Weather App APK"
echo "  Version: ${VERSION}"
echo "========================================="
echo ""

# Clean and create build directory
rm -rf "${BUILD_DIR}"
mkdir -p "${BUILD_DIR}/${APP_NAME}"

# Update version in apkg.xml to match version.py
echo "Updating apkg.xml version to ${VERSION}..."
sed -i "s|<version>.*</version>|<version>${VERSION}</version>|" apkg.xml

# Copy all necessary files
echo "Copying files..."
cp -r app.py requirements.txt version.py \
   install.sh uninstall.sh start.sh stop.sh \
   apkg.xml LICENSE README.md CHANGELOG.md \
   templates static \
   "${BUILD_DIR}/${APP_NAME}/"

# Set execute permissions for scripts
echo "Setting permissions..."
chmod +x "${BUILD_DIR}/${APP_NAME}/install.sh"
chmod +x "${BUILD_DIR}/${APP_NAME}/uninstall.sh"
chmod +x "${BUILD_DIR}/${APP_NAME}/start.sh"
chmod +x "${BUILD_DIR}/${APP_NAME}/stop.sh"

# Create icon.png if not exists (required by ASUSTOR)
echo "Creating icon.png..."
if command -v convert &> /dev/null; then
    # Create a proper 128x128 icon using ImageMagick
    convert -size 128x128 xc:steelblue -pointsize 60 -fill white \
            -gravity center -annotate +0+0 "☁" "${BUILD_DIR}/${APP_NAME}/icon.png"
else
    # Create minimal valid PNG placeholder (base64 encoded 1x1 transparent PNG)
    echo "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==" | base64 -d > "${BUILD_DIR}/${APP_NAME}/icon.png"
fi

# Create screenshot.png placeholder (required by ASUSTOR apkg.xml)
echo "Creating screenshot.png..."
if command -v convert &> /dev/null; then
    # Create a 800x600 screenshot placeholder
    convert -size 800x600 xc:lightblue -pointsize 40 -fill steelblue \
            -gravity center -annotate +0+0 "Weather App\nScreenshot" \
            "${BUILD_DIR}/${APP_NAME}/screenshot.png"
else
    # Create minimal valid PNG placeholder
    echo "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==" | base64 -d > "${BUILD_DIR}/${APP_NAME}/screenshot.png"
fi

# Create the APK archive
echo "Creating APK package..."
cd "${BUILD_DIR}"
tar -czf "../${APK_FILE}" "${APP_NAME}"

echo ""
echo "========================================="
echo "  Build completed successfully!"
echo "  Output: ${APK_FILE}"
echo "========================================="
echo ""
echo "Install on ASUSTOR NAS:"
echo "  1. Open App Central"
echo "  2. Click 'Installazione manuale'"
echo "  3. Select ${APK_FILE}"
echo ""
