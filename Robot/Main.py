#!/usr/bin/python3
from Robot import *
from debug import *
from time import sleep
rob = Robot()
debug = Debug()

def followline():
    """ Follow the line """
    rob.sensorbar()

    #rob.colors = reversed(rob.colors)

    if rob.colors[3] == BLACK and rob.colors[4] == BLACK:
        rob.motor('lr', rob.baseSpeed)
    elif BLACK in rob.colors[5:7] and not (BLACK in rob.colors[0:4]): # Line left
        rob.motor('r', rob.baseSpeed)
        rob.motor('l', -(rob.baseSpeed / 3))

        if rob.colors[7] == BLACK:
            rob.motor('l', -rob.baseSpeed)
        if rob.colors[6] == BLACK:
            rob.motor('r', rob.maxSpeed)
    elif BLACK in rob.colors[0:2] and not (BLACK in rob.colors[3:7]): # Line right
        rob.motor('l', rob.baseSpeed)
        rob.motor('r', -(rob.baseSpeed / 3))

        if rob.colors[0] == BLACK:
            rob.motor('r', -rob.baseSpeed)
        if rob.colors[1] == BLACK:
            rob.motor('l', rob.maxSpeed)

    sleep(rob.sample)

def printc():
    rob.sensorbar()
    print(rob.colors)


if __name__ == "__main__":
    try:
        while True:
            #sleep(1)
            #followline()
            #debug.log()
            pass

    except KeyboardInterrupt:
        rob.motor('r', 0)
        rob.motor('l', 0)
        #debug.clear()
        print("Beende Hauptprogramm, um Debug zu beenden drücke Q")
