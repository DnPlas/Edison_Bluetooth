#!/bin/bash

# Enable Bluetooth
/usr/sbin/rfkill unblock bluetooth

# Registers bluetooth agent and enables SPP
python /home/root/Edison_Bluetooth/spp.py &

sleep 1

# Print a message so the user knows everything was setup correctly
echo "Now can now pair your device with Edison"
