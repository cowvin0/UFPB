from scipy.integrate import quad
import numpy as np

def integrar(func):
    def integra(x, lamb):
        resultado = quad(lambda a: func(a, lamb), 0, 100)
        return abs(1 - resultado[0]) < 1e-2 
    return integra

@integrar
def pdf_exp(x, lamb):
    return lamb * np.exp(- lamb * x)