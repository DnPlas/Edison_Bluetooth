# Edison Bluetooth 
This repository contains base code for creating IoT projects using an Intel Edison board + Arduino Expansion board and a Grove Starter Kit. You will find all what is needed for connecting Edison to a device via Bluetooth and sample projects that use the Grove Kit sensors and actuators.

Before starting, you should consider having:

* Intel Edison board running the [Latest Yocto-Poky image] (https://software.intel.com/edison-image/latest)
* Android or Windows device with [SPP] (https://learn.sparkfun.com/tutorials/bluetooth-basics/bluetooth-profiles) capabilities
* [BlueSPP](https://play.google.com/store/apps/details?id=com.shenyaocn.android.BlueSPP&hl=en) (Android) or [Bluetooth Serial Terminal](https://www.microsoft.com/en-us/store/p/bluetooth-serial-terminal/9wzdncrdfst8) (Windows) already installed in your device
* [Grove Starter Kit] (https://www.seeedstudio.com/Grove-starter-kit-plus---Intel-IoT-Edition-for-Intel-Galileo-Gen-2-and-Edison-p-1978.html#)

## Quickstart
NOTE: Your board should be connected to a Wi-fi network, if you haven't set this up, please refer to the [Getting started guide] (https://software.intel.com/en-us/get-started-edison-windows)

1.Clone Edison_Bluetooth
```c
root@edison # git clone https://github.com/DnPlas/Edison_Bluetooth.git
```

2.Select the project you'll be working with and edit the BT setup script

Open ```bluscript.sh``` with your preferred text editor and edit line 24 so that it points to the project you'll be working with (default is set as "gardening-system").

That is:

```c
root@edison # cd Edison_Bluetooth
root@edison # nano bluscript.sh
# Once the file is opened, replace 'your-project' with one of the options listed below.
...
python /home/root/Edison_Bluetooth/projects/your-project/spp.py &
...
````

Save all changes and exit.

Options are:
* temperature-monitor
* gardening-system
* hospital-assistant

3.Run the BT setup script.

```c
root@edison # ./bluscript.sh
Wait for the Bluetooth setup to finish
...
Now can now pair your device with Edison
```

4.Pair your device with Edison. Generally, all you have to do is enter your device's Bluetooth settings and select 'edison' or 'Pair to edison'. Note that this step will change depending on your device.

5.Using BluSPP (Android) or Bluetooth Sertial Terminal (Windows), connect to your Edison and start communicating.

## Projects
TODO
### Temperature monitor
### Gardening system
### Hospital asssitant
