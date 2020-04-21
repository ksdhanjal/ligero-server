
# Ligero-Server

It is an HTTP server which uses pigpio to change color of analog LED strips(in this case SMD 5050) using Raspberry Pi.

## Prerequisites

### Software Requirements
Raspberry Pi with the following components installed:
 - Python 2.7 or higher
 - pigpio
 - flask
 - apache2 or any other web-server that you prefer

### Hardware Requirements
* LED Strip (SMD 5050 or any other analog LED strip)
* ULN2803 IC
* Power supply: 12v 0.5A
* Jumper wires, soldering wire and flux etc.

## Working
* Flask listens on different URLs, each corresponding to an LED strip
* Once the request is sent, then it changes the color by using pigpio's ```set_PWM_dutycycle``` method
* The request is sent in the format ```{ip-address}/change_led1/red_val,green_val,blue_val,power_status```
* LEDs can be turned on and off by sending just the power value in the url (0 for off and 1 for on)  ```{ip-address}/change_led1/power_status```

##  Customization

You can add or remove the number of LEDs by changing ```server.py```
* Define pins for RGB strip
* Instantiate an object of class ```LED``` for the said LED strip
* Create a url for that LED strip
* You can use the implementation of pigpio methods in ```LED.py``` as I did or you can customize it according to your own needs

## Deploying your flask app

Consider checking [this](https://flask.palletsprojects.com/en/1.1.x/deploying/) link to deploy your flask app 

## External Links

* [pigpio](http://abyz.me.uk/rpi/pigpio/download.html) library
* [Pulse Width Modulation](https://en.wikipedia.org/wiki/Pulse-width_modulation)
* Wiring: Same as used in [this](http://lifeofpenguin.blogspot.com/2015/07/mood-lighting-with-rpi.html) article (schemaics and wiring procedure used in this case will be uploaded shortly)
* You can also use MOSFETS as described in [this](https://dordnung.de/raspberrypi-ledstrip/) article

## Acknowledgements
* Original project by [@cashc](https://github.com/cashc/PiLi)
