# Imports
from  pycreate2 import Create2
import time
import tkinter as gui

root = gui.TK

#Setup
port = "/dev/tty.usbserial-DA01NUGW"   # Where is the Serial Port? 
bot = Create2(port)
bot.start()
bot.full()

#Instructions
bot.drive_direct(-100, -100)
time.sleep(3)
bot.drive_direct(-200, -200)
time.sleep(1.8)
bot.drive_direct(1000, 1000)
time.sleep(2)

bot.drive_stop()
