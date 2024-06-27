from matplotlib import pyplot as plt

x = [1,2,3,5]
y = [2,3,1,2]

# for lines or points/ here the color is same per plot
plt.plot(x, y,color='yellow', linewidth=5, alpha=0.8)
plt.plot(x, y, marker="*",linestyle="", color='red', markersize=20)

# just for points / color can change per point
# plt.scatter(x, y,color=["red","yellow","green","blue"], linewidth=5, alpha=0.8)


# plt.plot(x,y)
# plt.scatter(x,y)

plt.show()