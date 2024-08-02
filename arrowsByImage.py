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


image1Name = ("BSG-104-20220829-053930-36659038")
xRAW1 = [ -968.5533352, 5701.833361, 5692.520396]
yRAW1 = [-1809.196663, -1749.85123,  -1764.486807]
xRPC1 = [ 11.47203181, 26.73382711, 28.50346177]
yRPC1 = [-19.05544347,  0.21360917,  1.196682219]

image2Name = ("BSG-108-20220819-054840-35632660")
xRAW2 = [-933.53864556, 1880.269828]
yRAW2 = [-741.91098237, -2287.26652]
xRPC2 = [19.09489844, 6.84324919]
yRPC2 = [10.45342748, 17.35887856]

image3Name = ("BSG-112-20220721-083055-31906033")
xRAW3 = [1163.899777,   431.1371727, 3585.78726]
yRAW3 = [ 769.7979622, -523.4216769, -602.8574785]
xRPC3 = [111.1102926,  69.30373325,  91.29210023]
yRPC3 = [-94.3841913, -64.06145433, -82.67373532]

image4Name = ("BSG-112-20220726-063016-32739023")
xRAW4 = [-466.0412291,  2148.204663]
yRAW4 = [-665.5951562, -2308.569421]
xRPC4 = [ 25.39859309, 23.44645231]
yRPC4 = [-17.54393954, 33.92489155]

image5Name = ("BSG-114-20220705-142440-29423141")
xRAW5 = [2380.245797,  3716.161325]
yRAW5 = [1815.077626, -1895.880186]
xRPC5 = [ 16.07662052, 24.97990217]
yRPC5 = [-14.81325948, -1.554247489]

image6Name = ("BSG-115-20220714-150410-30862499")
xRAW6 = [-1360.881347, 1788.870743, -5063.097285, 1202.630305, -5061.175557, 951.4418083, 1153.188174]
yRAW6 = [-3295.088133, -3914.096933, -1171.225864, 4490.79701, -1177.700875, 2549.92543, 2551.717946]
xRPC6 = [8.63208513, 3.0126432, 6.66956689, 3.02003773, 5.83890963, 5.71368472, 8.10007059]
yRPC6 = [2.50136924, -1.99620199, 5.02607826, 2.35514922, 5.25979461, 5.30840906, 4.906913741]

image7Name = ("BSG-117-20220614-122129-26834717")
xRAW7 = [ -910.2192759, -4429.964175, -4428.45755, -1186.674527]
yRAW7 = [-3801.74264,   -1786.844565, -1793.265585, 6295.042542]
xRPC7 = [3.04806583,   6.41856276,  6.28168004, 11.92973482]
yRPC7 = [-14.4680754, -8.55658783, -9.09469319, -2.79406982]

image8Name = ("All Images")
xRAW8 = [-968.5533352, 5701.833361, 5692.520396, -933.53864556, 1880.269828, 1163.899777, 431.1371727, 3585.78726, -466.0412291, 2148.204663, -2380.245797, 3716.161325, -1360.881347, 1788.870743, -5063.097285, 1202.630305, -5061.175557, 951.4418083, 1153.188174, -910.2192759, -4429.964175, -4428.45755, -1186.674527]
yRAW8 = [-1809.196663, -1749.85123, -1764.486807, -741.91098237, -2287.26652, 769.7979622, -523.4216769, -602.8574785, -665.5951562, -2308.569421, -1815.077626, -1895.880186, -3295.088133, -3914.096933, -1171.225864, 4490.79701, -1177.700875, 2549.92543, 2551.717946, -3801.74264, -1786.844565, -1793.265585, 6295.042542]
xRPC8 = [11.47203181, 26.73382711, 28.50346177, 19.09489844, 6.84324919, 111.1102926, 69.30373325, 91.29210023, 25.39859309, 23.44645231, 16.07662052, 24.97990217, 8.63208513, 3.0126432, 6.66956689, 3.02003773, 5.83890963, 5.71368472, 8.10007059, 3.04806583, 6.41856276, 6.28168004, 11.92973482]
yRPC8 = [-19.05544347, 0.21360917, 1.196682219, -10.45342748, 17.35887856, -94.38419136, -64.06145433, -82.67373532, -17.54393954, 33.92489155, -14.81325948, -1.554247489, 2.50136924, -1.99620199, 5.02607826, 2.35514922, 5.25979461, 5.30840906, 4.906913741, -14.4680754, -8.55658783, -9.09469319, -2.79406982]


# Scatter Plot 1
plt.subplot(2, 4, 1)
plt.scatter(xRAW1, yRAW1, color ="red")
plt.scatter(xRPC1, yRPC1, color ="green")
# Draw arrows
for i in range(len(xRAW1)):
    plt.arrow(xRAW1[i], yRAW1[i], (xRPC1[i]-xRAW1[i]), (yRPC1[i]-yRAW1[i]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

plt.grid()
plt.axis('equal')
plt.title=(image1Name)
plt.xlim(xLimits1)
plt.ylim(yLimits1)


# Scatter Plot 2
plt.subplot(2, 4, 2)
plt.scatter(xRAW2, yRAW2, color ="red")
plt.scatter(xRPC2, yRPC2, color ="green")
# Draw arrows
for i in range(len(xRAW2)):
    plt.arrow(xRAW2[i], yRAW2[i], (xRPC2[i]-xRAW2[i]), (yRPC2[i]-yRAW2[i]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

plt.grid()
plt.axis('equal')
plt.title = (image2Name)
plt.xlim(xLimits1)
plt.ylim(yLimits1)

# Scatter Plot 3
plt.subplot(2, 4, 3)
plt.scatter(xRAW3, yRAW3, color ="red")
plt.scatter(xRPC3, yRPC3, color ="green")
# Draw arrows
for i in range(len(xRAW3)):
    plt.arrow(xRAW3[i], yRAW3[i], (xRPC3[i]-xRAW3[i]), (yRPC3[i]-yRAW3[i]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

plt.grid()
plt.axis('equal')
plt.title = (image3Name)
plt.xlim(xLimits1)
plt.ylim(yLimits1)

# Scatter Plot 4
plt.subplot(2, 4, 4)
plt.scatter(xRAW4, yRAW4, color ="red")
plt.scatter(xRPC4, yRPC4, color ="green")
# Draw arrows
for i in range(len(xRAW4)):
    plt.arrow(xRAW4[i], yRAW4[i], (xRPC4[i]-xRAW4[i]), (yRPC4[i]-yRAW4[i]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

plt.grid()
plt.axis('equal')
plt.title = (image4Name)
plt.xlim(xLimits1)
plt.ylim(yLimits1)

# Scatter Plot 5
plt.subplot(2, 4, 5)
plt.scatter(xRAW5, yRAW5, color ="red")
plt.scatter(xRPC5, yRPC5, color ="green")
# Draw arrows
for i in range(len(xRAW5)):
    plt.arrow(xRAW5[i], yRAW5[i], (xRPC5[i]-xRAW5[i]), (yRPC5[i]-yRAW5[i]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

plt.grid()
plt.axis('equal')
plt.title = (image5Name)
plt.xlim(xLimits1)
plt.ylim(yLimits1)

# Scatter Plot 6
plt.subplot(2, 4, 6)
plt.scatter(xRAW6, yRAW6, color ="red")
plt.scatter(xRPC6, yRPC6, color ="green")
# Draw arrows
for i in range(len(xRAW6)):
    plt.arrow(xRAW6[i], yRAW6[i], (xRPC6[i]-xRAW6[i]), (yRPC6[i]-yRAW6[i]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

plt.grid()
plt.axis('equal')
plt.title = (image6Name)
plt.xlim(xLimits1)
plt.ylim(yLimits1)

# Scatter Plot 7
plt.subplot(2, 4, 7)
plt.scatter(xRAW7, yRAW7, color ="red")
plt.scatter(xRPC7, yRPC7, color ="green")
# Draw arrows
for i in range(len(xRAW7)):
    plt.arrow(xRAW7[i], yRAW7[i], (xRPC7[i]-xRAW7[i]), (yRPC7[i]-yRAW7[i]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

plt.grid()
plt.axis('equal')
plt.title = (image7Name)
plt.xlim(xLimits1)
plt.ylim(yLimits1)

# Scatter Plot 8
plt.subplot(2, 4, 8)
plt.scatter(xRAW8, yRAW8, color ="red")
plt.scatter(xRPC8, yRPC8, color ="green")
# Draw arrows
for i in range(len(xRAW8)):
    plt.arrow(xRAW8[i], yRAW8[i], (xRPC8[i]-xRAW8[i]), (yRPC8[i]-yRAW8[i]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

plt.grid()
plt.axis('equal')
plt.title = (image8Name)
plt.xlim(xLimits1)
plt.ylim(yLimits1)

# Show Plots
plt.savefig('arrowsEachImage.png')
plt.show()



