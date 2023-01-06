import matplotlib.pyplot as plt

numSamp = 21000

for i in range(numSamp):
    r = random.rand()
    print(r)
print("\n") # blank line

mu_x, sigma_x = 0, 6 # mean and standard deviation
mu_y, sigma_y = -2, 4
x = np.random.normal(mu_x, sigma_x, numSamp)
y = np.random.normal(mu_y, sigma_y, numSamp)
print(x)
print(y)

# plotting
plt.title("Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.scatter(x, y, color ="red")
plt.show()
