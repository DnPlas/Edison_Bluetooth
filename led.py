#from spp import Profile
#import mraa

#ledPin = 13   # led pin number for mraa library
#led = mraa.Gpio(ledPin) 
#led.dir(mraa.DIR_OUT)


def funcion (data):
    func = functionInUse.get(data, dummy)
    func()

def relayOff():
    print ('relayOff')

def relayOn():
    print ('relayOn')

def ledOff():
    print ('ledOff')

def ledOn():
    print ('ledOn')

def dummy():
    pass

functionInUse = {'a' : relayOn,
                 'b' : relayOff,
                 'c' : ledOn,
                 'd' : ledOff, }
