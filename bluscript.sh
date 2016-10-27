#!/bin/bash

# Enable Bluetooth
/usr/sbin/rfkill unblock bluetooth
/usr/bin/hciconfig hci0 up

# Scan for near devices
hcitool scan
sleep 1

# Ask the user for the MAC address of device
echo "Write the MAC addres you want to connect to and press [ENTER]"
read mac_address

# Connect to device using hcitool
hcitool cc $mac_address
echo "Connected to $mac_address"
