from BrickPi import *
import time
BrickPiSetup()
BrickPi.MotorEnable[PORT_A] = 1
BrickPi.MotorEnable[PORT_B] = 1
while(True):
    motorRotateDegree([100,100],[300,300],[PORT_A,PORT_B])
    motorRotateDegree([100,100],[-300,300],[PORT_A,PORT_B])
    time.sleep(2)
    motorRotateDegree([100,100],[-300,-300],[PORT_A,PORT_B])
    motorRotateDegree([100,100],[300,-300],[PORT_A,PORT_B])
    time.sleep(2)

