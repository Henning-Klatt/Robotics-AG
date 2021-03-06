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

        if (rob.light[3] == BLACK and rob.light[4] == BLACK):
            rob.motor('rl', rob.baseSpeed)
            return 
        elif (BLACK in rob.light[4:7]):
            O = 7; OM = 6; MI = 5; I = 4;
            forw = 'l'; back = 'r'
            every = [O, OM, MI, I]
        elif (BLACK in rob.light[0:3]):
            O = 0; OM = 1; MI = 2; I = 3
            forw = 'r'; back = 'l'
            every = [O, OM, MI, I]
        else:
            rob.motor('lr', rob.baseSpeed)
            return
        if O == BLACK:
            rob.motor(back, -rob.baseSpeed, 180, blocking=False)
            rob.motor(forw, rob.baseSpeed, 180)
            print("0")
            return
        rob.motor(back, -rob.baseSpeed * 0.5)
        rob.motor(forw, rob.baseSpeed)

if __name__ == "__main__":
    m = main()
