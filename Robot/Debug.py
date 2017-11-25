#!/usr/bin/python3
from Robot import *
import curses
import threading
import sys, os
import led

class Debug(object):
    def __init__(self):
        # Setup ncurses
        led.set("running")
        self.screen = curses.initscr()
        curses.noecho()
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_CYAN)
        self.highlightText = curses.color_pair( 1 )
        self.normalText = curses.A_NORMAL
        self.screen.border(0)

        # Create windows
        self.sensorBox = curses.newwin(7, 40, 3, 4)
        self.sensorBox.box()
        self.keystateBox = curses.newwin(7, 20, 3, 45)
        self.keystateBox.box()
        self.keystateBox.addstr(3, 2, "---")
        self.valueBox = curses.newwin(20, 40, 10, 4)
        self.valueBox.box()
        self.valueBox.addstr(2, 2, "BaseSpeed:")
        self.valueBox.addstr(3, 2, "Motor 1  :")
        self.valueBox.addstr(4, 2, "Motor 2  :")
        self.logBox = curses.newwin(20, 40, 10, 45)
        self.logBox.box()

        # Print it
        self.screen.addstr(0, 3, "Team Robotastisch\n\n")
        self.screen.refresh()
        self.keystateBox.refresh()
        self.valueBox.refresh()
        self.logBox.refresh()

    def showValues(self, rob):
        rob.sensorbar()
        y = 5
        for color in reversed(rob.colors):
            if color == 1:
                self.sensorBox.addstr(3, y, str(color), curses.color_pair(1))
            else:
                self.sensorBox.addstr(3, y, str(color))
            y = y+4
        self.valueBox.addstr(2, 20, str(rob.baseSpeed))
        self.sensorBox.refresh()
        self.valueBox.refresh()

        # Add headlines
        self.screen.addstr(10, 22, "Werte")
        self.screen.addstr(3, 20, "Sensorbar")
        self.screen.refresh()

    def clear(self):
        curses.nocbreak()
        curses.endwin()

    def log(self, toLog):
        self.logBox.addstr(3, 3, str(toLog))
