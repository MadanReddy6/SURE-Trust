from matplotlib import pyplot as plt

x = [1,2,3,5,1,2,3,5]
y = [2,3,1,2,1,2,3,5]

plt.title("Figure 5")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.scatter(y, x,color='black', alpha=0.8)

plt.show()