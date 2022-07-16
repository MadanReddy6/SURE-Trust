import numpy as np

x = np.array([
    [1,2],
    [3,4],
    [5,6]
])

# print(x.shape)
print(x.reshape(-1))
print(x.reshape((1,6)))
print(x.reshape((6,1)))
print(x.reshape((2,-1)))


x = np.array([1,2,3,4,5,6,7])

print(x.reshape((7,1)))
print(x.reshape((1,7)))


a = 3
b = 2
c = 3

x = np.arange(a*b*c)+1
print(x.reshape(a,b,c))




