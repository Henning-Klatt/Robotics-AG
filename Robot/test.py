from BrickPiM import *
from time import sleep

b = BrickPi()
b.updateSpeed(0, 100)
b.updateSpeed(1, 100)

sleep(1)

i = 0

while True:
    b.updateDirection(0, 1)
    b.updateDirection(1, 0)

    sleep(1)

    b.updateDirection(0, 0)
    b.updateDirection(1, 1)

    sleep(1)
