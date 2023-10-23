import matplotlib.pyplot as plt
import numpy as np

numTrys = 10000
measureX = ([])
measureX.clear()
nfx = ([])
nfx.clear()

numSamp = 20

mu_x, sigma_x = 0, 1 # mean and standard deviation

# For Histogram graph
numBins = 31
histDensity = 'TRUE'
histOrientation = 'vertical'  # 'vertical' or 'horizontal'

for i in range(numTrys):
    x = np.random.normal(mu_x, sigma_x, numSamp)
    # print(np.std(x))
    measureX.insert(i,np.std(x))
    nfx.insert(i,np.percentile(x,95))

# plotting
plt.title("histogram")
plt.hist(nfx, bins = numBins, density = histDensity, orientation = histOrientation)
plt.show()
