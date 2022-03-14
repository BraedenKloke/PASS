"""
Author: Braeden Kloke
Version: March 10, 2022

Week: 3
Activity: 2

This Python code was designed for a "ECOR 1042: Data Management" PASS workshop.

Core concepts covered include:
* Incremental Development
* 2D Matrices


Activity: Find the Bug!
-----------------------

Some of the code will run. Some of it won't. It's up to the student to find the bugs!
"""


# Q1 Review!

def is_odd(num: int) -> bool:
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

# Q2 Review!

import math


def area_of_circle(radius: float) -> float:
    """ Returns the area of a circle.
     
    The constant pi must be imported from Python's math library.
    """
    return pi * radius**2


# Q3 2D Matrices

def empty_board1() -> list:
    """ Returns an 8 x 8 empty board. """
    board = []

    return board


# Q4 2D Matrices

def empty_board2() -> list:
    """ Returns an 8 x 8 empty board. """
    board = [[]]

    return board


# Q5 2D Matrices

def empty_board3() -> list:
    """ Returns an 8 x 8 empty board. """
    board = [
        [None],
        [None],
        [None],
        [None],
        [None],
        [None],
        [None],
        [None]
    ]

    return board


# Q6 2D Matrices

def empty_board4() -> list:
    """ Returns an 8 x 8 empty board. """
    board = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]

    return board

# STOP! How do this all relate to incremental development?

# Q7 2D Matrices

def empty_board5() -> list:
    """ Returns an 8 x 8 empty board. """
    board = [
        [None, None, None, None, None, None, None, None] * 8
    ]

    return board


# Q8 2D Matrices

def empty_board6() -> list:
    """ Returns an 8 x 8 empty board. """
    board = [
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8
    ]

    return board


# Q9 2D Matrices

def empty_board7() -> list:
    """ Returns an 8 x 8 empty board. """
    board = [[None] * 8 for i in range(8)]

    return board

# STOP! How do this all relate to incremental development?


