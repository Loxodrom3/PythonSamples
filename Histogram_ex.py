import matplotlib.pyplot as plt
import numpy as np

numSamp = 100000
mu_x, sigma_x = 0, 1 # mean and standard deviation

# For Histogram graph
numBins = 30
histDensity = 'TRUE'
histOrientation = 'vertical'  # 'vertical' or 'horizontal'

x = np.random.normal(mu_x, sigma_x, numSamp)
print(x)

# plotting
plt.title("histogram")
plt.hist(x, bins = numBins, density = histDensity, orientation = histOrientation)
plt.show()
