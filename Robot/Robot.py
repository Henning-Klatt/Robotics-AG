#!/usr/bin/python3
""" Everything needed to control the robot.  """
from threading import Thread
import spidev
import os
from BrickPi import *

class Robot(object):
    """ All methods needed to control the robot """
    def __init__(self, baseSpeed, motorl, motorr, sample):
        # Configuration
        self.baseSpeed = baseSpeed
        self.motorr = motorr
        self.motorl = motorl
        self.sample = sample # Delay used by motorRotateDegree
        self.speedl = 0
        self.speedr = 0
        self.colors = [0]*8 # Contains color Values
        self.colorsCalibrate = [0]*8 # Contains treshold

        # Setup
        #-------------------------------
        # Open SPI bus
        spi = spidev.SpiDev()
        spi.open(0, 0)

        BrickPiSetup()
        BrickPi.MotorEnable[self.motorr] = 1
        BrickPi.MotorEnable[self.motorl] = 1
        BrickPiUpdateValues()

        # Thread start
        self.motorThread = Thread(target=self._thread, args=())
        self.motorThread.setDaemon(1)
        self.motorThread.start()


    def ReadChannel(self):
        """ Function to read SPI data from MCP3008 chip """
        data = [0]*8
        for i in range(8):
            adc = spi.xfer2([1, (8+i)<<4, 0])
            data[i] = ((adc[1]&3) << 8) + adc[2]
        return data


    def motor(self, motor, speed):
        """ Set speed of a motor ('l' or 'r') while driving """
        if motor == 'l':
            self.speedl = speed
        elif motor == 'r':
            self.speedr = speed


    def motorRotateDegree(self, power,deg,port,sample,delay):
        """ Frontend to Brick.MotorRotateDegree 
        TODO: Look into threadsafe version of the library and maybe rewrite mRD() to use it"""
        self.speedl = -1
        self.speedr = -1
        motorRotateDegree(power, deg, [self.motorl, self.motorr], self.sample, .01)

    def _thread(self):
        """ Makes motors run for longer timespans.
        TODO: Research Threading class (and use it instead of this) """
        while True:
            if self.speedl != -1:
                BrickPi.MotorSpeed[self.motorl] = self.speedl
            if self.speedr != -1:
                BrickPi.MotorSpeed[self.motorr] = self.speedr

                BrickPiUpdateValues()
