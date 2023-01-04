import numpy as np
from numpy import random
rng = 15

for x in range(rng):
    r = random.rand()
    print(r)
print("\n") # blank line

mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, rng)
print(s)