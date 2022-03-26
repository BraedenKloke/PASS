from math import sin, pi
from typing import Callable

__author__ = "yousef"


def sign(num: float) -> bool:
    """
        Returns true if num is positive or equal to 0,
        returns false otherwise.
        
        >>> sign(1)
        >>> True
        >>> sign(-1)
        >>> False
    """

    if num < 0:
        return False
    return True


def bisection_fx(x_lower: float, x_upper: float, f: Callable[[float], float]) -> float:
    """
        Returns a root of f in between x_lower and x_upper if it exists.

        Note: We're passing a function as a parameter here (you don't need to - calling f works too,
        doing it this way makes our bisection_fx more universal to any function though).
        Callable means this is a function with [[parameter types], return type].
        >>> bisection_fx(0, 2, () -> x - 1)
        >>> ~1.00
    """

    EPSILON = 1e-2

    f_lower = f(x_lower)    # lower bound
    f_upper = f(x_upper)    # upper bound

    # Check for opposite signs (one endpoint is +ve, the other -ve)
    # that means the curve crosses the x-axis, ie there's a root
    if sign(f_lower) == sign(f_upper):
        raise ValueError("Supplied bounds with same sign, cannot guarantee a root.")

    x_guess = (x_lower + x_upper)     # Bisect the search range to find a guess
    f_guess = f(x_guess)

    while abs(f_guess) >= EPSILON:    # Keep searching until f(x_guess) = ~0, then x_guess is the root.
        # print(x_guess)

        """
            ::brief bisection search
            As long as the two endpoints of our search range have different signs,
            we guarantee that a root is in the search range (since you need
            to cross the x-axis to switch signs) -> see intermediate value theorem.

            So, our algorithm works by shrinking the search range but MAINTAINING the
            property that both endpoints keep opposite signs.

            Suppose the search range is [l, h] where f(l) is -ve, f_h is +ve.

            A negative f_guess means x_guess replaces l since f(l) was -ve. Likewise,
            a positive f_guess means x_guess replaces h since f(l) was +ve.
        """

        # If the guess' sign matches the lower bound, guess
        # replaces the lower bound.
        if sign(f_guess) == sign(f_lower):
            x_lower = x_guess

        # Otherwise, it matches the sign of the upper
        # bound (remember, we stop if we get f_guess = ~0)
        else:
            x_upper = x_guess

        # Update our guess and f_guess
        x_guess = (x_lower + x_upper) / 2
        f_guess = f(x_guess)

    # Exiting the loop means f(x_guess) ~ 0, we found the root.
    return x_guess


if __name__ == "__main__":
    # For this test, I'm using f(x) = sinc(2πx) = sin(2πx) / (2πx).
    # Take a look on desmos, we expect a root at x = 0.5.

    # The function of x we're trying to find a root for.
    def f(x: float) -> float:
        """
            Returns the result of
            f(x) = <any function here: implement it below>.
            I have implemented f(x) = sinc(2πx) = sin(2πx) / (2πx).
        """

        # I'll use sin(2 * pi * T * x) / (2 * pi * T * x) = sinc(2 * pi * T * x)
        # This has a root at 0.5 * T * n for all non-zero integers n

        T = 1
        return sin(2 * pi * T * x) / (2 * pi * T * x)     # careful not to divide by 0!

    root = bisection_fx(0.1, 0.75, f)   # Don't do lower = 0, you'll get a divide by 0 error.
    print(root)                         # Gives us 0.498, good enough.
    assert abs(root - 0.5) < 1e-2
