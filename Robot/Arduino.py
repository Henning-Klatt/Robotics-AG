import serial
import os

class arduino(object):
    def __init__(self):
        ser = os.listdir("/dev/serial/by-id")
        self.serial = serial.Serial("/dev/serial/by-id/" + ser[0])
        self.serial.baudrate = 250000

    def neopixel(self, led, color):
        """ Update color of led """
        self.serial.write(b'n')
        sleep(self.hw_timeout)
        self.serial.write(pack("!B", led))
        self.serial.write(color)

    def sensorbar(self, channel=0):
        """ Update self.colors and return value of one specified sensor (not neccessary)."""
        self.serial.flushInput()
        self.serial.write(b'l')
        data = ""
        while True:
            char = self.serial.read().decode("ascii")
            data += char
            if char == ']':
                break
        data = ast.literal_eval(data)[1:]
        return data

    def colorSensors(self):
        """ Get raw color values """
        self.serial.flushInput()
        self.serial.write(b'c')
        data = ""
        parens = 0
        while True:
            char = self.serial.read().decode("ascii")
            data += char
            if char == '[':
                parens += 1
            elif char == ']':
                if parens == 0:
                    break
                else:
                    parens -= 1
        data = ast.literal_eval(data)[1:]
        return data

    def gyro(self):
        pass

    def button(self):
        """ Update currently activated button """
        self.ser.flushInput()
        self.ser.write(b'b')
        data = ""
        while True:
            char = self.ser.read().decode("ascii")
            data += char
            if char == ']':
                break
        data = ast.literal_eval(data)[1:]
        return data

    def stop():
        self.serial.stop()
