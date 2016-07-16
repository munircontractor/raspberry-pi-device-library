  ------------------------------------ ------------------------------------
   \
    \
  **devices**
  [index](.)\
  [/home/pi/github-repo/raspberry-pi-d
  evice-library/rpi\_devices/devices.p
  y](file:/home/pi/github-repo/raspber
  ry-pi-device-library/rpi_devices/dev
  ices.py)
  ------------------------------------ ------------------------------------

 \
 **Modules**

`      `

 

  ----------------------------
  [RPi.GPIO](RPi.GPIO.html)\
  ----------------------------

 \
 **Classes**

`      `

 

[\_\_builtin\_\_.object](__builtin__.html#object)

[DCMotor](devices.html#DCMotor)

[LED](devices.html#LED)

[Servo](devices.html#Servo)

[SimpleMotor](devices.html#SimpleMotor)

 \
 class **DCMotor**([\_\_builtin\_\_.object](__builtin__.html#object))

`   `

`DC Motor which is connected to a controller (L293D or similar)   Use this class for a DC motor whose rotation speed needs to be controlled. Typically, the Pi's GPIO will be connected to the pins of a L293D or similar controller, and the controller is connected to the motor. `

 

Methods defined here:\

**\_\_init\_\_**(self, a, b, en, mode=10)
:   `Construct a new 'DCMotor' object.   Args:     a: GPIO pin number connected to A pin of the motor controller     b: GPIO pin number connected to B pin of the motor controller     en: GPIO pin number connected to the EN pin of the motor controller     mode: GPIO pin numbering mode, RPi.GPIO.BCM or RPi.GPIO.BOARD (default)   Raises:     ValueError: If mode is not RPi.GPIO.BCM or RPi.GPIO.BOARD`

**backward**(self, dc)
:   `Rotates the motor in an arbitrary direction.   The directions depend on the circuit connections and so cannot be guaranteed. Only guarantee is that forward and backward methods will always rotate in opposite directions.`

**change\_speed**(self, dc)
:   `Changes the speed of rotation of motor.   Manipulates the duty cycle of the internal software PWM to change the rotation speed. Higher the duty cycle, faster the speed of rotation.   Args:     dc: Duty cycle to change to   Raises:     ValueError: 0 <= dc <= 100 is not True`

**forward**(self, dc)
:   `Rotates the motor in an arbitrary direction.   The directions depend on the circuit connections and so cannot be guaranteed. Only guarantee is that forward and backward methods will always rotate in opposite directions.`

**get\_settings**(self)
:   `Returns a dictionary of GPIO pins being used and the mode of setup   Dictionary contains the following keys:     MODE: Mode being used by the object as string     A: GPIO pin connected to pin A of the motor controller     B: GPIO pin connected to pin B of the motor controller     EN: GPIO pin connected to enabler pin of the motor controller`

**stop**(self)
:   `Stops the motor   This has no effect if motor is not rotating.`

**swap**()
:   `Swap the forward and backward directions   No need to change any circuit connections`

* * * * *

Data descriptors defined here:\

**\_\_dict\_\_**
:   `dictionary for instance variables (if defined)`

**\_\_weakref\_\_**
:   `list of weak references to the object (if defined)`

 \
 class **LED**([\_\_builtin\_\_.object](__builtin__.html#object))

`   `

`Light Emitting Diode attached to the Pi   Use this class for LEDs, Laser Diodes or any other single pin controlled device for which the methods provided make sense `

 

Methods defined here:\

**\_\_init\_\_**(self, pin, mode=10)
:   `Constructs a LED object   Args:     pin: GPIO pin of the Pi connected to diode     mode: GPIO pin numbering mode, RPi.GPIO.BCM or RPi.GPIO.BOARD (default)   Raises:     ValueError: If mode is not RPi.GPIO.BCM or RPi.GPIO.BOARD`

**blink**(self, blinks, duration=0.1, interval=0.1)
:   `Blinks the LED for specified number of times   Args:     blinks: Number of time the LED will go on and off     duration: Duration in seconds for the LED to stay on (default: 0.1 seconds)     interval: Interval in seconds between LED turning off and turning back on (default: 0.1 seconds)`

**flash**(self, duration=0.01)
:   `Flashes the LED once   Args:     duration: Duration of the flash in seconds (default: 0.01 seconds)`

**get\_settings**()
:   `Returns a dictionary of the pin and mode of the LED   Dictionary contains the following keys:     MODE: Mode being used by the object as string     P: GPIO pin connected to the LED`

**off**(self)
:   `Turns off the LED`

**on**(self)
:   `Turns on the LED`

* * * * *

Data descriptors defined here:\

**\_\_dict\_\_**
:   `dictionary for instance variables (if defined)`

**\_\_weakref\_\_**
:   `list of weak references to the object (if defined)`

 \
 class **Servo**([\_\_builtin\_\_.object](__builtin__.html#object))

`   `

`Servo motor    Use this object for a servo connected to the Raspberry Pi `

 

Methods defined here:\

**\_\_init\_\_**(self, p, mode=10, freq=50, zero=3, slope=0.04722, lower=0, upper=360)
:   `Construct a new Servo object   For most standard servos, the default inputs will work, except when 0 postion needs to be changed or a specific PWM frequency is required   Args:     p: GPIO pin connected to the control pin of the servo     mode: GPIO pin numbering mode, RPi.GPIO.BCM or RPi.GPIO.BOARD (default)     freq: Frequency of internal PWM (default: 50)     zero: Zero degree position duty cycle (default: 3)     slope: Slope of the function that translates duty cycles to position (default: 0.04722)     lower: Lower limit on the position of servo in degrees (default: 0)     upper: Upper limit on the position of servo in degrees (default: 360)   Raises:     ValueError: If mode is not RPi.GPIO.BCM or RPi.GPIO.BOARD or lower and upper values don't make sense`

**change\_duty\_cycle**(self, dc)
:   `Changes the duty cycle of the internal PWM   Also sets the servo to the position for that duty cycle Can be used for obtaining d0 and d180 for the config method   Args:     dc: New duty cycle of the internal PWM   Raises:     ValueError: If duty cycle is not between 0 and 100, both inclusive`

**change\_freq**(self, freq)
:   `Changes the frequency of the internal PWM   After this, the servo will probably need to be reconfigured using config method   Args:     freq: The new frequency for the internal PWM   Raises:     ValueError: If frequency is negative or zero`

**change\_restrictions**(self, lower, upper)
:   `Changes the limits between which the servo can be set   Args:     lower: Lower limit on the position of servo in degrees     upper: Upper limit on the position of servo in degrees    Raises:     ValueError: If lower and upper values don't make sense`

**config**(self, d0, d180)
:   `Configure the servo positions   Resets the 0 position of servo and the recalculates the slope Note that there is no way to confirm the actual positions of the servo, so passing bad inputs to this can lead to undefined behavior of turn method   Args:     d0: New 0 degree position duty cycle     d180: New 180 degree position duty cycle   Raises:     ValueError: If d180 < d0 or either value is negative or zero`

**get\_settings**(self)
:   `Returns a dictionary of the settings of the servo   Dictionary contains the following keys:     MODE: Mode being used by the object as string     P: GPIO pin connected to the control pin of the servo     LOWER: Lower limit on the position of the servo in degrees     UPPER: Upper limit on the position of the servo in degrees`

**turn**(self, angle)
:   `Turn the servo to the specified angle   If angle is not between the limits set during construction or using change_restrictions later, servo is set to closest limit position   Args:     angle: Angle of desired position of the servo`

* * * * *

Data descriptors defined here:\

**\_\_dict\_\_**
:   `dictionary for instance variables (if defined)`

**\_\_weakref\_\_**
:   `list of weak references to the object (if defined)`

 \
 class
**SimpleMotor**([\_\_builtin\_\_.object](__builtin__.html#object))

`   `

`DC motor which does not require speed control   Use this object for a DC motor which does not need to be controlled using PWM `

 

Methods defined here:\

**\_\_init\_\_**(self, a, b, mode=10)
:   `Construct a new 'DCMotor' object.   Args:     a: GPIO pin number connected to one of the motor pins, directly or via a controller     b: GPIO pin number connected to the other motor pin, directly or via a controller     mode: GPIO pin numbering mode, RPi.GPIO.BCM or RPi.GPIO.BOARD (default)   Raises:     ValueError: If mode is not RPi.GPIO.BCM or RPi.GPIO.BOARD`

**backward**(self)
:   `Rotates the motor in an arbitrary direction.   The directions depend on the circuit connections and so cannot be guaranteed. Only guarantee is that forward and backward methods will always rotate in opposite directions.`

**forward**(self)
:   `Rotates the motor in an arbitrary direction.   The directions depend on the circuit connections and so cannot be guaranteed. Only guarantee is that forward and backward methods will always rotate in opposite directions.`

**get\_settings**(self)
:   `Returns a dictionary of GPIO pins being used and the mode of setup   Dictionary contains the following keys:     MODE: Mode being used by the object as string     A: GPIO pin connected to pin A of the motor controller     B: GPIO pin connected to pin B of the motor controller`

**stop**(self)
:   `Stops the motor   This has no effect if motor is not rotating.`

**swap**(self)
:   `Swap the forward and backward directions   No need to change any circuit connections`

* * * * *

Data descriptors defined here:\

**\_\_dict\_\_**
:   `dictionary for instance variables (if defined)`

**\_\_weakref\_\_**
:   `list of weak references to the object (if defined)`

 \
 **Functions**

`      `

 

**cleanup**()
:   `Same as RPi.GPIO.cleanup()`

 \
 **Data**

`      `

 

**\_\_all\_\_** = ['cleanup', 'DCMotor', 'SimpleMotor', 'Servo', 'LED']

