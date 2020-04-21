import pigpio
import time

pi = pigpio.pi()


class LED():
    red = 0
    green = 0
    blue = 0
    power = 1
    speed = 50
    fading = False
    red_pin = 17
    green_pin = 22
    blue_pin = 24
	

    def __init__(self, red, green, blue, power,red_pin,green_pin,blue_pin):
        self.red = red
        self.green = green
        self.blue = blue
        self.power = power
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin

    def update(self, red, green, blue, power):
        self.red = red
        self.green = green
        self.blue = blue
        self.power = power

    def gpio(self):
        pi.set_PWM_dutycycle(self.red_pin, self.red * self.power)
        pi.set_PWM_dutycycle(self.green_pin, self.green * self.power)
        pi.set_PWM_dutycycle(self.blue_pin, self.blue * self.power)

    def sleep(self):
        self.fading = True
        self.speed = 65;
        step = -1

        rBeg = self.red
        gBeg = self.green
        bBeg = self.blue
        rDiff = self.red / 100
        gDiff = self.green / 100
        bDiff = self.blue / 100

        while self.fading:
            if step > 0:
                beg = 100
                end = 0
                step = -1
            else:
                beg = 0
                end = 100
                step = 1
            for i in range(beg, end, step):
                self.power = i/100
                pi.set_PWM_dutycycle(self.red_pin, self.red * self.power)
                pi.set_PWM_dutycycle(self.green_pin, self.green * self.power)
                pi.set_PWM_dutycycle(self.blue_pin, self.blue * self.power)
                time.sleep(self.speed / 1000)


    def fade(self, toRed, toGreen, toBlue, speed=65):
        self.fading = True
        self.speed = speed
        rBeg = self.red
        gBeg = self.green
        bBeg = self.blue

        rDiff = (toRed - self.red) / 100
        gDiff = (toGreen - self.green) / 100
        bDiff = (toBlue - self.blue) / 100
        print("Increments:\nr:{0}, g:{1}, b:{2}".format(rDiff, gDiff, bDiff))
        step = -1

        while self.fading:
            if step > 0:
                beg = 100
                end = 0
                step = -1
            else:
                beg = 0
                end = 100
                step = 1
            for i in range(beg, end, step):
                red = rBeg + i * rDiff
                green = gBeg + i * gDiff
                blue = bBeg + i * bDiff
                pi.set_PWM_dutycycle(self.red_pin, red * self.power)
                pi.set_PWM_dutycycle(self.green_pin, green * self.power)
                pi.set_PWM_dutycycle(self.blue_pin, blue * self.power)
                time.sleep(self.speed / 1000)

        print("EXITING FADE")

    def off(self):
        pi.set_PWM_dutycycle(self.red_pin, 0)
        pi.set_PWM_dutycycle(self.green_pin, 0)
        pi.set_PWM_dutycycle(self.blue_pin, 0)
