import numpy as np
from numpy import random
import matplotlib.pyplot as plt

numSamp = 20

for i in range(numSamp):
    r = random.rand()
    print(r)
print("\n") # blank line

mu_x1, sigma_x1 = -5, 6 # mean and standard deviation
mu_y1, sigma_y1 = 6, 4
mu_x2, sigma_x2 = 0, 1 # mean and standard deviation
mu_y2, sigma_y2 = 0, 1
x1 = np.random.normal(mu_x1, sigma_x1, numSamp)
y1 = np.random.normal(mu_y1, sigma_y1, numSamp)
x2 = np.random.normal(mu_x2, sigma_x2, numSamp)
y2 = np.random.normal(mu_y2, sigma_y2, numSamp)
pts1 = ([1,2],[1,4],[2,2], )

# plotting
plt.title("Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.scatter(x1, y1, color ="red")
plt.scatter(x2, y2, color ="green")

# for i in range(len(x1)):
#     lineStr = [x1[i],y1[i]] # eine Start
#     lineEnd = [x2[i],y2[i]] # line End
#     plt.plot(lineStr, lineEnd)

for i in range(len(x1)):
    plt.arrow(x1[i], y1[i], (x2[i]-x1[i]), (y2[i]-y1[i]),color = "blue", 
    head_width=0.3, lw=0.2, shape="full", length_includes_head=True )
plt.xlim((-20,20))
plt.ylim((-20,20))
plt.show()
