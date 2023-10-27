import matplotlib.pyplot as plt
import numpy as np

itter8 = 100000
stdx = ([])
stdx.clear()
nfx = ([])
nfx.clear()

numSamp = 32

mu_x, sigma_x = 0, 1 # mean and standard deviation

# For Histogram graph
numBins = 51
histDensity = 'TRUE'
histOrientation = 'vertical'  # 'vertical' or 'horizontal'
xMin = 0  # adding limits to keep histogram range consistent
xMax = 4

for i in range(itter8):
    x = np.random.normal(mu_x, sigma_x, numSamp)
    # print(np.std(x))
    stdx.insert(i,np.std(x))
    nfx.insert(i,np.percentile(abs(x), 95))  # absolute value of x

# plotting
plt.title(numSamp)
plt.hist(nfx, bins = numBins, density = histDensity, orientation = histOrientation)
plt.xlim(xMin, xMax) 
plt.show()# Write your code here :-)
