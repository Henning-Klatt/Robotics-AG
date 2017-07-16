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

    if rob.colors[3] == BLACK or rob.colors[4] == BLACK:
        rob.motor('l', rob.baseSpeed)
        rob.motor('r', rob.baseSpeed)
    elif BLACK in rob.colors[5:7] and not (BLACK in rob.colors[0:3]): # Line left
        rob.motor('r', 0)
    elif BLACK in rob.colors[0:2] and not (BLACK in rob.colors[4:7]): # Line right
        rob.motor('l',0)

def printc():
    rob.sensorbar()
    print(rob.colors)


if __name__ == "__main__":
    try:
        while True:
            followline()
            #debug.log()

    except KeyboardInterrupt:
        rob.motor('r', 0)
        rob.motor('l', 0)
        debug.clear()
        print("Beende Hauptprogramm, um Debug zu beenden drücke Q")
