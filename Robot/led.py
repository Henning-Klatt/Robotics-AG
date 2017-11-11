import RPi.GPIO as GPIO
from threading import Thread
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

RGB = [7,15,16]
for pin in RGB:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,1)

global mode
mode = "off"

def controller():
    for pin in RGB:
        GPIO.output(pin, 1)
    while(True):
        if(mode == "off"):
            for pin in RGB:
                GPIO.output(pin, 1)
        if(mode == "alarm"):
            GPIO.output(RGB[0],0)
            sleep(.5)
            GPIO.output(RGB[0],1)
            sleep(.2)
        if(mode == "red"):
            GPIO.output(RGB[0], 0)
        if(mode == "green"):
            GPIO.output(RGB[1], 0)
        if(mode == "blue"):
            GPIO.output(RGB[2], 0)
        if(mode == "rainbow"):
            GPIO.output(RGB[0], 0)
            sleep(.1)
            GPIO.output(RGB[1], 0)
            sleep(.1)
            GPIO.output(RGB[2], 0)
            sleep(.1)
            GPIO.output(RGB[0], 1)
            sleep(.1)
            GPIO.output(RGB[1], 1)
            sleep(.1)
            GPIO.output(RGB[0], 0)
            GPIO.output(RGB[1], 0)
            GPIO.output(RGB[2], 1)
            sleep(.1)
            GPIO.output(RGB[2], 0)
            sleep(.1)
            GPIO.output(RGB[0], 1)
            GPIO.output(RGB[1], 1)
            GPIO.output(RGB[2], 1)
        if(mode == "running"):
            GPIO.output(RGB[2], 0)
            sleep(.4)
            GPIO.output(RGB[2], 1)
            sleep(.1)
            GPIO.output(RGB[2], 0)
            sleep(.1)
            GPIO.output(RGB[2], 1)
        sleep(.1)
        

if __name__ != "__main__":
    Thread = Thread(target=controller, args=())
    Thread.setDaemon(1)
    Thread.start()
    
    def set(setmode):
        global mode
        mode = setmode

    

if __name__ == "__main__":
    try:
        while(True):
            request = raw_input("RGB:")
            if (len(request) ==3):
                GPIO.output(RGB[0],int(request[0]))
                GPIO.output(RGB[1],int(request[1]))
                GPIO.output(RGB[2],int(request[2]))

    except KeyboardInterrupt:
        GPIO.cleanup
