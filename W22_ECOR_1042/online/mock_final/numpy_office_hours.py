"""
Numpy Functions

- linspace
- polyval
- polyfit
- array
- exp 


Scipy

- fsolve: Find the roots for a function in a given range. Solves the equations f(x) = 0

fsolve(func, [start, end]) <- def func(x) -> float: return y

   f(x) = value 
=> f(x) - value = 0 ---> g(x) = 0

g(x) = f(x) - value


- fminbound
"""

import numpy as np
import scipy.optimize as sp
import math

"""
x = np.exp(u) -> x = e^u (e is euler's number = 2.718...)
"""
print(np.exp(2))
print(math.exp(2))

"""
x = np.array([1, 1.1, 2]) -> numpy's version of a python list
"""
lst = [1, 1.1, 2]
np_lst = np.array([1, 1.1, 2])

print("Python list:", lst, "First element:", lst[0])
print("Numpy array:", np_lst, "First element:", np_lst[0])

"""
x = np.linspace(start, end, number_of_points)
-> Generates number_of_points points between start and end (inclusive) - evenly spaced.
"""
x = np.linspace(0, 5, 6)    # [0, 1, 2, 3, 4, 5] 
print(x)

"""
y = np.polyval(polynomial_coefficients, x)
-> Take in an array of coefficients for a polynomials
ax^2 + bx + c
[a, b, c]

-> Take in a single x value or a list of x values
-> Return the polynomial evaluated at the the singular x value OR
-> a list of y values corresponding to the list of x values
"""

"""
Polynomial is x^2 + 1
"""
x_squared = [1, 0, 1]

f_1 = np.polyval(x_squared, 1) # x_squared[0] * ( 1 ** 2) + x_squared[1] * ( 1 ** 1) + x_squared[2] * ( 1 ** 0) 
f_2 = np.polyval(x_squared, 2)
f_3 = np.polyval(x_squared, 3)

print(f_1, f_2, f_3)    # 2, 5, 10

f_values = np.polyval(x_squared, [1, 2, 3])
print(f_values)

"""
x = np.polyfit(list_x_values, list_y_values, degree_poly_to_fit)
-> Return a np.array of the coefficients of the polynomial that
(curve) fits the specified points (first point is <x_values[0], y_values[0]>).

-> Curve Fit (Regression, Interpolation)

Polyfit does Regression:
- Degree is less than number_of_points - 1

Polyfit does Interpolation:
- Degree is larger or equal to number_of_points - 1
"""

"""
Line: (0,1), (1,3) -> y = 2x + 1 
"""

line_coeffs = np.polyfit([0, 1], [1, 3], 2)     # [2, 1]
print(line_coeffs)

"""
Line: (0,0), (1,1), (2, 4) -> y = x^2
"""

line_coeffs = np.polyfit([0, 1, 2], [0, 1, 4], 1)
print(line_coeffs)

def root_quadratic(x: float) -> float:
    return 4 * (x ** 2) + x - 2 - 5

roots = sp.fsolve(root_quadratic, [-5, 5])
print(roots)

"""
Intersection of two curves: 
f(x) = 4x^2 + x - 2
g(x) = x^3

We want the x values for when f(x) = g(x), these
are the same values for f(x) - g(x) = 0. (Roots of the left side).
"""
def intersection_function(x: float) -> float:
    """
    f(x) = g(x)

    h(x) = f(x) - g(x) = 0
    """
    return 4 * (x ** 2) + x - 2 - (x ** 3)

roots = sp.fsolve(intersection_function, [0, 2])
print(roots)

"""
How polyval works:
"""
coeffs = [1, 0, 0]
len_coeffs = len(coeffs)

# coeffs[0] * x ^ (len_coeffs - 1 - 0) + coeffs[1] * x ^ (len_coeffs - 1 - 1)

result = 0
x = 1
for i in range(len_coeffs):
    result += coeffs[i] * (x ** (len_coeffs - 1 - i))