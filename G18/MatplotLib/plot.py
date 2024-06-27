import matplotlib.pyplot as plt

x = [1,2,3,5,1,2,3,5]
y = [2,3,1,2,1,2,3,5]

plt.subplot(3,2,(1,4))
plt.title("Random 1")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.scatter(y, x,c='black', s=40, alpha=1)


plt.subplot(3,2,(5,6))
plt.title("Random 2")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.scatter(x, y,c='hotpink', s=40, alpha=0.5)

plt.show()