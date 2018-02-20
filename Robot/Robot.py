#!/usr/bin/python3
""" Everything needed to control the robot.  """
import yaml
import spidev
import serial
from time import sleep
from struct import pack
from BrickPiM import BrickPi

global BLACK
global WHITE
global GREEN

GREEN = 2
BLACK = 1
WHITE = 0

class Robot(object):
    """ All methods needed to control the robot """
    def __init__(self):
        # Load configuration file
        with open("config.yml", 'r') as ymlfile: # Load Configuration into Dict
                cfg = yaml.load(ymlfile)
        for section in cfg['robot']:
            setattr(self, section, cfg['robot'][section])

        # Init vars for values
        self.light = [0]*8 # Contains sensorbar values
        self.colors = [[0]*4]*2
        self.lightCalibrate = [600]*8 # Contains treshold, modified by Robot.Calibrate

        # Setup
        #-------------------------------
        # Open Serial connection to arduino
        # FIXME: Does this change? - No
        self.serial = serial.Serial("/dev/serial/by-path/platform-3f980000.usb-usb-0:1.4:1.0-port0")
        self.serial.baudrate = 9600

        # BrickPi
        self.brick = BrickPi(unsafe=self.unsafe)


    def sensorbar(self, channel=0):
        """ Update self.colors and return value of one specified sensor (not neccessary)."""
        self.serial.flushInput()
        self.serial.write(b'l')
        sleep(self.hw_timeout) # FIXME: Nonblocking call to read_all()
        data = self.serial.read_all().decode("utf-8").replace("['l'", "").replace("]", "")[1:].split(",")
        for index in range(8):
            if(int(data[index]) > 80):
                self.light[index] = BLACK
            else:
                self.light[index] = WHITE
        return self.light[channel]

    def colorSensors(self):
        self.serial.flushInput()
        self.serial.write(b'c')
        sleep(self.hw_timeout) # FIXME: Nonblock
        self.colors = self.serial.read_all()

    # FIXME: This has to be called when the button is pressed. An interrupt should be used
    #        Alternatively: do not flushInput() everytime
    # XXX: Not tested. But it SHOULD work
    def button(self):
        """ Update currently activated button """
        self.serial.flushInptu()
        self.serial.write(b'b')
        sleep(self.hw_timeout) # FIXME: Nonblocking call to read_all()
        return (self.serial.read_all())

    def motor(self, direct, speed, steps=-1, blocking=True):
        if direct == 'l':
            m = self.motorl
        elif direct == 'r':
            m = self.motorr
        else:
            m = self.motorr
            self.motor('l', speed, steps, blocking=False)

        if speed < 0:
            self.brick.updateDirection(m, 0)
        else:
            self.brick.updateDirection(m, 1)

        self.brick.updateSpeed(m, abs(int(speed)))

        if steps != -1:
            self.brick.moveSteps(m, steps, blocking)


    def close(self):
        self.brick.stop()
