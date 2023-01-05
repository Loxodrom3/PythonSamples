import numpy as np
from numpy import random
rng = 21

for i in range(rng):
    r = random.rand()
    print(r)
print("\n") # blank line

mu_x, sigma_x = 0, 6 # mean and standard deviation
mu_y, sigma_y = -2, 4
x = np.random.normal(mu_x, sigma_x, rng)
y = np.random.normal(mu_y, sigma_y, rng)
print(x)
print(y)
