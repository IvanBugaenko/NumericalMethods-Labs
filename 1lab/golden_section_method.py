# Метод Золотого сечения
from math import sqrt
import numpy as np

def f(x):
    return np.sin(x)


def golden_section_method(a0, b0, eps):
    tao = 3 - sqrt(5)
    a, b = a0, b0
    while b - a > eps:
        x1, x2 = a + (b - a) * tao, b - (b - a) * tao
        if f(x1) > f(x2):
            b = x1
            x1 = x2
            x2 = b - (b - a) * tao
        else:
            a = x2
            x2 = x1
            x1 = a + (b - a) * tao
    answer = sorted([(x1, f(x1)), (x2, f(x2))], key=lambda x: x[1])
    print(f'x* = {answer[0][0]}\nf* = {answer[0][1]}')

golden_section_method(-np.pi, np.pi/2, 0.1)
