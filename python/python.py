from numba import jit
from functools import lru_cache


@jit
def sum(elements):
    sum = elements[0]
    for i in range(1, len(elements)):
        sum += elements[i]

    return sum


@jit
def fatorial(value):
    prod = 1
    for i in range(1, value):
        prod *= value - i + 1
    return prod


@jit
def aprox_pi(lim):
    prev = 1
    i = 1
    sum = 1
    while True:
        numerator = (-1) ** i
        denom = 2 * i + 1
        sum += numerator / denom
        if abs(4 * (sum - prev)) < lim:
            break
        i += 1
        prev = sum

    return 4 * sum


@lru_cache
def fibonacci(n):
    a = 0
    b = 1
    c = 0

    for _ in range(n):
        c = a + b
        a = b
        b = c

    return c


# def is_cdf(func):
#     if
