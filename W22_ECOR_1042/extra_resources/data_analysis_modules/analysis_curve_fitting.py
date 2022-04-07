"""
Data Analysis and Curve Fitting Example

Time Travel Analysis

Eren, a famous scientist in Japan, is obsessed with time travel and has come
really close to a machine that makes it reality.

Eren has associated and error score with his experiments - lower is better.
Depending on his use of magic (0 - 2.11), Eren finds the following Error scores:

Magic Usage: [0.12, 0.3, 0.61, 0.77, 0.97, 1.08, 1.35, 1.56, 1.75, 2.11]
Error Score: [-0.29, -0.6, -0.67, -1.34, -1.0, -0.89, 0.57, 2.1, 4.75, 7.94]

How much magic should eren use to minimize error?

a) Find a cubic regression for the data above. What is the equation?
b) How much error can we estimate for magic usage of 1?
c) Plot the cubic along with a scatter plot
d) How much magic is used for an error of -0.5?
e) How much magic should be used to minimize the error?
"""

# Our data-analysis module imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve, fminbound

# Define a list of x and y points to represent our data set
magic = [0.12, 0.3, 0.61, 0.77, 0.97, 1.08, 1.35, 1.56, 1.75, 2.11]         # x
error = [-0.29, -0.6, -0.67, -1.34, -1.0, -0.89, 0.57, 2.1, 4.75, 7.94]     # y


def main() -> None:
    """
    a) Find a cubic regression for the data above? What's the equation.
    """
    regression = np.polyfit(magic, error, 3)    # [ 0.23608757  3.71614026 -5.24373445  0.50705775]
    print(regression)                           # 0.23x^3 + 3.716x^2 - 5.24x + 0.507

    """
    b) How much error can we estimate for magic usage of 1?
    """
    # Magic is the independent variable (x) that we change.
    # Hence the regression is really a function: f(magic) -> error
    # We want to evaluate the regression polynomial for magic usage of 1 (i.e x = 1)
    error_1 = np.polyval(regression, 1)
    print("Estimated error is: ", error_1)

    """
    c) Plot the cubic regression along with a scatter plot
    """
    # Create a data set of points for the regression
    magic_r = np.linspace(0, 2.11, 100)
    error_r = np.polyval(regression, magic_r)

    # Plot and shot the regression as a continuous curve ('-')
    # and the original data set as a scatter plot ('o')

    # Can also use plt.scatter(magic, error) for just a scatter plot
    # or simply plt.plot(magic, error, 'o')

    plt.plot(magic, error, 'o', magic_r, error_r, '-')
    plt.show()

    """
    d) How much magic is used for an error of -0.5?
    """
    # This is the opposite of b) - We know have the error and
    # want to solve for the magic (given y, find x)

    # f(magic) = -0.5 => f(magic) + 0.5 = 0 <- The roots of this equation give our solution.

    # *Note*: The function argument to fsolve must be
    # a function with one input (x) and one output (y). So
    # we'll make a new function to wrap polyval (since it takes two arguments)
    def root05(m: float):
        return np.polyval(regression, m) + 0.5

    # We'll maintain the original data set's domain of 0 - 2.11
    range = [0, 2.11]
    e_magic = fsolve(root05, range)
    print("Estimated magic for error of -0.5: ", e_magic)

    """
    e) How much magic should be used to minimize the error? What is the minimum error?
    """
    # *Note*: The function argument to fminbound must be
    # a function with one input (x) and one output (y). So
    # we'll make a new function to wrap polyval (since it takes two arguments)
    def r_error(m: float):
        return np.polyval(regression, m)

    magic_min = fminbound(r_error, 0, 2.11)
    print("Magic for min error:", magic_min)
    error_min = r_error(magic_min)
    print("The minimum error is:", error_min)


if __name__ == "__main__":
    main()
