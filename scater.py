import matplotlib.pyplot as plt
import numpy as np

# number samples and graph limits
numSamp = 25
limGr = 50
xLimits = (-1*limGr,limGr)
yLimits = (-1*limGr,limGr)

# Set up Random values
mu_x, sigma_x = 0, 6 # mean and standard deviation
mu_y, sigma_y = -2, 22
x = np.random.normal(mu_x, sigma_x, numSamp)
y = np.random.normal(mu_y, sigma_y, numSamp)
print(x)
# Define Plots
fig, axs = plt.subplots(1,1)

# origion lines
axs[0,0].plot((0,0),(yLimits), color="black")
axs[0,0].plot((xLimits),(0,0), color="black")
# plotting
axs[0,0].scatter(x, y, color ="red")
axs[0,0].set_title(("Scatter Plot of " + str(numSamp) + " points"), fontsize =8)
axs[0,0].grid()
axs[0,0].set_aspect('equal', 'box')
axs[0,0].set(xlim=(xLimits), ylim=(yLimits))


plt.show()
