import numpy as np


def f(x):
    return 20 - (x[0] - 1) * np.exp(1 - x[0]) - (x[1] - 2) * np.exp(2 - x)


def cyclic_coordinate_descent(x1, eps):
    while np.linalg.norm(np.array([3, 4]), ord=2):
        ...
