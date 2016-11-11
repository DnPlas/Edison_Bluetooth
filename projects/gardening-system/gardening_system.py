#!/usr/bin/python

# ========== * IMPORT SECTION * ========== #

# UPM Modules
import pyupm_i2clcd as lcd
import pyupm_grove as g

# BT Needed Modules
import spp as s
from optparse import OptionParser, make_option
import os, sys, socket, uuid, dbus, dbus.service
import dbus.mainloop.glib, gardening_system
try:
      from gi.repository import GObject
except ImportError:
    import gobject as GObject
from time import sleep

# =========== * BT CONSTANTS * =========== #
BUS_NAME = 'org.bluez'
AGENT_INTERFACE = 'org.bluez.Agent1'
PROFILE_INTERFACE = 'org.bluez.Profile1'

# ========= * SETTING UP GPIOS * ========= #
light = g.GroveLight(0)                 # Light sensor is connected to slot A0
display = lcd.Jhd1313m1(0, 0x3E, 0x62)  # LCD goes on any I2C slot
relay = g.GroveRelay(4)                 # Relay module is connected to slot D4

# ========= * PROJECT FUNCTIONS * ======== #

# ------------ LCD Functions ------------- #

# Display light sensor data
def displayLightInfo():
    display.clear()                 # Clear LCD
    display.setCursor(0,0)          # Set LCD cursor position (top left corner)
    display.write('Light:%s' % str(light.value()))  # Display light sensor data
    sleep(1)

# Display message on LCD
def displayStatus(message):    
    display.clear()            # Clear LCD
    display.setColor(0,0,255)  # Set LCD backlight color to blue
    display.setCursor(0,2)     # Set cursor position (bottom left corner)
    display.write(message)     # Display message

# Change LCD backlight color based on light threshold
def displayLight():
    if light.value() <= 20:             # Set a low light threshold
        display.setColor(255,0,0)       # If low light, set LCD color to RED
    elif light.value() in range(21,29): # Set medium amount of light threshold
        display.setColor(255,255,0)     # If mid light, set LCD color to YELLOW
    elif light.value() >= 30:           # Set a high amount of light threshold
        display.setColor(0,255,0)       # If high light, set LCD color to GREEN

#-------------  BT Functions -------------  #
    
# Water your plant via BT
def waterPlant():              
    displayStatus('Watering')     # Display message when plant is being watered
    relay.off()                   # Turns relay off
    sleep(1)                      
    relay.on()                    # Turns relay on for five seconds
    sleep(5)
    relay.off()                   # Tunrs relay off again

# Request light sensor data via BT
def requestData():
    return str(light.value())     # Returns light sensor data

#-----------  BT Communication ------------ #

# BT dependent case function
def function (data):
    func = functionInUse.get(data) # Selects the function to be used
    func()                         # depending on BT commands

functionInUse = {'a' : waterPlant,    # Sets which letter corresponds
                 'b' : requestData, } # to each BT controlled function

# ------------ Project Program ------------ #
# Run all non-BT controlled functions
def myProgram():
      displayLight()     # Run these functions until a BT event is triggered
      displayLightInfo()

# =========== * BT MAIN LOOP * ============ #

if __name__ == '__main__':
  
    # dbus config
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    obj = bus.get_object(BUS_NAME, "/org/bluez");
    
    # Profile config
    profile_manager = dbus.Interface(obj, "org.bluez.ProfileManager1")
    profile_path = "/foo/bar/profile"
    auto_connect = {"AutoConnect": False}
    profile_uuid = "1101"
    profile = s.Profile(bus, profile_path)
    profile_manager.RegisterProfile(profile_path, profile_uuid, auto_connect)
    
    # Mainloop
    mainloop = GObject.MainLoop()
    mainloop.run()
