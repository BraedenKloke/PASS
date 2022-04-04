import statistics as s
from random import randint
from typing import List, Tuple

MEAN = 0.018828201
VARIANCE = 0.021617


def mystery_fx(x: float) -> float:
    return 3 * (x ** 3) - 4 * (x ** 2)


def error() -> List[float]:
    n = s.NormalDist(mu=MEAN, sigma=VARIANCE ** (1 / 2))

    samples = n.samples(10, seed=randint(0, 100))

    return samples


def dataset() -> Tuple[List[float], List[float]]:
    error_x = error()
    error_y = error()

    x = []
    y = []

    x_val = 0
    for i in range(0, 10):
        x_val += 0.2

        x.append(round(x_val + error_x[i], 2))
        y.append(round(mystery_fx(x_val) + error_y[i], 2))

    return x, y


x, y = dataset()
print(x)
print(y)
