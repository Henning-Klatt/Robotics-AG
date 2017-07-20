#!/usr/bin/python3
from Robot import *
from time import sleep
import curses
import threading
import sys, os
import led

class Debug(object):

    def __init__(self):
        led.set("running")
        self.running = True
        self.rob = Robot()
        self.screen = curses.initscr()
        curses.noecho()
        curses.curs_set(0)
        self.screen.keypad(1)
        curses.start_color()
        curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_CYAN)
        self.highlightText = curses.color_pair( 1 )
        self.normalText = curses.A_NORMAL
        self.screen.border(0)
        self.box = curses.newwin(7, 40, 3, 4)
        self.box.box()
        self.box2 = curses.newwin(7, 20, 3, 45)
        self.box2.box()
        self.box2.addstr(3, 2, "---")
        self.box3 = curses.newwin(20, 40, 10, 4)
        self.box3.box()
        self.box3.addstr(2, 2, "BaseSpeed:")
        self.box3.addstr(3, 2, "Motor 1  :")
        self.box3.addstr(4, 2, "Motor 2  :")
        self.box4 = curses.newwin(20, 40, 10, 45)
        self.box4.box()
        self.screen.addstr(0, 3, "Team Robotastisch\n\n")
        self.screen.refresh()
        self.box2.refresh()
        self.box3.refresh()
        self.box4.refresh()

        updater = threading.Thread(target=self.showValues, args=(self.rob, self.running, self.box, self.screen, self.box3))
        updater.daemon = True
        updater.start()
        listener = threading.Thread(target=self.KeyListener, args=(self.running, self.screen,self.box2, self.rob))
        listener.ddaemon = True
        listener.start()

    def showValues(self, rob, running, box, screen, box3):
        try:
            while self.running:
                self.rob.sensorbar()
                y = 5
                for color in reversed(self.rob.colors):
                    if color == 1:
                        self.box.addstr(3, y, str(color), curses.color_pair(1))
                    else:
                        self.box.addstr(3, y, str(color))
                    y = y+4
                self.box3.addstr(2, 20, str(self.rob.baseSpeed))
                self.box.refresh()
                self.box3.refresh()
                self.screen.addstr(10, 22, "Werte")
                self.screen.addstr(3, 20, "Sensorbar")
                self.screen.refresh()
                sleep(rob.sample)
        except KeyboardInterrupt:
            print("Drücke Q um zu verlassen")

    def KeyListener(self, running, screen, box2, rob):
        try:
            last = ""
            while self.running:
                self.screen.addstr(3, 52, "Aktion")
                self.screen.refresh()
                event = screen.getch()
                if event == ord("q"):
                    led.set("off")
                    sleep(.6)
                    curses.endwin()
                    self.running = False
                    self.rob.motor('lr', 0)
                    print("To stop, press STR+C")
                    #os._exit(1)
                    exit()
                    break
                if event == ord("w"):
                    self.box2.addstr(3, 2, "      ")
                    self.box2.addstr(3, 2, "Vor")
                    self.rob.motor('l', rob.baseSpeed)
                    self.rob.motor('r', rob.baseSpeed)
                    #self.log("w")
                if event == ord("s"):
                    self.box2.addstr(3, 2, "      ")
                    self.box2.addstr(3, 2, "Zurück")
                    self.rob.motor('lr', -rob.baseSpeed)
                if event == ord("a"):
                    self.box2.addstr(3, 2, "      ")
                    self.box2.addstr(3, 2, "Links")
                    self.rob.motor('l', 0)
                    self.rob.motor('r', rob.baseSpeed)
                if event == ord("d"):
                    self.box2.addstr(3, 2, "      ")
                    self.box2.addstr(3, 2, "Rechts")
                    self.rob.motor('l', rob.baseSpeed)
                    self.rob.motor('r', 0)
                if event == ord(" "):
                    self.box2.addstr(3, 2, "      ")
                    self.box2.addstr(3, 2, "Stop")
                    self.rob.motor('l', 0)
                    self.rob.motor('r', 0)
                self.box2.refresh()
        except KeyboardInterrupt:
            print("Drücke Q um zu verlassen")

    def clear(self):
        curses.endwin()
        sys.exit(0)

    def log(self, toLog):
        self.box4.addstr(1, 1, str(toLog))
