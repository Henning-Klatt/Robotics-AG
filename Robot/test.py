from Robot import *
import time

rob = Robot()

while True:
    print(rob.ReadChannel())
    time.sleep(1)
