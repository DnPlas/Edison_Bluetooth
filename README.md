# Edison Bluetooth 
This repository contains base code for creating IoT projects using an Intel Edison board + Arduino Expansion board and a Grove Starter Kit. You will find all what is needed for connecting the Intel Edison board to a device capable of communicating through Serial Port Profile (SPP) and sample projects that use the Grove Kit sensors/actuators.

## Quickstart
NOTE: Your board should be connected to a Wi-fi network, if you haven't set this up, pleas refer to the [Getting started guide] (https://software.intel.com/en-us/get-started-edison-windows)

1. Clone Edison_Bluetooth
```root@edison # git clone https://github.com/DnPlas/Edison_Bluetooth.git```

2. Select the project you'll be working with and edit the BT setup script

Open ```bluscript.sh``` with your preferred text editor and replace "your-project" with the name of the project you'll be working with (default is set as "gardening-system").

Options are:

* Temperature monitor (temperature-monitor)
* Gardening system (gardening-system)
* Hospital assistant (hospital-assistant)

```root@edison # cd Edison_Bluetooth```
```root@edison # nano bluscript.sh```

3.Run the BT setup script
```root@edison # ./bluscript.sh```

4.Pair your device with Edison. Generally, all you have to do is enter your device's Bluetooth settings and select 'edison' or 'Pair to edison'. Note that this step will change depending on your device.

5.Using BluSPP (Android) or Bluetooth Sertial Terminal (Windows), connect to your Edison and start communicating.

