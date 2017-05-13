#!/usr/bin/env pyhton

from Brick import *

BrickPiSetup()

BrickPi.MotorEnable[PORT_B] = 1

motorRotateDegree([100, 100], [200, 200], [PORT_B, PORT_A], 0, .005)

print("STOPPED")
