EPSILON = 0.001

__author__ = "yousef"


def bisection_sqrt(x: float) -> float:
    """
        Returns the square root of x.
        >>> exhaustive_sqrt(25.0)
        >>> 5.0
    """
    # Define an initial search range. The positive square root of a number
    # MUST be in the range of 0 to the number itself.
    low = 0
    high = x

    # Our guess at every iteration is the midpoint of the current range
    # i.e we halve our search range every iteration.
    guess = (low + high) / 2

    while abs(guess ** 2 - x) >= EPSILON and low < high:
        # If the guess^2 is less than x, we need a larger guess
        # so we have a new lower bound
        if guess ** 2 < x:
            low = guess
        # Otherwise, we need a smaller guess so we have a new
        # upper bound
        else:
            high = guess

        # Update the guess
        guess = (low + high) / 2

    return guess
