import RPi.GPIO as GPIO
from time import sleep

"""This module contains the classes for LED and other diodes.
"""

__all__ = ['LED']

class LED(object):
    """Light Emitting Diode attached to the Pi

    Use this class for LEDs, Laser Diodes or any other single pin controlled device for which
    the methods provided make sense
    """

    __PIN = -1
    __mode = GPIO.BOARD

    def __init__(self, pin, mode=GPIO.BOARD):
        """Constructs a LED object

        Args:
            pin: GPIO pin of the Pi connected to diode
            mode: GPIO pin numbering mode, RPi.GPIO.BCM or RPi.GPIO.BOARD (default)

        Raises:
            ValueError: If mode is not RPi.GPIO.BCM or RPi.GPIO.BOARD
        """

        if mode == GPIO.BOARD or mode == GPIO.BCM:
            self.__mode = mode
        else:
            raise ValueError("'mode' should be RPi.GPIO.BOARD or RPi.GPIO.BCM")
        self.__PIN = pin
        GPIO.setmode(mode)
        GPIO.setup(pin, GPIO.OUT)

    def on(self):
        """Turns on the LED"""

        GPIO.setmode(__mode)
        GPIO.output(self.__PIN, GPIO.HIGH)

    def off(self):
        """Turns off the LED"""

        GPIO.setmode(__mode)
        GPIO.output(self.__PIN, GPIO.LOW)

    def flash(self, duration = 0.01):
        """Flashes the LED once

        Args:
            duration: Duration of the flash in seconds (default: 0.01 seconds)
        """

        self.on()
        sleep(duration)
        self.off()

    def blink(self, blinks, duration = 0.1, interval = 0.1):
        """Blinks the LED for specified number of times

        Args:
            blinks: Number of time the LED will go on and off
            duration: Duration in seconds for the LED to stay on (default: 0.1 seconds)
            interval: Interval in seconds between LED turning off and turning back on (default: 0.1 seconds)
        """

        for i in range(1, blinks + 1):
            self.flash(duration = duration)
            sleep(interval)

    def get_settings():
        """Returns a dictionary of the pin and mode of the LED

        Dictionary contains the following keys:
            MODE: Mode being used by the object as string
            P: GPIO pin connected to the LED
        """

        return {'MODE': 'BOARD' if __mode == GPIO.BOARD else 'BCM', 'P': __PIN}
