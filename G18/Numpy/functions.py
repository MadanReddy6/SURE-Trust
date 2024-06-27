
import numpy as np

x = np.arange(1,13).reshape(3,4)
x = np.flip(x,axis=1).copy()
print(x)
print("_______")

# for i in np.nditer(x):
#     print(i)

# hstack, vstack, dstack

a1 = np.zeros((2,4), dtype=int)
a2 = np.zeros((3,2), dtype=int)
# print(a2)
print(np.vstack((x,a1)))
print("_______")
print(np.hstack((x,a2)))
print("_______")


x = np.arange(1,25).reshape(2,3,4)
print(x)
a1 = np.zeros((1,3,4), dtype=int)
a2 = np.zeros((2,1,4), dtype=int)
a3 = np.zeros((2,3,1), dtype=int)

print(np.vstack((x,a1)))
print(np.hstack((x,a2)))
print(np.dstack((x,a3)))
