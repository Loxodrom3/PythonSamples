import matplotlib.pyplot as plt
import numpy as np

itter8 = 100
grphx = ([])
grphx.clear()
x10 = ([])   # Ten percentile
x10.clear()
x30 = ([])
x30.clear()
x50 = ([])   # Fifty percentile
x50.clear()
x70 = ([])
x70.clear()
x90 = ([])
x90.clear()
x95 = ([])   # Ninty five percentile
x95.clear()
x99 = ([])   # Ninty nine percentile
x99.clear()
x999 = ([])   # Ninty nine percentile
x999.clear()

numSamp = 300

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
    x10.insert(i,np.percentile(abs(x), 10))
    x30.insert(i,np.percentile(abs(x), 30))
    x50.insert(i,np.percentile(abs(x), 50))
    x70.insert(i,np.percentile(abs(x), 70))
    x90.insert(i,np.percentile(abs(x), 90))
    x95.insert(i,np.percentile(abs(x), 95))  # absolute value of x
    x99.insert(i,np.percentile(abs(x), 99))  # absolute value of x
    x999.insert(i,np.percentile(abs(x),99.9))  # absolute value of x

# plotting
plt.title("Itterations = " + ascii(itter8) + " numSamps= " + ascii(numSamp))
plt.hist(grphx,bins = numBins, color='gray',  density = True, orientation = histOrientation)
plt.hist(x10,  bins = numBins, color='cyan',  density = True, orientation = histOrientation)
plt.hist(x30,  bins = numBins, color='orange',density = True, orientation = histOrientation)
plt.hist(x50,  bins = numBins, color='orange',density = True, orientation = histOrientation)
plt.hist(x70,  bins = numBins, color='orange',density = True, orientation = histOrientation)
# plt.hist(stdx, bins = numBins, color='red',   density = True, orientation = histOrientation)
plt.hist(x90,  bins = numBins, color='orange',density = True, orientation = histOrientation)
# plt.hist(x95,  bins = numBins, color='blue',  density = True, orientation = histOrientation)
# plt.hist(x99,  bins = numBins, color='green', density = True, orientation = histOrientation)
plt.hist(x999,  bins = numBins, color='Red', density = True, orientation = histOrientation)

plt.xlim(xMin, xMax)
plt.show()
