import matplotlib.pyplot as plt
import numpy as np

numSamps = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
itters = 10

mu_x, sigma_x = 0, 1 # mean and standard deviation
mu_y, sigma_y = -2, 22

for i in range(len(numSamps)):
    for j in range(1,itters,1):
        x = np.random.normal(mu_x, sigma_x, numSamps[i])
        StDEVx = np.std(x)
        print(numSamps[i], " ", j, "  ", StDEVx)

