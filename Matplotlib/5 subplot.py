from matplotlib import pyplot as plt

x = [1,2,3,4]
y = [4,3,2,1]
z = [2]*4

# the shape we'll pass in is 2,2 so the sublots will be structured like:
# [
#     [[1],[2]],
#     [[3],[4]]
# ]
plt.subplot(2,2,1)
plt.title("First")
plt.scatter(x,y, marker="+")

plt.subplot(2,2,4)
plt.title("Second")
plt.plot(x,x, linestyle="dashed")

plt.subplot(2,2,3)
plt.title("Third")
plt.plot(x,z, color="hotpink")

plt.subplot(2,2,2)
plt.title("Fourth")
plt.bar(["a","b","c","d"],z)

plt.show()