#!/usr/bin/python3
""" Everything needed to control the robot.  """
import yaml
import spidev
import serial
import os
from time import sleep
from struct import pack
from BrickPiM import BrickPi
import Arduino
import ast

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
        self.colors = [0]*2
        self.lightCalibrate = [150]*8 # Contains treshold, modified by Robot.Calibrate

        # Setup
        #-------------------------------
        # Arduino
        self.arduino = Arduino.arduino()

        # BrickPi
        self.brick = BrickPi(unsafe=self.unsafe)
        sleep(5)

    def sensorbar(self, channel=0):
        """ Transform raw values to BLACK/WHITE """
        data = self.arduino.sensorbar(channel)
        for index in range(8):
            if(int(data[index]) > 80):
                self.light[index] = BLACK
            else:
                self.light[index] = WHITE
        return self.light[channel]

    def colorSensors(self):
        """ Transfomr raw values to BLACK/WHITE/GREEN """
        data = self.arduino.colorSensors()

    def motor(self, direct, speed, steps=-1, blocking=True):
        """ Control both motors at the same time """
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
        """ Stop all open connections """
        self.brick.stop()
        self.arduino.close()
