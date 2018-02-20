#!/usr/bin/python3
from Robot import *
from Debug import *
from time import sleep
import sys
rob = Robot()
debug = Debug()

def followline():
    """ Follow the line """
    rob.sensorbar()

    if rob.light[3] == BLACK and rob.light[4] == BLACK:
        rob.motor('rl', rob.baseSpeed)
        debug.log("straight")
        return
    elif BLACK in rob.light[4:7] and not (BLACK in rob.light[0:3]): # Line right
        # Outside; Outside Middle; Middle inside; Inside
        #O = 0; OM = 1; MI = 2; I = 3
        #every = [I,MI,OM,O]
        #forw = 'r'; back = 'l'
        rob.motor('l', rob.baseSpeed)
        rob.motor('r', 0.5 * -rob.baseSpeed)
        debug.log("left")
    elif BLACK in rob.light[0:3] and not (BLACK in rob.light[4:7]): # Line left
        # Outside; Outside Middle; Middle inside; Inside
        #O = 7; OM = 6; MI = 5; I = 4
        #every = [I,MI,OM,O]
        #forw = 'l'; back = 'r'
        rob.motor('l', 0.5 * -rob.baseSpeed)
        rob.motor('r', rob.baseSpeed)
        debug.log("right")
    else:
        rob.motor('rl', 0)
        debug.log("stop")
        return

    #rob.motor(back, 0)
    #rob.motor(forw, rob.baseSpeed)

if __name__ == "__main__":
    try:
        rob.motor('rl', 0) # Test brickpi.
        while True:
            followline()
            debug.showValues(rob)
            sleep(rob.sample)

    except Exception as e:
        debug.clear()
        print(e)

    finally:
        sleep(.1)
        debug.clear()
        rob.motor('l', 0)
        rob.motor('r', 0)
        rob.close()
        sys.exit(0)
