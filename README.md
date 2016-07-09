# raspberry-pi-device-library

This is a Python 3 library for easily setting up devices connected to a Raspberry Pi.
It contains objects and methods for DC motors with and without software PWM, servos and LEDs.

Currently, following objects are available:
* `SimpleMotor`: DC Motor with bi-directional rotation (no PWM control)
* `DCMotor`: DC Motor with bi-directional rotation and PWM control methods
* `Servo`: Servo with PWM control and configuration methods
* `LED`: LED, Laser Diode or any other device which can be controlled using a single GPIO output pin

## Installation

1. Copy the `.py` files to your Raspberry Pi
2. To use the objects, add the following lines at the top of your code:  
<pre>
import sys
sys.path.append("\</full/path/to/devices.py\>")
from devices import \<Device\>
</pre>
3. Use and enjoy
4. Do not forget to run the library's `cleanup` function or `RPi.GPIO.cleanup()` after you are done

## Cautions

Although all the classes in this library allow a different pin numbering mode during setup, it is strongly recommended to use the same mode across all devices. The pin numbering mode is set globally, so if devices are set with different pin numbering modes, code which is not calling a device method will automatically use the mode of the last device called, which can lead to undesirable and, at times, harmful to the Pi behavior.
