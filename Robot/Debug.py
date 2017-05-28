from Robot import *
import curses
import time

class Debug:
    def __init__(self):
        self.window = curses.initscr()

        # Setup terminal
        curses.noecho()
        curses.cbreak()

        self.window.clear()
        self.window.refresh()


    def stop(self):
        curses.echo()
        curses.nocbreak()
        curses.endwin()


if __name__ == "__main__":
    deb = Debug()
    x = 0
    while x != ord('b'):
        x = deb.window.getch()
    time.sleep(5)
    deb.stop()
