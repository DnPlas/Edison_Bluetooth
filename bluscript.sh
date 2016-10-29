#!/bin/bash

# Enable Bluetooth
/usr/sbin/rfkill unblock bluetooth
/usr/bin/hciconfig hci0 up

## Enable default-agent
bluetoothctl << EOF
power on
discoverable on
pairable on
quit
EOF
sleep 1

# Enable simple agent
python /home/root/edison_b/simple-agent1 &
sleep 1

# Enable SPP
python /home/root/edison_b/spp.py &
## Ask the user for the MAC address of device
#echo "Write the MAC addres you want to connect to and press [ENTER]"
#read mac_address
#
## Connect to device using hcitool
##hcitool cc $mac_address
#
#bluetoothctl --agent=NoInputNoOutput << EOF
#trust $mac_address
#quit
#EOF
#
#bluetoothctl --agent=NoInputNoOutput << EOF
#pair $mac_address
#connect $mac_address
#info $mac_address
#quit
#EOF
