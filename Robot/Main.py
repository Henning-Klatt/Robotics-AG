from Robot import *

rob = Robot()

def followline():
    """ Follow the line """
    rob.sensorbar()

    if (rob.colors[3], rob.colors[4]) == (BLACK, BLACK):
        rob.motor('lr', rob.baseSpeed)

    elif not rob.colors[4]: # Rob to far left
        rob.motor('l', int(rob.baseSpeed * 1.5))
        if not rob.colors[3]: # Rob farer left
            rob.motor('r', int(rob.baseSpeed * .5))
        if not rob.colors[2]:
            rob.motor('l', int(rob.baseSpeed * 2))
        if not rob.colors[1]:
            rob.motor('r', int(rob.baseSpeed * 0))
        if not rob.colors[0]:
            rob.motor('l', int(rob.baseSpeed * 3))

    elif not rob.colors[3]: # Rob to far right
        rob.motor('r', int(rob.baseSpeed * 1.5))
        if not rob.colors[4]: # Rob farer right
            rob.motor('l', int(rob.baseSpeed * .5))
        if not rob.colors[5]:
            rob.motor('r', int(rob.baseSpeed * 2))
        if not rob.colors[6]:
            rob.motor('l', int(rob.baseSpeed * 0))
        if not rob.colors[7]:
            rob.motor('r', int(rob.baseSpeed * 3))

if __name__ == "__main__":
    while True:
        followline()
