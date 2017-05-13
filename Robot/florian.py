from Brick import *
import time
BrickPiSetup()
BrickPi.MotorEnable[PORT_A] = 1
BrickPi.MotorEnable[PORT_B] = 1
while(True):
	BrickPi.MotorSpeed[PORT_A] = 200
	BrickPi.MotorSpeed[PORT_B] = 200
	BrickPiUpdateValues()
	time.sleep(1)
	BrickPi.MotorSpeed[PORT_A] = -200
	BrickPi.MotorSpeed[PORT_B] = -200
	BrickPiUpdateValues()
	time.sleep(1)

