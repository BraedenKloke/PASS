"""
    One possible solution among many. Make sure you 
    understand why each line is needed - once you do, I 
    recommend trying to write your own solution from memory/intuition.

    Yes, this question is long - more like 2-3 long answer questions in one.
"""

import numpy as np
import matplotlib.pyplot as plt


def sort_points(data_points: list) -> None:
    """
        Sorts a list of data points represented as tuples (x, y) 
        in ascending order based on their y-values.

        Note: Since lists are mutable, if you give a function a list, it'll
        modify the original list (it doesn't create a new list for the data_points
        parameter) -> give a function a list in pytutor and look at the arrows.

        This means we don't need a return value.

        >>> lst = [(1, 3), (3, 2), (4, 1)]
        >>> sort_points(lst)
        >>> print(lst)
        >>> [(4, 1), (3, 2), (1, 3)]
    """

    # Insertion sort, i is the index of what we're inserting next
    for i in range(1, len(data_points)):
        current_inserting = data_points[i]      # The point being inserted (a tuple)
        current_y = current_inserting[1]        # The y-value of the point being inserted (a float)

        # Now compare to the points before it (in the sorted region)
        j = i - 1

        """
        NOTE: we compare the y-values but move around the 
        actual data point (tuples). Y-values are at index 1.
        """

        # Keep shifting the points before it one slot up, until
        # we get to the first slot in the list OR the point before the 
        # current slot has a smaller y-value
        while j >= 0 and current_y < data_points[j][1]:
            # Shift up
            data_points[j + 1] = data_points[j]     # slot j is free
            j -= 1                                  # slot j + 1 is free

        # If either condition in the while loop is false, we found
        # the correct slot to place this point -> the free slot is at index j + 1.
        data_points[j + 1] = current_inserting


def linear_regression(data_points: list) -> tuple:
    """
        Returns the slope (a) and y-intercept (b) corresponding
        to the best-fit line through the specified points in data_points.

        Also returns a list of all the x-values and y-values <- optional, we'll use this in
        the main function to plot the scatter plot
    """

    # polyfit needs two seperate lists of x values and y values
    # Hence, these two lists will store them
    x_points = []
    y_points = []

    # Add the x and y values to the lists above.
    for x, y in data_points:
        x_points.append(x)
        y_points.append(y)

    # Get the equation of the line of best fit
    regression = np.polyfit(x_points, y_points, 1)

    a = regression[0]
    b = regression[1]

    return a, b, x_points, y_points


def plot(x_scatter: list, y_scatter: list, slope: float, y_int: float) -> None:
    """
        Creates and displays a two plots in one:
        - A scatter plot of the points represented by x_scatter and y_scatter
        - A continuous line with the equation y = slope * x + y_int
    """
    # Store the coefficient in a list for polyval
    regression_coeffs = [slope, y_int]

    # Generate x points for the continuous line - technically two points at 0 and 10 are enough
    # since it's a line. But, in general you'll want many points for a curvy curve (degree > 1).
    x_continuous = np.linspace(0, 10, 100)
    # Get the corresponding y-values to all those x values.
    y_continuous = np.polyval(regression_coeffs, x_continuous)

    # Plot the scatter plot and line together.
    plt.plot(x_scatter, y_scatter, 'o', x_continuous, y_continuous, '-')
    # And show it
    plt.show()

    """
    You could also do this:

    plt.scatter(x_scatter, y_scatter, c="red")
    plt.plot(x_regression, y_regression)
    plt.show()

    -> When you do plt.show(), your plot resets.
    """


def statistical_analysis(data_points: list[tuple[float, float]]) -> None:
    """
        Returns a dictionary containing the number of points in data_points, along
        with the minimum, maximum, median and mean of all their y-values.

        Plots a scatter plot of all the points along with their line of best fit.
    """
    # Store all the measures in a dictionary
    stats = {}

    # Sort the points with insertion sort to make getting
    # the measure simple.
    sort_points(data_points)

    stats["n"] = len(data_points)

    # The minimum is in the first index in the sorted points list.
    stats["min"] = data_points[0][1]

    # The maximum is in the last index in the sorted points list.
    stats["max"] = data_points[stats["n"] - 1][1]
    
    # median: 
    # if odd, it's just at n // 2                       [1, 2, 4] -> median at index 1 = 3 // 2
    # if even, it's average of n//2 - 1 and n//2        [1, 2, 4, 5] -> median is 0.5 * (2 + 4) = 3, 2 is at n//2 - 1 and 4 is at n // 2

    # odd
    if stats["n"] % 2 == 1:
        stats["median"] = data_points[stats["n"] // 2][1]

    # Not odd? Then even.
    else:
        median = 0.5 * (data_points[stats["n"] // 2 - 1][1] + data_points[stats["n"] // 2][1])
        stats["median"] = median
    
    # The mean is a standard average -> get the sum, divide by the number of points.
    total_y = 0
    for x, y in data_points:
        total_y += y 

    stats["mean"] = total_y / stats["n"]

    # Get the regression parameters
    slope, y_int, x, y = linear_regression(data_points)
    stats["best_fit"] = { "slope": slope, "y_intercept": y_int }

    # And plot the curve
    plot(x, y, slope, y_int)

    return stats

    
# Test
points = [(1, 3), (3, 2), (4, 1), (1, 1.5)]
print(statistical_analysis(points))