"""
=======================
Header
=======================

"""
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

# Plot text
plotTitle = "Arrow Graph" # Overview Title
plotTitleCU = "Close up of final" # Title for the close up graph
xLabel    = "X Axis"
yLabel    = "Y Axis"

# CDI Plot Colors
DBlu = (  0/255,  61/255, 165/255)
LBlu = (102/255, 204/255, 255/255)
DGrn = (  0/255, 131/255,  61/255)
LGrn = (188/255, 218/255, 140/255)
Gry  = (208/255, 206/255, 206/255)

# Plot Limits
limGr1 = 6000
limGr2 = 200
xLimits1 = (-1*limGr1,limGr1)
yLimits1 = (-1*limGr1,limGr1)
xLimits2 = (-1*limGr2,limGr2)
yLimits2 = (-1*limGr2,limGr2)

# origional data
#x1 = [-968.5533352, 5701.833361, 5692.520396, -933.53864556, 1880.269828, 1163.899777, 431.1371727, 3585.78726, -466.0412291, 2148.204663, -2380.245797, 3716.161325, -1360.881347, 1788.870743, -5063.097285, 1202.630305, -5061.175557, 951.4418083, 1153.188174, -910.2192759, -4429.964175, -4428.45755, -1186.674527]
#y1 = [-1809.196663, -1749.85123, -1764.486807, -741.91098237, -2287.26652, 769.7979622, -523.4216769, -602.8574785, -665.5951562, -2308.569421, -1815.077626, -1895.880186, -3295.088133, -3914.096933, -1171.225864, 4490.79701, -1177.700875, 2549.92543, 2551.717946, -3801.74264, -1786.844565, -1793.265585, 6295.042542]
#x2 = [11.47203181, 26.73382711, 28.50346177, 19.09489844, 6.84324919, 111.1102926, 69.30373325, 91.29210023, 25.39859309, 23.44645231, 16.07662052, 24.97990217, 8.63208513, 3.0126432, 6.66956689, 3.02003773, 5.83890963, 5.71368472, 8.10007059, 3.04806583, 6.41856276, 6.28168004, 11.92973482]
#y2 = [-19.05544347, 0.21360917, 1.196682219, -10.45342748, 17.35887856, -94.38419136, -64.06145433, -82.67373532, -17.54393954, 33.92489155, -14.81325948, -1.554247489, 2.50136924, -1.99620199, 5.02607826, 2.35514922, 5.25979461, 5.30840906, 4.906913741, -14.4680754, -8.55658783, -9.09469319, -2.79406982]

imgList = ["BSG-104-20220829-053930-36659038", "BSG-104-20220829-053930-36659038", "BSG-104-20220829-053930-36659038",
           "BSG-108-20220819-054840-35632660", "BSG-108-20220819-054840-35632660",
           "BSG-112-20220721-083055-31906033", "BSG-112-20220721-083055-31906033", "BSG-112-20220721-083055-31906033",
           "BSG-112-20220726-063016-32739023", "BSG-112-20220726-063016-32739023",
           "BSG-114-20220705-142440-29423141", "BSG-114-20220705-142440-29423141",
           "BSG-115-20220714-150410-30862499", "BSG-115-20220714-150410-30862499", "BSG-115-20220714-150410-30862499", "BSG-115-20220714-150410-30862499", "BSG-115-20220714-150410-30862499", "BSG-115-20220714-150410-30862499", "BSG-115-20220714-150410-30862499",
           "BSG-117-20220614-122129-26834717", "BSG-117-20220614-122129-26834717", "BSG-117-20220614-122129-26834717", "BSG-117-20220614-122129-26834717"]
images = list(set(imgList)) # convert to a set to get unique names, and then change to a list so it is subscriptable
images = images.sort(reverse=False)
xRAW = [-968.5533352, 5701.833361, 5692.520396, -933.53864556, 1880.269828, 1163.899777, 431.1371727, 3585.78726, -466.0412291, 2148.204663, -2380.245797, 3716.161325, -1360.881347, 1788.870743, -5063.097285, 1202.630305, -5061.175557, 951.4418083, 1153.188174, -910.2192759, -4429.964175, -4428.45755, -1186.674527]
yRAW = [-1809.196663, -1749.85123, -1764.486807, -741.91098237, -2287.26652, 769.7979622, -523.4216769, -602.8574785, -665.5951562, -2308.569421, -1815.077626, -1895.880186, -3295.088133, -3914.096933, -1171.225864, 4490.79701, -1177.700875, 2549.92543, 2551.717946, -3801.74264, -1786.844565, -1793.265585, 6295.042542]
xRPC = [11.47203181, 26.73382711, 28.50346177, 19.09489844, 6.84324919, 111.1102926, 69.30373325, 91.29210023, 25.39859309, 23.44645231, 16.07662052, 24.97990217, 8.63208513, 3.0126432, 6.66956689, 3.02003773, 5.83890963, 5.71368472, 8.10007059, 3.04806583, 6.41856276, 6.28168004, 11.92973482]
yRPC = [-19.05544347, 0.21360917, 1.196682219, -10.45342748, 17.35887856, -94.38419136, -64.06145433, -82.67373532, -17.54393954, 33.92489155, -14.81325948, -1.554247489, 2.50136924, -1.99620199, 5.02607826, 2.35514922, 5.25979461, 5.30840906, 4.906913741, -14.4680754, -8.55658783, -9.09469319, -2.79406982]

print(imgList)
print(images)
stop
# Define Plots
row = 2
col = 4
fig, axs = plt.subplots(row,col) # define the subplots

# Scatter Plots i, j
for i in range(0, row):
    for j in range(0, col):
        print("row = ",i, " col = ", j)
        for k in range(len(images)):
            xRAWg =[] # reset x and ys to empts list
            yRAWg =[]
            xRPCg =[]
            yRPCg =[]
            for l in range(len(imgList)):
                if images[k] == imgList[l]:
                    # do once axs[i,j].plot((0,0),(yLimits1), color="black", lw=0.75)
                    # do once axs[i,j].plot((xLimits1),(0,0), color="black", lw=0.75)
                    # do once axs[i,j].set_facecolor(color= Gry)
                    print (images[k], " ,", imgList[l])
                    xRAWg.append(xRAW[l]) # x RAW for Graph
                    yRAWg.append(yRAW[l])
                    xRPCg.append(xRPC[l])
                    yRPCg.append(yRPC[l])
            # end for l
                axs[i,j].scatter(xRAW, yRAW, color =LBlu)
                axs[i,j].scatter(xRPC, yRPC, color =DGrn)
                axs[i,j].set_title(images[k], fontsize =8)
        #end for k
    # end for j
# end for i
plt.show()

# -----------------------------------------------
axs[i,j].plot((0,0),(yLimits1), color="black", lw=0.75)
axs[i,j].plot((xLimits1),(0,0), color="black", lw=0.75)
axs[i,j].set_facecolor(color= Gry)
axs[i,j].scatter(xRAW1, yRAW1, color =LBlu)
axs[i,j].scatter(xRPC1, yRPC1, color =DGrn)
axs[i,j].set_title(image1Name, fontsize =8)
# Draw arrows
for k in range(len(xRAW)):
    axs[i,j].arrow(xRAW[k], yRAW[k], (xRPC[k]-xRAW[k]), (yRPC[k]-yRAW[k]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

axs[i,j].grid()
axs[i,j].set_aspect('equal', 'box')
axs[i,j].set(xlim=(xLimits1), ylim=(yLimits1))


# Scatter Plot 2
axs[0,1].plot((0,0),(yLimits1), color="black")
axs[0,1].plot((xLimits1),(0,0), color="black")
axs[0,1].scatter(xRAW2, yRAW2, color ="red")
axs[0,1].scatter(xRPC2, yRPC2, color ="green")
axs[0,1].set_title(image2Name, fontsize =8)
# Draw arrows
for i in range(len(xRAW2)):
    axs[0,1].arrow(xRAW2[i], yRAW2[i], (xRPC2[i]-xRAW2[i]), (yRPC2[i]-yRAW2[i]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

axs[0,1].grid()
axs[0,1].set_aspect('equal', 'box')
axs[0,1].set(xlim=(xLimits1), ylim=(yLimits1))

# Scatter Plot 3
axs[0,2].plot((0,0),(yLimits1), color="black")
axs[0,2].plot((xLimits1),(0,0), color="black")
axs[0,2].scatter(xRAW3, yRAW3, color ="red")
axs[0,2].scatter(xRPC3, yRPC3, color ="green")
axs[0,2].set_title(image2Name, fontsize =8)
# Draw arrows
for i in range(len(xRAW3)):
    axs[0,2].arrow(xRAW3[i], yRAW3[i], (xRPC3[i]-xRAW3[i]), (yRPC3[i]-yRAW3[i]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

axs[0,2].grid()
axs[0,2].set_aspect('equal', 'box')
axs[0,2].set(xlim=(xLimits1), ylim=(yLimits1))

# Scatter Plot 4
axs[0,3].plot((0,0),(yLimits1), color="black")
axs[0,3].plot((xLimits1),(0,0), color="black")
axs[0,3].scatter(xRAW4, yRAW4, color ="red")
axs[0,3].scatter(xRPC4, yRPC4, color ="green")
axs[0,3].set_title(image2Name, fontsize =8)
# Draw arrows
for i in range(len(xRAW4)):
    axs[0,3].arrow(xRAW4[i], yRAW4[i], (xRPC4[i]-xRAW4[i]), (yRPC4[i]-yRAW4[i]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

axs[0,3].grid()
axs[0,3].set_aspect('equal', 'box')
axs[0,3].set(xlim=(xLimits1), ylim=(yLimits1))

# Scatter Plot 5
axs[1,0].plot((0,0),(yLimits1), color="black")
axs[1,0].plot((xLimits1),(0,0), color="black")
axs[1,0].scatter(xRAW5, yRAW5, color ="red")
axs[1,0].scatter(xRPC5, yRPC5, color ="green")
axs[1,0].set_title(image2Name, fontsize =8)
# Draw arrows
for i in range(len(xRAW5)):
    axs[1,0].arrow(xRAW5[i], yRAW5[i], (xRPC5[i]-xRAW5[i]), (yRPC5[i]-yRAW5[i]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

axs[1,0].grid()
axs[1,0].set_aspect('equal', 'box')
axs[1,0].set(xlim=(xLimits1), ylim=(yLimits1))

# Scatter Plot 6
axs[1,1].plot((0,0),(yLimits1), color="black")
axs[1,1].plot((xLimits1),(0,0), color="black")
axs[1,1].scatter(xRAW6, yRAW6, color ="red")
axs[1,1].scatter(xRPC6, yRPC6, color ="green")
axs[1,1].set_title(image2Name, fontsize =8)
# Draw arrows
for i in range(len(xRAW6)):
    axs[1,1].arrow(xRAW6[i], yRAW6[i], (xRPC6[i]-xRAW6[i]), (yRPC6[i]-yRAW6[i]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

axs[1,1].grid()
axs[1,1].set_aspect('equal', 'box')
axs[1,1].set(xlim=(xLimits1), ylim=(yLimits1))

# Scatter Plot 7
axs[1,2].plot((0,0),(yLimits1), color="black")
axs[1,2].plot((xLimits1),(0,0), color="black")
axs[1,2].scatter(xRAW7, yRAW7, color ="red")
axs[1,2].scatter(xRPC7, yRPC7, color ="green")
axs[1,2].set_title(image2Name, fontsize =8)
# Draw arrows
for i in range(len(xRAW7)):
    axs[1,2].arrow(xRAW7[i], yRAW7[i], (xRPC7[i]-xRAW7[i]), (yRPC7[i]-yRAW7[i]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

axs[1,2].grid()
axs[1,2].set_aspect('equal', 'box')
axs[1,2].set(xlim=(xLimits1), ylim=(yLimits1))

# Scatter Plot 8
axs[1,3].plot((0,0),(yLimits1), color="black")
axs[1,3].plot((xLimits1),(0,0), color="black")
axs[1,3].scatter(xRAW8, yRAW8, color ="red")
axs[1,3].scatter(xRPC8, yRPC8, color ="green")
axs[1,3].set_title(image2Name, fontsize =8)
# Draw arrows
for i in range(len(xRAW8)):
    axs[1,3].arrow(xRAW8[i], yRAW8[i], (xRPC8[i]-xRAW8[i]), (yRPC8[i]-yRAW8[i]),color = "blue",
    head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

axs[1,3].grid()
axs[1,3].set_aspect('equal', 'box')
axs[1,3].set(xlim=(xLimits1), ylim=(yLimits1))


# Show Plots
plt.show()
plt.savefig('arrows2axs.png')

