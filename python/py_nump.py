from scipy.integrate import quad
from scipy.optimize import minimize import numpy as np

def integrar(error):
    def integra1(func):
        def integra2(*args):
            resultado = quad(lambda a: func(a, args[1]), 0, 100)
            return abs(1 - resultado[0]) < error
        return integra2
    return integra1

@integrar(error=1e-15)
def pdf_exp(x, lamb):
    return lamb * np.exp(- lamb * x)



# def minimiza(x0):
#     def minimiza1(func):
#         def minimiza2(*args):
#             def objective(parameters):



# def maxinho_exp(x, lamb):
#     n = len(x)
#     return n * np.log(lamb) - lamb * sum(x)


def py_sapply(x, func):

    if not isinstance(x, (dict, list)):
        raise TypeError("x datatype must be either a list or a dict")

    if isinstance(x, list):
        return [func(elemento) for elemento in x]
    else:
        return {k: func(v) for k, v in x.items()}


def py_apply(x, func, margin=0):
    pass