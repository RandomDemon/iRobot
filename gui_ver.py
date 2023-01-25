# Imports
from pycreate2 import Create2
import time
import tkinter as gui

root = gui.Tk()

port = "/dev/tty.usbserial-DA01NUGW"   # Where is the Serial Port? 
bot = Create2(port)
bot.start()
bot.full()

root.title("iCreate2 Control Panel")

# Create functions
def move_forward():
    bot.drive_direct(500, 500)
def turn_around():
    bot.drive_direct(-400, 400)
    time.sleep(1)
    bot.drive_stop()

def stop():
    bot.drive_stop()
def undock():
    bot.drive_direct(-100, -100)
    time.sleep(3)
    bot.drive_direct(-400, 400)
    time.sleep(1)
    bot.drive_stop()

# Create a button to move the iCreate2 forward
forward_button = gui.Button(root, text="Move Forward", command=move_forward)
undock_button = gui.Button(root, text="Undock", command=undock)
stop_button = gui.Button(root, text="Stop", command=stop)

#Pack the buttons
forward_button.pack()
undock_button.pack()
stop_button.pack()

# Start the Tkinter event loop
root.mainloop()
