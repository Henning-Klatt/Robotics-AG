import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BOARD)

RGB = [7,15,16]
for pin in RGB:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,1)

try:
        while(True):
                
                   GPIO.output(RGB[0],0)
                   time.sleep(.5) 
                   GPIO.output(RGB[0],1)
                   time.sleep(.5)
                   GPIO.output(RGB[1],0)
                   time.sleep(.5)
                   GPIO.output(RGB[1],1)
                   time.sleep(.5) 
                   GPIO.output(RGB[2],0)
                   time.sleep(.5)
                   GPIO.output(RGB[2],1)
                   time.sleep(.5)
                   GPIO.output(RGB[0],0)
                   time.sleep(.5)
                   GPIO.output(RGB[0],1) 
except KeyboardInterrupt:
        GPIO.cleanup()

