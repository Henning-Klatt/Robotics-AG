from Robot import *
import time

rob = Robot()

rob.motor('lr', 150)
time.sleep(1)
print("Stop")
rob.motor('lr', -1)
time.sleep(5)
# rob.motorRotateDegree([100,100],[-50,-50])
