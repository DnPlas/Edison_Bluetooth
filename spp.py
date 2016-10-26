#!/usr/bin/python

from optparse import OptionParser, make_option
import os, sys, socket, uuid, dbus, dbus.service, dbus.mainloop.glib
try:
  from gi.repository import GObject
except ImportError:
  import gobject as GObject

class Profile(dbus.service.Object):
	fd = -1

	@dbus.service.method("org.bluez.Profile1",
				in_signature="oha{sv}", out_signature="")
	def NewConnection(self, path, fd, properties):
		self.fd = fd.take()
		print("\nConnected to (%s, %d)" % (path, self.fd))

		server_sock = socket.fromfd(self.fd, socket.AF_UNIX, socket.SOCK_STREAM)
		server_sock.setblocking(1)
		server_sock.send("Hello, this is Edison!")
		try:
		    while True:
		        data = server_sock.recv(1024)
		        print("received: %s" % data)
			server_sock.send("looping back: %s\n" % data)
		except IOError:
		    pass

		server_sock.close()
		print("Disconnected")

if __name__ == '__main__':

        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
	bus = dbus.SystemBus()
	manager = dbus.Interface(bus.get_object("org.bluez",
				"/org/bluez"), "org.bluez.ProfileManager1")
        path = "/foo/bar/profile"
        auto_connect = {"AutoConnect": False}
        uuid = "1101"
	profile = Profile(bus, path)
	mainloop = GObject.MainLoop()
	manager.RegisterProfile(path, uuid, auto_connect)
	mainloop.run()
