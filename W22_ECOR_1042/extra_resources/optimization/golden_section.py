# type: ignore
from math import sqrt, exp
from typing import Callable

"""
Implementation of Golden Section Search

We define two bounds, a lower bound xl and an upper bound xu.
We also define the golden ratio Φ = 1.618.

At every iteration, we compute three values:
    - A distance, d = (Φ - 1)(xu - xl) = 0.618(xu - xl)
    - A two bound candidates..
        x_1 = xl + d
        x_2 = xu - d

    Notice that d is a bit past the midpoint of the distance
    between xu and xl. So, x1 is closer to xu and x2 is closer to xl.

    To shrink our search range [xl, xu] we'll either replace xl with x2
    or xu with x1.

    Remember the goal is to find a minimum. So, we'd like to ensure that a
    (local) minimum exists in our search interval at each iteration.

    To do this, we'll update the search range with the new bound that produces
    the larger value when put in our function. In other words:
        - If f(x1) > f(x2): x1 is used to update xu.
        - Otherwise, f(x2) >= f(x1): x2 is used to update xl.

    The smaller of the two will remain in the search range and guarantees that
    there is atleast one more value in the interval smaller than both bounds.

    By the math, it turns out that the unpicked candidate (x1 or x2) switches
    roles in the next iteration. So, if you don't pick x1, it'll become x2 in
    the next interval. If you don't pick x2, it'll become x1 in the next interval
    (do the math once to convince yourself).
"""

PHI = (1 + sqrt(5)) / 2     # The golden ratio: 1.618


def golden_section(func: Callable[[float], float], xl: float, xu: float, tol: float = 1e-4) -> float:
    """
        Returns the minimum of func in the interval [xl, xu].
        >>> golden_section(min_object_height, 0, 15)
        >>> 3.8013720346725286
    """
    error = abs(xu - xl)        # The current error/distance between xu and xl

    # Find the two initial candidates.
    d = (PHI - 1) * (xu - xl)
    x1 = xl + d
    x2 = xu - d

    # Keep iterating until the distance between xu and xl is
    # incredibly small (< tol) - at which point, we've converged to the minimum.
    while (error > tol):

        # Update the search range with the candidate
        # that maps to a larger value through func.
        if (func(x1) > func(x2)):
            xu = x1
            x1 = None
        else:
            xl = x2
            x2 = None

        # Recompute the updated distance parameter.
        d = (PHI - 1) * (xu - xl)
        if (x1 is None):
            # If x2 wasn't picked, it becomes x1. We could
            # calculate it again but we'd get x1 so this saves time.
            x1 = x2
            x2 = xu - d
        else:
            # If x1 wasn't picked, it becomes x2. We could
            # calculate it again but we'd get x2 so this saves time.
            x2 = x1
            x1 = xl + d

        error = abs(xu - xl)    # Update the error
        # print(xu, xl)

    return (xl + xu) / 2        # Arbitrary decision: return the average of the converged search range.


G = 9.81


# Object height from lecture 10
def object_height(r: float, vo: float, t: float) -> float:
    return (1 / r) * (vo + G / r) * (1 - exp(-r * t)) - (G * t) / r


# Negate the function so we can find the maximum (negating it makes the
# maximum a minimum - which we can find with golden section search)
def min_object_height(t):
    r = 0.35
    vo = 78
    return -object_height(r, vo, t)


# fminbound returned 3.801383774408884 (lecture 10)
# golden_section returns 3.8013720346725286 -> pretty good
print(golden_section(min_object_height, 0, 15))
