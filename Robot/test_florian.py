from BrickPi import *
BrickPiSetup()
BrickPi.MotorEnable[PORT_C] = 1
BrickPi.MotorEnable[PORT_B] = 1

def Cycle(speed):   
 while True:
        motorRotateDegree([220,220],[720,720],[PORT_B,PORT_C])
        time.sleep(2)
        motorRotateDegree([220,220],[-720,-720],[PORT_B,PORT_C])
        break()
Cycle(100)

def Hue(light):
  while True:
       
