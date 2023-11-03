import matplotlib.pyplot as plt
import numpy as np

itter8 = 10000
grphx = ([])
grphx.clear()
tnx = ([])   # Ten percentile
tnx.clear()
ffx = ([])   # Fifty percentile
ffx.clear()
stdx = ([])  # Stand Deviation
stdx.clear()
nfx = ([])   # Ninty five percentile
nfx.clear()
nnx = ([])   # Ninty nine percentile
nnx.clear()

numSamp = 50

mu_x, sigma_x = 0, 1 # mean and standard deviation

# For Histogram graph
numBins = 51
histDensity = True
histOrientation = 'vertical'  # 'vertical' or 'horizontal'
xMin = -4  # adding limits to keep histogram range consistent
xMax = 4

for i in range(itter8):
    x = np.random.normal(mu_x, sigma_x, numSamp)
    grphx.insert(i, x[0])
    tnx.insert(i,np.percentile(abs(x), 10))
    ffx.insert(i,np.percentile(abs(x), 50))
    stdx.insert(i,np.std(x))
    nfx.insert(i,np.percentile(abs(x), 95))  # absolute value of x
    nnx.insert(i,np.percentile(abs(x), 99))  # absolute value of x

# plotting
plt.title("Itterations = " + ascii(itter8) + " numSamps= " + ascii(numSamp))
plt.hist(grphx,bins = numBins, color='gray',  density = False, orientation = histOrientation)
plt.hist(tnx,  bins = numBins, color='cyan',  density = False, orientation = histOrientation)
plt.hist(ffx,  bins = numBins, color='orange',density = False, orientation = histOrientation)
plt.hist(stdx, bins = numBins, color='red',   density = False, orientation = histOrientation)
plt.hist(nfx,  bins = numBins, color='blue',  density = False, orientation = histOrientation)
plt.hist(nnx,  bins = numBins, color='green', density = False, orientation = histOrientation)

plt.xlim(xMin, xMax)
plt.show()
