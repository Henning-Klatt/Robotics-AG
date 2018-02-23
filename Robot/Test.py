from Robot import *
from Arduino import *
import sys

print ("TESTING ARDUINO:\n----------------------------------------")
print("INIT ARDUINO:")
try:
    a = Arduino()
except Exception as e:
    print("Initializing Arduino failed. Error: ")
    print(e)
    sys.exit()
print("OK")

try:
    a.sensorbar()
except Exception as e:
    print("Reading Sensorbar failed. Error: ")
    print(e)
    sys.exit()
print("OK")

try:
    a.colorSensors()
except Exception as e:
    print("Reading color sensors failed. Error: ")
    print(e)
    sys.exit()
print("OK")

try:
    for i in range(8):
        a.neopixel(i, 'R')
        a.neopixel(i, '0')
except Exception as e:
    print("Writing neopixel failed. Error: ")
    print(e)
    sys.exit()
print("OK")

print ("TESTING ROB:\n----------------------------------------")
print("INIT ROB: ")
try:
    r = Robot()
except Exception as e:
    print("Initializing Robot failed. Error: ")
    print(e)
    sys.exit()
print("OK")

print("SENSORBAR: ")
try:
    r.sensorbar()
    print(r.light)
except Exception as e:
    print("Reading sensorbar failed. Error: ")
    print(e)
    r.close()
    sys.exit()
print("OK")

try:
    r.colorSensors()
    print(r.colors)
except Exception as e:
    print("Reading color sensors failed. Error: ")
    print(e)
    r.close()
    sys.exit()
print("OK")

print("BRICKPI: ")
try:
    r.motor('lr', 0)
except Exception as e:
    print("Writing to BrickPi failed. Error: ")
    print(e)
    r.close()
    sys.exit()
print("OK")

r.close()
