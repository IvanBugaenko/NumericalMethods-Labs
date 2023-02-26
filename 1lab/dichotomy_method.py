# Метод дихотомии
import numpy as np

def f(x):
    return np.sin(x)


def dichotomy_method(a_0, b_0, eps):
    a, b = a_0, b_0
    while b - a > eps:
        x = (a + b) / 2
        x1, x2 = x - eps/2, x + eps/2
        if f(x1) > f(x2):
            a = x1
        else:
            b = x1

    print(f'x* = {(a + b) / 2}\nf* = {f((a + b) / 2)}')


dichotomy_method(-np.pi, np.pi/2, 0.1)