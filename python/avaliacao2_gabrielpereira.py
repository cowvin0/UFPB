import numpy as np
from functools import wraps
from scipy.integrate import quad
from scipy.stats import weibull_min
from scipy.optimize import minimize

# Segunda avaliação de Python

# Gabriel de Jesus Pereira - 20200121424

# Questão 1


def f(lista):
    return [i ** 2 if i % 2 == 0 else i ** 3 for i in lista]

# >>> f([1, 2, 3])
# [1, 4, 27]

# Questão 2


def py_sapply(x, func):

    if not isinstance(x, (dict, list)):
        raise TypeError("x datatype must be either a list or a dict")

    if isinstance(x, list):
        return [func(elemento) for elemento in x]
    else:
        return {k: func(v) for k, v in x.items()}

# A função py_sapply itera sobre os elementos de uma lista e aplica uma função passada como argumento.
#   Caso seja um dicionário, itera sobre cara valor do dicionário e aplica a função.
# >>> py_sapply([[1, 2, 3, 4], 1, [3, 5, 6]], np.sum)
#   [10, 1, 14]
# >>> py_sapply({'a': [1, 2, 3, 4], 'b': 1, 'c': [3, 5, 6]}, np.sum)
#   {'a': 10, 'b': 1, 'c': 14}
# >>> py_sapply({'a': [1, 2, 3, 4], 'b': 1, 'c': [3, 5, 6]}, lambda x: [i + 1 for i in x] if isinstance(x, (list, tuple)) else x)
#   {'a': [2, 3, 4, 5], 'b': 1, 'c': [4, 6, 7]}


def py_apply(x, func, margin=0):
    match margin:
        case 0:
            return np.array([func(linha) for linha in x])
        case 1:
            array_ = np.array([func(x[:, pos]) for pos in range(x.shape[1])])
            if array_.ndim > 1:
                return array_.T
            else:
                return array_

# A função py_apply pode iterar sobre as linhas caso margin=0 ou sobre as colunas caso margin=1.
#   Durante a iteração, é aplicada alguma função que foi passada como argumento.
# >>> array = np.arange(12).reshape(4, 3)
# >>> py_apply(array, lambda x: [i + 1 for i in x], margin=1)
# array([[ 1,  2,  3],
#        [ 4,  5,  6],
#        [ 7,  8,  9],
#        [10, 11, 12]])
# >>> py_apply(array, np.prod)
# array([  0,  60, 336, 990])
# >>> py_apply(array, np.sum, margin=1)
# array([18, 22, 26])


# Questão 3


def integration(lim_inf, lim_sup):
    def integra1(func):
        def integra2(*args, **kwargs):
            resultado, _ = quad(func, lim_inf, lim_sup, args=args, **kwargs)
            return resultado
        return integra2
    return integra1


@integration(lim_inf=0, lim_sup=4)
def integra(x, a, b):
    return x ** 2 + a + b

# >>> integra(1, 2)
# 33.33333333333333

# Questão 4


def minim(x0, sample_dist, set_seed=42, **kwargs):
    def minim1(func):
        np.random.seed(set_seed)
        x = sample_dist(**kwargs)

        @wraps(func)
        def minim2(*args, **kwargs):
            result = minimize(
                func,
                x0=x0,
                args=(x,),
                method="L-BFGS-B",
                *args,
                **kwargs
            )
            return result.x
        return minim2
    return minim1


@minim(x0=[2, 15], sample_dist=weibull_min.rvs, **dict(c=2.17, scale=18, size=1000))
def log_likelihood(params, x):
    alpha, beta = params
    if alpha <= 0 or beta <= 0:
        return np.inf
    return -np.sum(np.log(weibull_min.pdf(x, alpha, scale=beta)))

#   O decorador minim (criado como exércicio passado para casa) serve para encontrar os
# parâmetros de distruições utilizando a função de verossimilhança.
#   Assim, basta decorar uma função de verossibilhança, como
# foi feito acima.
# >>> teste = log_likelihood()
# >>> teste
# array([ 2.14894163, 17.73597424])
#   O decorador *wraps* do functools te permite continuar utilizando a função de verossimilhança
# sem que esteja decorada.
# >>> log_vero = log_likelihood.__wrapped__
# >>> log_vero
# <function log_likelihood at 0x7a10fa49ae60>
# >>> log_vero((1,2), [1, 2, 3, 4])
# 7.772588722239782


# Questão 5


def prime_generator():
    numero_primo = 2
    while True:
        if all(numero_primo % prev_numero for prev_numero in range(2, numero_primo // 2 + 1)):
            yield numero_primo
        numero_primo += 1


primos = prime_generator()
for _ in range(10):
    print(f'Número primo: {next(primos)}')
