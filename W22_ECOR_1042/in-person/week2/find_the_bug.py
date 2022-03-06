"""
Author: Braeden Kloke
Version: March 6, 2022

Week: 2
Activity: 2

This Python code was designed for a "ECOR 1042: Data Management" PASS workshop.

Core concepts covered include:
* Tuples
* Imports and modules


Activity: Find the Bug!
-----------------------

Some of the code will run. Some of it won't. It's up to the student to find the bugs!
"""


# Q1 Imports and Modules
import math


def area_of_circle1(radius: float) -> float:
    """ Returns the area of a circle.
     
    The constant pi must be imported from Python's math library.
    """
    return pi * radius**2


# Q2 Imports and Modules
import math


def area_of_circle2(radius: float) -> float:
    """ Returns the area of a circle.
     
    The constant pi must be imported from Python's math library.
    """
    return math.pi * radius**2


# Q3 Imports and Modules
from math import pi


def area_of_circle3(radius: float) -> float:
    """ Returns the area of a circle.
     
    The constant pi must be imported from Python's math library.
    """
    return pi * radius**2


# Q4 Imports and Modules
from math import *


def area_of_circle4(radius: float) -> float:
    """ Returns the area of a circle.
     
    The constant pi must be imported from Python's math library.
    """
    return pi * radius**2


# Q5 Tuples
def tell_time1(time: tuple) -> None:
    """
    Prints the time in HH:MM:SS.
    
    >>> time = (11, 35, 0)
    >>> tell_time(time)
    "11:35:00"
    >>> time = (18, 5, 0)
    >>> tell_time(time)
    "18:05:00"
    """
    hours = time(0)
    minutes = time(1)
    seconds = time(2)

    # Convert hours to string
    if hours < 10:
        hours = '0' + str(hours)
    else:
        hours = str(hours)
    # Convert minutes to string
    if minutes < 10:
        minutes = '0' + str(minutes)
    else:
        minutes = str(minutes)
    # Convert seconds to string
    if seconds < 10:
        seconds = '0' + str(seconds)
    else:
        seconds = str(seconds)

    print(hours + ':' + minutes + ':' + seconds)


# Q6 Tuples
def tell_time2(time: tuple) -> None:
    """
    Prints the time in HH:MM:SS.
    
    >>> time = (11, 35, 0)
    >>> tell_time(time)
    "11:35:00"
    >>> time = (18, 5, 0)
    >>> tell_time(time)
    "18:05:00"
    """
    hours = time[0]
    minutes = time[1]
    seconds = time[2]

    # Convert hours to string
    if hours < 10:
        hours = '0' + str(hours)
    else:
        hours = str(hours)
    # Convert minutes to string
    if minutes < 10:
        minutes = '0' + str(minutes)
    else:
        minutes = str(minutes)
    # Convert seconds to string
    if seconds < 10:
        seconds = '0' + str(seconds)
    else:
        seconds = str(seconds)

    print(hours + ':' + minutes + ':' + seconds)


# Q7 Tuples
def tell_time3(time: tuple) -> None:
    """
    Prints the time in HH:MM:SS.
    
    >>> time = (11, 35, 0)
    >>> tell_time(time)
    "11:35:00"
    >>> time = (18, 5, 0)
    >>> tell_time(time)
    "18:05:00"
    """
    (hours, minutes, seconds) = time

    # Convert hours to string
    if hours < 10:
        hours = '0' + str(hours)
    else:
        hours = str(hours)
    # Convert minutes to string
    if minutes < 10:
        minutes = '0' + str(minutes)
    else:
        minutes = str(minutes)
    # Convert seconds to string
    if seconds < 10:
        seconds = '0' + str(seconds)
    else:
        seconds = str(seconds)

    print(hours + ':' + minutes + ':' + seconds)


# Q8 Tuples
def tell_time4(time: tuple) -> None:
    """
    Prints the time in HH:MM:SS.
    
    >>> time = (11, 35, 0)
    >>> tell_time(time)
    "11:35:00"
    >>> time = (18, 5, 0)
    >>> tell_time(time)
    "18:05:00"
    """
    hours, minutes, seconds = time

    # Convert hours to string
    if hours < 10:
        hours = '0' + str(hours)
    else:
        hours = str(hours)
    # Convert minutes to string
    if minutes < 10:
        minutes = '0' + str(minutes)
    else:
        minutes = str(minutes)
    # Convert seconds to string
    if seconds < 10:
        seconds = '0' + str(seconds)
    else:
        seconds = str(seconds)

    print(hours + ':' + minutes + ':' + seconds)


# Q9 Determining if Numbers are Odd or Even
def is_odd1(num: int) -> bool:
    """
    Returns true if number is odd, false otherwise.
    
    >>> is_odd(2)
    False
    >>> is_odd(-3)
    True
    """
    if num % 2 == 0:
        return True
    else:
        return False

# Q10 Determining if Numbers are Odd or Even


def is_odd2(num: int) -> bool:
    """
    Returns true if number is odd, false otherwise.
    
    >>> is_odd(2)
    False
    >>> is_odd(-3)
    True
    """
    if num % 2 == 1:
        return True
    else:
        return False

# Q11 Determining if Numbers are Odd or Even


def is_odd3(num: int) -> bool:
    """
    Returns true if number is odd, false otherwise.
    
    >>> is_odd(2)
    False
    >>> is_odd(-3)
    True
    """
    if num % 2 != 0:
        return True
    else:
        return False


