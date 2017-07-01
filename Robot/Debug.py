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

    def clear(self):
        self.window.clear()
        self.window.refresh()

    def stop(self):
        curses.echo()
        curses.nocbreak()
        curses.endwin()


if __name__ == "__main__":
    deb = Debug()
    rob = Robot()
    x = 0
    while x != ord('q'):
        x = deb.window.getch()
        rob.sensorbar()
        data = rob.colors
        deb.window.move(0, 0)
        deb.addstr(str(data))
    time.sleep(5)
    deb.stop()
