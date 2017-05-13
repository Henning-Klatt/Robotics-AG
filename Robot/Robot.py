#/usr/bin/python
import spidev
import os
from Brick import *
from threading import Thread

class Robot(object):
	def __init__(self, speed, motorl, motorr, sample):
		# Configuration
		self.baseSpeed = speed
		self.motorr = motorr
		self.motorl = motorl
		self.sample = sample # Delay used by motorRotateDegree
		self.speedl = 0
		self.speedr = 0

		# Setup
		#-------------------------------
		# Open SPI bus
		spi = spidev.SpiDev()
		spi.open(0,0)

		BrickPiSetup()
		BrickPi.MotorEnable[self.motorr] = 1
		BrickPi.MotorEnable[self.motorl] = 1
		BrickPiUpdateValues()

		# Thread start
		self.motorThread = Thread(target=self.motor_thread, args=())
		self.motorThread.setDaemon(1)
		self.motorThread.start()

		
	def ReadChannel(self):
		""" Function to read SPI data from MCP3008 chip """
		data = []
		for i in range(7):
			adc = spi.xfer2([1,(8+i)<<4,0])
			data[i] = ((adc[1]&3) << 8) + adc[2]
		return data


	def motor(self, motor, speed):
		""" Set speed of a motor ('l' or 'r') while driving """
		if (motor == 'l'):
			self.speedl = speed
		elif (motor == 'r'):
			self.speedr = speed


	def motor_thread(self):
		while True:
			BrickPi.MotorSpeed[self.motorl] = self.speedl
			BrickPi.MotorSpeed[self.motorr] = self.speedr
			BrickPiUpdateValues()
