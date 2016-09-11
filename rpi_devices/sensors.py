import RPi.GPIO as GPIO
from threading import Thread

""" This module contains classes for sensors and switches.
"""

class Sensor(object):
    """Single input sensor attached to the Pi

    Use this class for PIR sensors and other single pin input sensors that do not require a software
    PUD resistor connected to the Pi, and the callback functions should be run in a single thread in
    order. Note that the callbacks will still be made in a separate thread from the main thread.
    """

    __PIN = -1
    __mode = GPIO.BOARD
    __callbacks = []
    __event = -1
    __event_detection = False
    
    def __init__(self, pin, mode=GPIO.BOARD):
        """Constructs a Sensor object

        Args:
            pin: GPIO pin of the Pi connected to the sensor

        Raises:
            ValueError: If ``mode`` is not RPi.GPIO.BCM or RPi.GPIO.BOARD
        """

        if mode == GPIO.BOARD or mode == GPIO.BCM:
            self.__mode = mode
        else:
            raise ValueError("'mode' should be RPi.GPIO.BOARD or RPi.GPIO.BCM")
        self.__PIN = pin
        GPIO.setmode(mode)
        GPIO.setup(pin, GPIO.IN)

    def add_event_detection(event, callbacks=[], bouncetime=200):
        """Starts event detection on the pin of the sensor for specified edge event

        Args:
            event: Type of edge event to detect; one of RPi.GPIO.RISING, RPi.GPIO.FALLING or RPi.GPIO.BOTH
            callbacks: A list of callbacks to be made in same order after event is detected
            bouncetime: Time, in milliseconds, during which further events are ignored after callback is made

        Raises:
            ValueError: If ``event`` is not RPi.GPIO.RISING, RPi.GPIO.FALLING or RPi.GPIO.BOTH
            TypeError: If any item in ``callbacks`` is not callable
            TypeError: If ``callbacks`` is not a list
        """

        try:
            e = [GPIO.RISING, GPIO.FALLING, GPIO.BOTH].index(event):
        except ValueError:
            raise ValueError("'event' must be one of RPi.GPIO.RISING, RPi.GPIO.FALLING or RPi.GPIO.BOTH")
        if not type(callbacks) == list:
            raise TypeError("'callbacks' must be a list")
        for callback in callbacks:
            if not callable(callback):
                raise TypeError("All items in 'callbacks' must be callable")
        GPIO.add_event_detect(self.__PIN, event)
        self.__event = ['RISING', 'FALLING', 'BOTH'][e]
        for callback in callbacks:
            GPIO.add_event_callback(self.__PIN, callback, bouncetime=bouncetime)
            self.__callbacks.append(callback)
        self.__event_detection = True

    def event_detected(self):
        """Returns whether event has been detected or not, if event detection has been set up.

        Raises:
            ValueError: If event detecction has not been set up
        """

        if not self.__event_detection:
            raise ValueError("Event detection has not been set up")
        return GPIO.event_detected(self.__PIN)

    def wait_for_edge(self, edge, timeout=5000):
        """Blocks execution if program until an edge is detected

        Args:
            edge: Type of edge to wait for, one of RPi.GPIO.RISING, RPi.GPIO.FALLING or RPi.GPIO.BOTH
            timeout: Time, in milliseconds, to wait before continuing with the rest of the program

        Returns:
            The channel at which the edge is detected

        Raises:
            ValueError: If ``edge`` is not one of RPi.GPIO.RISING, RPi.GPIO.FALLING or RPi.GPIO.BOTH
        """

        try:
            e = [GPIO.RISING, GPIO.FALLING, GPIO.BOTH].index(edge)
        except ValueError:
            raise ValueError("'edge' must be one of RPi.GPIO.RISING, RPi.GPIO.FALLING or RPi.GPIO.BOTH")
        GPIO.wait_for_edge(self.__PIN, edge, timeout=timeout)

    def remove_event_detection(self):
        """Stops event detection and further callbacks for the sensor."""
        if self.__event_detection:
            GPIO.remove_event_detect(self.__PIN)
            self.__event_detection = False
            self.__callbacks = []

    def get_settings(self):
        """Returns a dictionary of the pin, mode, event detection and callbacks of the sensor

        Dictionary contains the following keys:
          MODE: Mode being used by the sensor as string
          P: GPIO pin connected to the sensor
          EVENT: Event being listened for
          CALLBACKS: List of callbacks in the order they are called after an event is detected
        """

        return {'MODE': 'BOARD' if __mode == GPIO.BOARD else 'BCM', 'P': __PIN,
            'EVENT': __event, 'CALLBACKS': __callbacks}
