RaspberryPi Device Control Library
==================================

This is a Python 3 library for easily setting up devices connected to a
Raspberry Pi. It contains objects and methods for DC motors with and
without software PWM, servos and LEDs.

Currently, following objects are available: 

* ``SimpleMotor``: DC Motor with bi-directional rotation (no PWM control)
* ``DCMotor``: DC Motor with bi-directional rotation and PWM control
  methods
* ``Servo``: Servo with PWM control and configuration methods
* ``LED``: LED, Laser Diode or any other device which can be controlled 
  using a single GPIO output pin

Installation and Usage
----------------------

Option 1 (Recommended) :
^^^^^^^^^^^^^^^^^^^^^^^^

1. Using ``pip``: ::

     sudo pip install rpi_devices

   or using ``setuptools``: ::

     git clone https://github.com/munircontractor/raspberry-pi-device-library
     cd raspberry-pi-device-library
     sudo python3 setup.py install

2. Then, in your code: ::

     from rpi_devices import cleanup, <Device>

Option 2 :
^^^^^^^^^^

Using directly:

1. Copy the ``rpi_devices/devices.py`` files to your Raspberry Pi.
2. To use the objects, add the following lines at the top of your code: ::

     import sys
     sys.path.append("/full/path/to/devices.py")
     from devices import cleanup, <Device>-

Cautions
--------

1. Do not forget to run the library’s ``cleanup`` function or 
   ``RPi.GPIO.cleanup()`` after you are done.
2. Although all the classes in this library allow a different pin numbering
   mode during setup, it is strongly recommended to use the same mode
   across all devices. The pin numbering mode is set globally, so if
   devices are set with different pin numbering modes, code which is not
   calling a device method will automatically use the mode of the last
   device called, which can lead to undesirable and, at times, harmful behavior.

