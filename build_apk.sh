#!/bin/bash
# Build script for ASUSTOR APK package
# © Copyright 2024-2026 Nsfr750 - All rights reserved.
# Licensed under GPLv3
#
# ASUSTOR APK Format:
# - control.tar.gz: apkg.xml, icon.png, install.sh, uninstall.sh, start.sh, stop.sh, apkg-version
# - data.tar.gz: application files (app.py, templates, static, etc.)
# - Combined into .apk (tar.gz archive)

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
mkdir -p "${BUILD_DIR}/control"
mkdir -p "${BUILD_DIR}/data"

# Update version in apkg.xml to match version.py
echo "Updating apkg.xml version to ${VERSION}..."
sed -i "s|<version>.*</version>|<version>${VERSION}</version>|" apkg.xml

# Create icon.png if not exists (required by ASUSTOR)
echo "Creating icon.png..."
if command -v convert &> /dev/null; then
    # Create a proper 128x128 icon using ImageMagick
    convert -size 128x128 xc:steelblue -pointsize 60 -fill white \
            -gravity center -annotate +0+0 "☁" "icon.png"
else
    # Create minimal valid PNG placeholder (base64 encoded 1x1 transparent PNG)
    echo "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==" | base64 -d > "icon.png"
fi

# Copy control files to control directory
echo "Preparing control files..."
cp apkg.xml icon.png install.sh uninstall.sh start.sh stop.sh "${BUILD_DIR}/control/"

# Set execute permissions for scripts
chmod +x "${BUILD_DIR}/control/install.sh"
chmod +x "${BUILD_DIR}/control/uninstall.sh"
chmod +x "${BUILD_DIR}/control/start.sh"
chmod +x "${BUILD_DIR}/control/stop.sh"

# Create apkg-version file in control directory
echo "Creating apkg-version file..."
echo "${VERSION}" > "${BUILD_DIR}/control/apkg-version"

# Create control.tar.gz
echo "Creating control.tar.gz..."
cd "${BUILD_DIR}/control"
tar -czf "../control.tar.gz" .
cd ../..

# Copy data files to data directory
echo "Preparing data files..."
cp app.py requirements.txt version.py LICENSE README.md CHANGELOG.md "${BUILD_DIR}/data/"
cp -r templates static "${BUILD_DIR}/data/"

# Create data.tar.gz
echo "Creating data.tar.gz..."
cd "${BUILD_DIR}/data"
tar -czf "../data.tar.gz" .
cd ../..

# Create the final APK archive (contains control.tar.gz and data.tar.gz)
echo "Creating APK package..."
cd "${BUILD_DIR}"
tar -czf "../${APK_FILE}" control.tar.gz data.tar.gz
cd ..

# Cleanup build directory
rm -rf "${BUILD_DIR}"

echo ""
echo "========================================="
echo "  Build completed successfully!"
echo "  Output: ${APK_FILE}"
echo "========================================="
echo ""
echo "APK Structure:"
echo "  - control.tar.gz: apkg.xml, icon.png, scripts, apkg-version"
echo "  - data.tar.gz: application files"
echo ""
echo "Install on ASUSTOR NAS:"
echo "  1. Open App Central"
echo "  2. Click 'Installazione manuale'"
echo "  3. Select ${APK_FILE}"
echo ""
