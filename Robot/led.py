
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

RGB = [7,15,16]
for pin in RGB:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,1)

try:
        while(True):
                request = raw_input("RGB==>")
                if (len(request) ==3):
                    GPIO.output(RGB[0],int(request[0]))
                    GPIO.output(RGB[1],int(request[1]))
                    GPIO.output(RGB[2],int(request[2]))

except KeyboardInterrupt:
        GPIO.cleanup
