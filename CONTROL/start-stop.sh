#!/bin/sh

. /etc/script/lib/command.sh

APKG_PKG_DIR=/usr/local/AppCentral/weather-app
PID_FILE_DD=/var/run/weather-app.pid
PID_FILE_WEB=/var/run/weather-app-web.pid
PYTHON_CMD=/usr/local/bin/python3

case $1 in

	start)
		# start weather service
		$PYTHON_CMD $APKG_PKG_DIR/data/app.py --daemon > /dev/null 2>&1 &
		echo $! > $PID_FILE_DD
		

	stop)
		# stop weather service
		if [ -f $PID_FILE_DD ]; then
			kill -9 `cat $PID_FILE_DD` 2> /dev/null
			rm -rf $PID_FILE_DD
		fi

		;;

	*)
		echo "usage: $0 {start|stop}"
		exit 1
		;;

esac

exit 0
