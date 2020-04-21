from LED import LED
from flask import Flask
from flask import render_template, request, redirect, url_for
import thread

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

led1_red_pin = 23
led1_green_pin = 24
led1_bluepin = 25
led_1 = LED(0, 0, 0, 1,led1_red_pin,led1_green_pin,led1_bluepin)
led_1.gpio()


led2_red_pin = 16
led2_green_pin = 26
led2_bluepin = 21
led_2 = LED(0, 0, 0, 1,led2_red_pin,led2_green_pin,led2_bluepin)
led_2.gpio()


led3_red_pin = 17
led3_green_pin = 27
led3_bluepin = 22
led_3 = LED(0, 0, 0, 1,led3_red_pin,led3_green_pin,led3_bluepin)
led_3.gpio()


led4_red_pin = 5
led4_green_pin = 6
led4_bluepin = 13
led_4 = LED(0, 0, 0, 1,led4_red_pin,led4_green_pin,led4_bluepin)
led_4.gpio()


""" KSD  """


@app.route('/change_led1/')
@app.route('/change_led1/<int:power>')
@app.route('/change_led1/<int:red>,<int:green>,<int:blue>')
@app.route('/change_led1/<int:red>,<int:green>,<int:blue>,<int:power>')
def change_led1(red=None, green=None, blue=None, power=None):
    led_1.fading = False
    # only update color if a color is specified and max is 255
    if red is None:
        red = led_1.red
    elif red > 255:
        red = 255
    elif red < 0:
        red = 0

    if green is None:
        green = led_1.green
    elif green > 255:
        green = 255
    elif green < 0:
        green = 0

    if blue is None: 
        blue = led_1.blue
    elif blue > 255:
        blue = 255
    elif blue < 0:
        blue = 0

    if power is None:
        power = led_1.power
    elif power > 1:
        power = 1
    elif power < 0:
        power = 0

    led_1.update(red, green, blue, power)

    if power == 0:
        print("powering off")
        led_1.off()
    else:
        led_1.gpio()

    return "R: " + str(led_1.red) +  " G: " + str(led_1.green) + " B: " + str(led_1.blue) + " Power: " + str(led_1.power)



@app.route('/change_led2/')
@app.route('/change_led2/<int:power>')
@app.route('/change_led2/<int:red>,<int:green>,<int:blue>')
@app.route('/change_led2/<int:red>,<int:green>,<int:blue>,<int:power>')
def change_led2(red=None, green=None, blue=None, power=None):
    led_2.fading = False
    # only update color if a color is specified and max is 255
    if red is None:
        red = led_2.red
    elif red > 255:
        red = 255
    elif red < 0:
        red = 0

    if green is None:
        green = led_2.green
    elif green > 255:
        green = 255
    elif green < 0:
        green = 0

    if blue is None: 
        blue = led_2.blue
    elif blue > 255:
        blue = 255
    elif blue < 0:
        blue = 0

    if power is None:
        power = led_2.power
    elif power > 1:
        power = 1
    elif power < 0:
        power = 0

    led_2.update(red, green, blue, power)

    if power == 0:
        print("powering off")
        led_2.off()
    else:
        led_2.gpio()

    return "R: " + str(led_2.red) +  " G: " + str(led_2.green) + " B: " + str(led_2.blue) + " Power: " + str(led_2.power)





@app.route('/change_led3/')
@app.route('/change_led3/<int:power>')
@app.route('/change_led3/<int:red>,<int:green>,<int:blue>')
@app.route('/change_led3/<int:red>,<int:green>,<int:blue>,<int:power>')
def change_led3(red=None, green=None, blue=None, power=None):
    led_3.fading = False
    # only update color if a color is specified and max is 255
    if red is None:
        red = led_3.red
    elif red > 255:
        red = 255
    elif red < 0:
        red = 0

    if green is None:
        green = led_3.green
    elif green > 255:
        green = 255
    elif green < 0:
        green = 0

    if blue is None: 
        blue = led_3.blue
    elif blue > 255:
        blue = 255
    elif blue < 0:
        blue = 0

    if power is None:
        power = led_3.power
    elif power > 1:
        power = 1
    elif power < 0:
        power = 0

    led_3.update(red, green, blue, power)

    if power == 0:
        print("powering off")
        led_3.off()
    else:
        led_3.gpio()

    return "R: " + str(led_3.red) +  " G: " + str(led_3.green) + " B: " + str(led_3.blue) + " Power: " + str(led_3.power)



@app.route('/change_led4/')
@app.route('/change_led4/<int:power>')
@app.route('/change_led4/<int:red>,<int:green>,<int:blue>')
@app.route('/change_led4/<int:red>,<int:green>,<int:blue>,<int:power>')
def change_led4(red=None, green=None, blue=None, power=None):
    led_4.fading = False
    # only update color if a color is specified and max is 255
    if red is None:
        red = led_4.red
    elif red > 255:
        red = 255
    elif red < 0:
        red = 0

    if green is None:
        green = led_4.green
    elif green > 255:
        green = 255
    elif green < 0:
        green = 0

    if blue is None: 
        blue = led_4.blue
    elif blue > 255:
        blue = 255
    elif blue < 0:
        blue = 0

    if power is None:
        power = led_4.power
    elif power > 1:
        power = 1
    elif power < 0:
        power = 0

    led_4.update(red, green, blue, power)

    if power == 0:
        print("powering off")
        led_4.off()
    else:
        led_4.gpio()

    return "R: " + str(led_4.red) +  " G: " + str(led_4.green) + " B: " + str(led_4.blue) + " Power: " + str(led_4.power)



