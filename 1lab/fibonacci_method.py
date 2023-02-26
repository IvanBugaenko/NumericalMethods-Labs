# Метод Фибоначчи
import numpy as np

def f(x):
    return np.sin(x)


def sequence_generation(a, b, eps):
        fib = [1, 1]
        while (fib[-1] + fib[-2]) < (b - a) / eps:
            fib.append(fib[-1] + fib[-2])
        fib.append(fib[-1] + fib[-2])
        return fib


def fibonacci_method(a0, b0, eps):
    F = sequence_generation(a0, b0, eps)
    n = len(F) - 1
    a, b = a0, b0
    while n > 2:
        x1, x2 = a + F[n - 1] * (b - a) / F[n], b - F[n - 1] * (b - a) / F[n]
        if f(x1) > f(x2):
            b = x1
            x1 = x2
            x2 = b - F[n - 2] * (b - a) / F[n - 1]
        else:
            a = x2
            x2 = x1
            x1 = a + F[n - 2] * (b - a) / F[n - 1]
        n -= 1

    print(f'x* = {(a + b) / 2}\nf* = {f((a + b) / 2)}')
        

fibonacci_method(-np.pi, np.pi/2, 0.1)
