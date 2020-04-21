#!/bin/bash
if [ "$1" != "-d" ]; then
    export FLASK_DEBUG=1
fi
export FLASK_APP=/home/pi/led_project/method3_ksd/server.py
#sudo pigpiod
flask run --host=0.0.0.0
