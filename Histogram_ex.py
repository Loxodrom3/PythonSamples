import matplotlib.pyplot as plt
import numpy as np

numSamp = 100000
mu_x, sigma_x = 0, 1 # mean and standard deviation
mu_y, sigma_y = -2, 22

# For Histogram graph
numBins = 30
histDensity = 'TRUE'
histOrientation = 'vertical'  # 'vertical' or 'horizontal'



x = np.random.normal(mu_x, sigma_x, numSamp)
y = np.random.normal(mu_y, sigma_y, numSamp)
print(x)
print(y)

# plotting
plt.title("histogram")
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.scatter(x, y, color ="red")
plt.hist(x, bins = numBins, density = histDensity, orientation = histOrientation)
plt.show()
