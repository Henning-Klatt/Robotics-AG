import os
import ast
import serial
from time import sleep
import threading
import Main
import Arduino

class watcher(object):
    def __init__(self):
        self.mainThread = []
        self.arduino = Arduino.arduino()

    def stopNetwork(self):
        os.system("systemctl stop networking")

    def startNetwork(self):
        os.system("systemctl start networking")
        os.system("systemctl start hostapd")

    def main(self):
        self.main = Main.main()

    def runMain(self):
        self.main = threading.Thread(target=Main.main)
        self.main.join()

if __name__ == "__main__":
    w = watcher()
    while True:
        b = w.arduino.button()
        print(b)
        sleep(0.5)
