import sys
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


def velo_motorista(velo):
    if velo > 80:
        print(f"Você foi multado, esse é o valor de sua multa: {5 * velo}")
    else:
        print("Muito bem, você não está acima da velocidade limite.")


def numeros(numeros):
    print(f"Esses são seus valores na ordem correta: {numeros[1:].sort()}")


def salario_func(salario):
    if salario > 1250:
        return salario * 1.1
    else:
        return salario * 1.5


def is_prime(num):
    while True:
        for i in range(2, num):
            if num % i == 0:
                print(f"O número {num} não é primo.")
                break
            else:
                print(
                    r"""
                      Ainda não foi confirmado não ser primo,
                      continue a iteração...
                    """
                )
                continue
        break


def is_cdf(func, *kwargs):
    is_non_decreasing = all((func(i) < func(i + 1)) for i in range(-10, 100))


