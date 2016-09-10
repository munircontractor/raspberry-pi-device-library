import RPi.GPIO as GPIO

""" This module contains classes for sensors.
"""

class Sensor(object):
    """Single input sensor attached to the Pi

    Use this class for PIR sensors, magnetic swtiches and other single input pin sensors
    """

    __PIN = -1
    __mode = GPIO.BOARD
    __trigger = None
    
    def __init__(self, pin, trigger=None, mode=GPIO.BOARD):
        """Constructs a Sensor object

        Args:
            pin: GPIO pin of the Pi connected to the sensor

        Raises:
            ValueError: If mode is not RPi.GPIO.BCM or RPi.GPIO.BOARD
            TypeError: If trigger is not a callable
        """

        if mode == GPIO.BOARD or mode == GPIO.BCM:
            self.__mode = mode
        else:
            raise ValueError("'mode' should be RPi.GPIO.BOARD or RPi.GPIO.BCM")
        self.__PIN = pin
        if not(callable(trigger) or trigger == None):
            raise TypeError("'trigger' should be a callable function")
        self.__trigger = trigger
        GPIO.setmode(mode)
        GPIO.setup(pin, GPIO.IN)

