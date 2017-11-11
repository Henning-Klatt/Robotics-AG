#!/usr/bin/python3
from Robot import *
from debug import *
from time import sleep
import sys
rob = Robot()
debug = Debug()

def followline():
    """ Follow the line """
    rob.sensorbar()
    #rob.motor('l', rob.baseSpeed)
    #rob.motor('r', rob.baseSpeed)

    if rob.colors[3] == BLACK and rob.colors[4] == BLACK:
        rob.motor('l', rob.baseSpeed)
        rob.motor('r', rob.baseSpeed)
        return
    elif BLACK in rob.colors[0:3] and not (BLACK in rob.colors[4:7]): # Line right
        # Outside; Outside Middle; Middle inside; Inside
        O = 0; OM = 1; MI = 2; I = 3
        every = [I,MI,OM,O]
        forw = 'r'; back = 'l'
    elif BLACK in rob.colors[4:7] and not (BLACK in rob.colors[0:3]): # Line left
        O = 7; OM = 6; MI = 5; I = 4
        every = [I,MI,OM,O]
        forw = 'l'; back = 'r'
    else:
        return

    if rob.colors[I] == BLACK:
        rob.motor('r', rob.baseSpeed - 20)
    if rob.colors[MI] == BLACK:
        rob.motor('r', rob.baseSpeed - 40)
    if rob.colors[OM] == BLACK:
        rob.motor('r', rob.baseSpeed - 80)
    if rob.colors[O] == BLACK:
        rob.motor('r', rob.baseSpeed - 100)

if __name__ == "__main__":
    try:
        rob.motor('rl', 0) # Test brickpi.
        while True:
            followline()
            debug.showValues(rob)
            debug.log("test")
            sleep(rob.sample)
            debug.log("test")

    except Exception as e:
        sleep(.1)
        rob.motor('l', 0)
        rob.motor('r', 0)
        rob.close()
        debug.clear()
        print(e)

    finally:
        sleep(.1)
        rob.motor('l', 0)
        rob.motor('r', 0)
        rob.close()
        debug.clear()
        sys.exit(0)
