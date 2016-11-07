#!/usr/bin/python

import pyupm_grove as g
import pyupm_i2clcd as lcd
from time import sleep

light = g.GroveLight(0)
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
relay = g.GroveRelay(4)
watering = 0
already_watered = 0

def displayLight():
    if light.value() <= 20:
        display.setColor(255,0,0)
    elif light.value() in range(21,29):
        display.setColor(255,255,0)
    elif light.value() >= 30:
        display.setColor(0,255,0)

def function (data):
    func = functionInUse.get(data, dummy)
    func()

def dummy():
    pass

def requestData():
    return str(light.value())

def displayStatus(message):
    display.clear()
    display.setColor(0,0,255)
    display.setCursor(0,2)
    display.write(message)

def waterPlant():
    displayStatus('Watering')
    relay.off()
    sleep(1)
    relay.on()
    sleep(5)
    relay.off()

def displayLightInfo():
    display.clear()
    display.setCursor(0,0)
    display.write('Light:%s' % str(light.value()))
    sleep(1)

def myProgram(): 
     displayLight()
     displayLightInfo()

functionInUse = {'a' : waterPlant,
                 'b' : requestData, }
