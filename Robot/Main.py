#!/usr/bin/python3
from Robot import *
from debug import *
from time import sleep
rob = Robot()
#debug = Debug()

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
        rob.motor(back, -rob.minSpeed)
        rob.motor(forw, rob.baseSpeed)
    if rob.colors[MI] == BLACK:
        rob.motor(back, -rob.minSpeed)
        rob.motor(forw, rob.baseSpeed)
    if rob.colors[OM] == BLACK:
        pass
    if rob.colors[O] == BLACK:
        pass

if __name__ == "__main__":
    try:
        while True:
            followline()
            sleep(rob.sample)
            #debug.log()

    except KeyboardInterrupt:
        rob.motor('l', 0)
        rob.motor('r', 0)
        rob.close()
        #debug.clear()
        print("Beende Hauptprogramm, um Debug zu beenden druecke Q")
