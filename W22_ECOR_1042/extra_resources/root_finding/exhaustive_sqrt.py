from typing import Union
EPSILON = 0.001


def exhaustive_sqrt(x: float) -> Union[float, None]:
    """
        Returns the square root of x.
        >>> exhaustive_sqrt(25.0)
        >>> 5.0
    """

    # Step should be f(EPSILON) where f is the function we're finding the root for.
    step = EPSILON ** 2
    guess = 0.0             # An initial guess to start us off

    # Keep incrementing our guess by step until it's close enough
    # to the real root.
    while abs(guess ** 2 - x) >= EPSILON and guess <= x:
        guess += step

    # If we exit the loop, there's still a chance we missed the root
    # in which case guess <= x became false.
    if guess > x:
        return None
    else:
        return guess
