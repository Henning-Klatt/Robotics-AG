#!/usr/bin/python3
from Robot import *
from Debug import *
from time import sleep
import sys
rob = Robot()
#debug = Debug()

class main(object):
    def __init__(self):
        try:
            rob.motor('rl', 0) # Test brickpi.
            print("start")
            while True:
                self.followline()
                print(rob.light)
                #debug.showValues(rob)
                sleep(rob.sample)
    
        except Exception as e:
            #debug.clear()
            print(e)
    
        finally:
            sleep(.1)
            #debug.clear()
            rob.motor('l', 0)
            rob.motor('r', 0)
            rob.close()
            sys.exit(0)

    def followline(self):
        """ Follow the line """
        rob.sensorbar()
        rob.motor('lr', rob.baseSpeed)

        if (rob.light[3] == BLACK and rob.light[4] == BLACK):
            rob.motor('rl', rob.baseSpeed)
        elif (BLACK in rob.light[4:7]):
            print("r")
            rob.motor('r', -rob.baseSpeed * 1.5)
            rob.motor('l', rob.baseSpeed * 1.5)
            sleep(.1)
        elif (BLACK in rob.light[0:3]):
            print("l")
            rob.motor('l', -rob.baseSpeed * 1.5)
            rob.motor('r', rob.baseSpeed * 1.5)

if __name__ == "__main__":
    m = main()
