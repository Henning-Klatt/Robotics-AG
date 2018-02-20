# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *

import argparse
import signal
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def signal_handler(signal, frame):
        colorWipe(strip, Color(0,0,0))
        sys.exit(0)

def opt_parse():
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', action='store_true', help='clear the display on exit')
        args = parser.parse_args()
        if args.c:
                signal.signal(signal.SIGINT, signal_handler)

LED_COUNT      = 8
LED_PIN        = 21
LED_FREQ_HZ    = 800000
LED_DMA        = 5
LED_BRIGHTNESS = 255
LED_INVERT     = False
LED_CHANNEL    = 0
LED_STRIP      = ws.WS2811_STRIP_GRB

def color(r, g, b):
	for i in range(strip.numPixels()):
                strip.setPixelColor(i, Color(r, g, b))
                strip.show()

counter = 0
def button(channel):
    global counter
    if(counter == 0):
        counter = 1
        color(255, 255, 255)
        return
    if(counter == 1):
        counter = 2
        color(255, 0, 0)
        return
    if(counter == 2):
        counter = 3
        color(0, 255, 0)
        return
    if(counter == 3):
        counter = 4
        color(0, 0, 255)
        return
    if(counter == 4):
        counter = 0
        color(0, 0, 0)
        return
    print("LED " + str(counter))

if __name__ == '__main__':
    GPIO.add_event_detect(18, GPIO.RISING, callback=button, bouncetime=300)
    opt_parse()
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    strip.begin()

    print ('Ctrl+C')
    while True:
        try:
             time.sleep(1)
#            color(255, 255, 255)
#            time.sleep(.01)
#            color(0, 255, 0)
#            time.sleep(.01)
        except (KeyboardInterrupt, SystemExit):
            color(0, 0, 0)
            break
