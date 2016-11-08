# Edison Bluetooth 
This repository contains a workaround for connecting the Intel Edison board to a device capable of communicating through Serial Port Profile (SPP).
## Quickstart
NOTE: Your board should be connected to a Wi-fi network, if you haven't set this up, pleas refer to the [Getting started guide] (https://software.intel.com/en-us/get-started-edison-windows)

1. Clone Edison_Bluetooth
```root@edison # git clone https://github.com/DnPlas/Edison_Bluetooth.git```

2. Select the project you'll be working with
* Temperature monitor
* Gardening system
* Hospital assistant
```root@edison # cd Edison_Bluetooth```
Open ```bluscript.sh``` with your preferred text editor and replace "your-project" with the name of the project you'll be working with. 
Default is set as "gardening-system". Options are:
- gardening-system
- temperature-monitor
- hospital-assistant
```root@edison # nano bluscript.sh```

3.Run the BT setup script
```root@edison # ./bluscript.sh```

4.Pair your device with Edison
5.Using BluSPP (Android) or Bluetooth Sertial Terminal (Windows), connect to your device

