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
light = g.GroveLight(0)
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
relay = g.GroveRelay(4)

# ========= * PROJECT FUNCTIONS * ======== #

# ------------ LCD Functions ------------- #

# Display light sensor data
def displayLightInfo():
    display.clear()
    display.setCursor(0,0)
    display.write('Light:%s' % str(light.value()))
    sleep(1)

# Display message on LCD
def displayStatus(message):
    display.clear()
    display.setColor(0,0,255)
    display.setCursor(0,2)
    display.write(message)

# Change LCD backlight color based on light threshold
def displayLight():
    if light.value() <= 20:
        display.setColor(255,0,0)
    elif light.value() in range(21,29):
        display.setColor(255,255,0)
    elif light.value() >= 30:
        display.setColor(0,255,0)

#-------------  BT Functions -------------  #
    
# Water your plant via BT
def waterPlant():
    displayStatus('Watering')
    relay.off()
    sleep(1)
    relay.on()
    sleep(5)
    relay.off()

# Request light sensor data via BT
def requestData():
    return str(light.value())

#-----------  BT Communication ------------ #

# BT dependent case function
def function (data):
    func = functionInUse.get(data)
    func()

functionInUse = {'a' : waterPlant,
                 'b' : requestData, }

# ------------ Project Program ------------ #
# Run all non=BT dependent functions
def myProgram():
      displayLight()
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
