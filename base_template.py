from  pycreate2 import Create2
import time

# Setup
port = "/dev/tty.usbserial-DA01NUGW"   # Where is the Serial Port? 
bot = Create2(port)
bot.start()

# Launches the bot in safe mode
# RECOMMENDED MODE!
bot.safe()

# ONLY run in sudo mode if you know what you're doing
# bot.full()

# Moves the robot forwards
bot.drive_direct(100, 100)
time.sleep(2)

# Turns the robot (In place)
bot.drive_direct(200,-200)  # +/- 500 max
time.sleep(2)

# Stop the bot
bot.drive_stop()

# Query some sensors
#sensors = bot.get_sensors()  # returns all data
#print(sensors.light_bumper_left)

# Close the connection
#bot.close()
