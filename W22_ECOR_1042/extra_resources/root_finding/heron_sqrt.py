EPSILON = 0.001


def heron_sqrt(x: float) -> float:
    """
        Returns the square root of x.
        >>> exhaustive_sqrt(25.0)
        >>> 5.0
    """
    guess = 0.1

    while abs(guess ** 2 - x) > EPSILON:
        # Every iteration, our guess is improved by updating it
        # to be the average between the current guess and the ratio of
        # the target number and the guess. i.e updated_g = average(g + target / g)
        guess = (guess + (x / guess)) / 2

    return guess
