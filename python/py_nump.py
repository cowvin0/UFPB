import numpy as np
import functools


x = np.arange(1, 11, 1)

print(x[3:9])
print(x[-8:-2])
print(x[-8:9])
print([x for x in x if x > 2 and x < 9])
print(list(filter(lambda i: i > 2 and i < 9, x)))
print(x[(x >= 3) & (x < 9)])
print(x[3:-2])

x.reshape(2, 5, order="C")
