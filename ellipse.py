import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms

def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    """
    Create a plot of the covariance confidence ellipse of *x* and *y*.

    Parameters
    ----------
    x, y : array-like, shape (n, )
        Input data.

    ax : matplotlib.axes.Axes
        The axes object to draw the ellipse into.

    n_std : float
        The number of standard deviations to determine the ellipse's radiuses.

    **kwargs
        Forwarded to `~matplotlib.patches.Ellipse`

    Returns
    -------
    matplotlib.patches.Ellipse
    """
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensional dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)

    # Calculating the standard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calculating the standard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)


numSamp = 50

mu_x1, sigma_x1 = -5, 6 # mean and standard deviation
mu_y1, sigma_y1 = 6, 4
mu_x2, sigma_x2 = 0, 2 # mean and standard deviation
mu_y2, sigma_y2 = 0, 2
x1 = np.random.normal(mu_x1, sigma_x1, numSamp)
y1 = np.random.normal(mu_y1, sigma_y1, numSamp)
x2 = np.random.normal(mu_x2, sigma_x2, numSamp)
y2 = np.random.normal(mu_y2, sigma_y2, numSamp)

# Plot Limits
limGr = 20
xLimits = (-1*limGr,limGr)
yLimits = (-1*limGr,limGr)

fig, axs = plt.subplots(1,1)

# plotting
axs.set_title("Line graph")
axs.axvline(c='grey', lw=1.5)
axs.axhline(c='grey', lw=1.5)
axs.scatter(x1, y1, color ="red")
axs.scatter(x2, y2, color ="green")

confidence_ellipse(x1, y1, axs, n_std=1.960, edgecolor="red")
confidence_ellipse(x2, y2, axs, n_std=1.960, edgecolor="green")

for i in range(len(x1)):
    axs.arrow(x1[i], y1[i], (x2[i]-x1[i]), (y2[i]-y1[i]),color = "blue",
    head_width=0.3, lw=0.2, shape="full", length_includes_head=True )
axs.set(xlim=xLimits, ylim=yLimits)

plt.show()
