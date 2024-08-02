import numpy as np
from numpy import random
import matplotlib.pyplot as plt

# Plot text
plotTitle = "Arrow Graph" # Overview Title
plotTitleCU = "Close up of final" # Title for the close up graph
xLabel    = "X Axis"
yLabel    = "Y Axis"
limGr1 = 6000
limGr2 = 200
xLimits1 = (-1*limGr1,limGr1)
yLimits1 = (-1*limGr1,limGr1)
xLimits2 = (-1*limGr2,limGr2)
yLimits2 = (-1*limGr2,limGr2)
# Generate Random data sets for x1,y1 and x2,y2
numSamp = 23

mu_x1, sigma_x1 = -4, 4 # mean and standard deviation
mu_y1, sigma_y1 = 3, 6
mu_x2, sigma_x2 = 0, 1 # mean and standard deviation
mu_y2, sigma_y2 = 0, 1

x1 = [-968.5533352, 5701.833361, 5692.520396, -933.53864556, 1880.269828, 1163.899777, 431.1371727, 3585.78726, -466.0412291, 2148.204663, -2380.245797, 3716.161325, -1360.881347, 1788.870743, -5063.097285, 1202.630305, -5061.175557, 951.4418083, 1153.188174, -910.2192759, -4429.964175, -4428.45755, -1186.674527]
y1 = [-1809.196663, -1749.85123, -1764.486807, -741.91098237, -2287.26652, 769.7979622, -523.4216769, -602.8574785, -665.5951562, -2308.569421, -1815.077626, -1895.880186, -3295.088133, -3914.096933, -1171.225864, 4490.79701, -1177.700875, 2549.92543, 2551.717946, -3801.74264, -1786.844565, -1793.265585, 6295.042542]
x2 = [11.47203181, 26.73382711, 28.50346177, 19.09489844, 6.84324919, 111.1102926, 69.30373325, 91.29210023, 25.39859309, 23.44645231, 16.07662052, 24.97990217, 8.63208513, 3.0126432, 6.66956689, 3.02003773, 5.83890963, 5.71368472, 8.10007059, 3.04806583, 6.41856276, 6.28168004, 11.92973482]
y2 = [-19.05544347, 0.21360917, 1.196682219, -10.45342748, 17.35887856, -94.38419136, -64.06145433, -82.67373532, -17.54393954, 33.92489155, -14.81325948, -1.554247489, 2.50136924, -1.99620199, 5.02607826, 2.35514922, 5.25979461, 5.30840906, 4.906913741, -14.4680754, -8.55658783, -9.09469319, -2.79406982]
# x1 = np.random.normal(mu_x1, sigma_x1, numSamp)
# y1 = np.random.normal(mu_y1, sigma_y1, numSamp)
# x2 = np.random.normal(mu_x2, sigma_x2, numSamp)
# y2 = np.random.normal(mu_y2, sigma_y2, numSamp)

# plotting info
# plt.title(plotTitle)
# plt.xlabel(xLabel)
# plt.ylabel(yLabel)

# Scatter Plot 1
plt.subplot(1, 2, 1)
plt.scatter(x1, y1, color ="red")
plt.scatter(x2, y2, color ="green")

# Draw arrows
for i in range(len(x1)):
    plt.arrow(x1[i], y1[i], (x2[i]-x1[i]), (y2[i]-y1[i]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

plt.grid()
plt.axis('equal')
plt.xlim(xLimits1)
plt.ylim(yLimits1)


# Scatter Plot 2
plt.subplot(1, 2, 2)
plt.scatter(x1, y1, color ="red")
plt.scatter(x2, y2, color ="green")

# Draw arrows
for i in range(len(x1)):
    plt.arrow(x1[i], y1[i], (x2[i]-x1[i]), (y2[i]-y1[i]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

plt.grid()
plt.axis('equal')
plt.xlim(xLimits2)
plt.ylim(yLimits2)

# Show Plots
plt.savefig('graph.png')
plt.show()


