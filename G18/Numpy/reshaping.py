import numpy as np

x = np.arange(1,61,dtype=int)


# print(x.reshape(2,10))

# print(x.reshape(10,2))

# print(x.reshape(2,5,2))
# print(x.reshape(5,2,2))
x = x.reshape(3,2,2,5)
# print(x)
# print(x[:,0,0,-1])
# print(x[:,1,:,1:4])

# [[[[ 1  2  3  4  5]
#    [ 6  7  8  9 10]]

#   [[11 12 13 14 15]
#    [16 17 18 19 20]]]


#  [[[21 22 23 24 25]
#    [26 27 28 29 30]]

#   [[31 32 33 34 35]
#    [36 37 38 39 40]]]


#  [[[41 42 43 44 45]
#    [46 47 48 49 50]]

#   [[51 52 53 54 55]
#    [56 57 58 59 60]]]]

matrix = np.arange(1,25).reshape(2,3,4)

# print(matrix)
# print(matrix.T)

# print(np.flip(matrix, axis=0)) # along verical axis 
# print(np.flip(matrix, axis=1)) # along horizontal axis

# sort
# unique
# nditr

# print(matrix)
# print("__________")
# print(matrix.sum(axis = 0)) # row-wise 
# print("__________")
# print(matrix.sum(axis = 1))
# print("__________")
# print(matrix.sum(axis = 2))
# print(matrix.max(axis = 0)) # column-wise

x = np.random.randint(1,6, (2,5))
# print(x)

x.sort(axis=1)

# print(np.unique(x))