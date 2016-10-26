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
		print("\nConected to (%s, %d)" % (path, self.fd))


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

	option_list = [
			make_option("-C", "--channel", action="store",
					type="int", dest="channel",
					default=None),
			]

	parser = OptionParser(option_list=option_list)

	(options, args) = parser.parse_args()

#	options.uuid = "1101"
#	options.psm = "3"
#	options.role = "server"
#	options.name = "Edison SPP Loopback"
#	options.service = "spp char loopback"
	options.path = "/foo/bar/profile"
	options.auto_connect = False
#	options.record = ""

	profile = Profile(bus, options.path)

	mainloop = GObject.MainLoop()

	opts = {
			"AutoConnect" :	options.auto_connect,
		}

#	if (options.name):
#		opts["Name"] = options.name
#
#	if (options.role):
#		opts["Role"] = options.role
#
#	if (options.psm is not None):
#		opts["PSM"] = dbus.UInt16(options.psm)
#
#	if (options.channel is not None):
#		opts["Channel"] = dbus.UInt16(options.channel)
#
#	if (options.record):
#		opts["ServiceRecord"] = options.record
#
#	if (options.service):
#		opts["Service"] = options.service
#
#	if not options.uuid:
#		options.uuid = str(uuid.uuid4())

	manager.RegisterProfile(options.path, "1101", opts)

	mainloop.run()
