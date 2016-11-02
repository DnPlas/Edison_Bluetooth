#!/bin/bash

# Enable Bluetooth
/usr/sbin/rfkill unblock bluetooth
/usr/bin/hciconfig hci0 up

# Make Edison discoverable
bluetoothctl <<EOF
discoverable on
quit 
EOF

# Registers bluetooth agent and enables SPP
python /home/root/Edison_Bluetooth/spp.py &

# Print a message so the user knows everything was setup correctly
sleep 1
echo "Now can now pair your device with Edison"
