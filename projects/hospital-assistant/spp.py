#!/usr/bin/python

# Python modules imports
import os
import socket
import dbus
import dbus.service
import dbus.mainloop.glib
from threading import Thread

import pyupm_grove as g

#import hospital_assistant as ha
try:
    from gi.repository import GObject
except ImportError:
    import gobject as GObject


BUS_NAME = 'org.bluez'
AGENT_INTERFACE = 'org.bluez.Agent1'
PROFILE_INTERFACE = 'org.bluez.Profile1'

closing = False

def set_trusted(path):
    """Trusted device function"""
    props = dbus.Interface(bus.get_object("org.bluez", path),
                           "org.freedesktop.DBus.Properties")
    props.Set("org.bluez.Device1", "Trusted", True)


def processSockets(fd):
    data = ""
    server_sock = socket.fromfd(fd,
                                socket.AF_UNIX,
                                socket.SOCK_STREAM)
    server_sock.settimeout(1)
    server_sock.send("Hello, this is Edison!")
    try:
        while not closing:
            try:
                data = server_sock.recv(1024)
                print ("Here's data %s" % data)
                result = ha.callFunction(data)
                if result:
                    server_sock.send(result)
            except socket.timeout:
                pass
    except IOError:
        pass
    server_sock.close()


# Agent class
class Agent(dbus.service.Object):
    @dbus.service.method(AGENT_INTERFACE, in_signature="ou", out_signature="")
    def RequestConfirmation(self, device, passkey):
        print("\nEnsure this passkey matches with the one in your device: "
              "%06d\nPress [ENTER] to continue" % passkey)
        set_trusted(device)
        return


# Profile class
class Profile(dbus.service.Object):
    fd = -1

    @dbus.service.method(PROFILE_INTERFACE,
                         in_signature="oha{sv}",
                         out_signature="")
    def NewConnection(self, path, fd, properties):
        self.fd = fd.take()
        global closing

        device_path = os.path.basename(path)
        print("\nConnected to %s\nPress [ENTER] to continue" % device_path)
        socket_thread = Thread(target=processSockets, args=(self.fd,))
        socket_thread.start()
        try:
            while not closing:
                ha.myProgram()
        except IOError:
            pass
        closing = True

        print("\nYour device is now disconnected\nPress [ENTER] to continue")


def closeThreads():
    global closing
    closing = True

def bluetoothConnection():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    obj = bus.get_object(BUS_NAME, "/org/bluez")
    profile_manager = dbus.Interface(obj, "org.bluez.ProfileManager1")
    profile_path = "/foo/bar/profile"
    auto_connect = {"AutoConnect": False}
    profile_uuid = "1101"
    profile = Profile(bus, profile_path)
    profile_manager.RegisterProfile(profile_path, profile_uuid, auto_connect)
    mainloop = GObject.MainLoop()
    try:
        mainloop.run()
    except (KeyboardInterrupt, SystemExit):
        closeThreads()

if __name__ == '__main__':
    # Generic dbus config
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    obj = bus.get_object(BUS_NAME, "/org/bluez")

    # Agent config
    agent_capability = "KeyboardDisplay"
    agent_path = "/test/agent"
    agent = Agent(bus, agent_path)
    agent_manager = dbus.Interface(obj, "org.bluez.AgentManager1")
    agent_manager.RegisterAgent(agent_path, agent_capability)
    agent_manager.RequestDefaultAgent(agent_path)

    # Mainloop
    mainloop = GObject.MainLoop()
    mainloop.run()
