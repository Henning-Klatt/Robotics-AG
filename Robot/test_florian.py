from Robot import *
rob = Robot()
import led
import time
def Autismus():
 while True:
       led.set("off")
       rob.motor("rl", 100)
       led.set("red")
       time.sleep(2)
       led.set("off")
       rob.motor("rl", -100)
       led.set("blue")
       time.sleep(.5)
       rob.motor("rl", 0)
       time.sleep(2)
Autismus()
