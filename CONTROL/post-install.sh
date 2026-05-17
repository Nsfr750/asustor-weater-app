#!/bin/sh

APKG_PKG_DIR=/usr/local/AppCentral/weather-app

case "$APKG_PKG_STATUS" in

	install)
		# post install script here
		mkdir -p $APKG_PKG_DIR/etc
		chmod 755 $APKG_PKG_DIR/data/app.py
		;;
	upgrade)
		# post upgrade script here (restore data)
		if [ -d $APKG_TEMP_DIR ]; then
			cp -af $APKG_TEMP_DIR/* $APKG_PKG_DIR/etc/.
		fi
		chmod 755 $APKG_PKG_DIR/data/app.py
		;;
	*)
		;;

esac

exit 0
