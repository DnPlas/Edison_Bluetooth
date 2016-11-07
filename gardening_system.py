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
    func = functionInUse.get(data)
    func()

def requestData():
    return str(light.value())

def waterPlant():
    relay.off()
    watering = 1
    sleep(1)
    relay.on()
    sleep(60)
    relay.off()
    watering = 0
    already_watered = 1

def displayLightInfo():
    display.setCursor(0,0)
    display.write('Light:%s' % str(light.value()))
    sleep(1)

def displayWateringInfo(watering, already_watered):
    display.setCursor(1,0)
    if watering:
        display.write('Watering')
    else:
        if already_watered == 0:
            display.write('Watered:NO')
        elif already_watered:
            display.write('Watered:YES')


if __name__ == '__main__':
    
    functionInUse = {'a' : waterPlant,
                     'b' : requestData}
    while True:
        displayLight()
        displayLightInfo()
        displayWateringInfo(watering, already_watered)
