import RPi.GPIO as GPIO
from time import sleep

"""This module contains module level methods for the package.
"""

__all__ = ['cleanup']

def cleanup():
    """Same as RPi.GPIO.cleanup()"""
    GPIO.cleanup()

