import numpy as np


x = np.array([
    [1,2],
    [3,4]
]) # 2,2

y = np.array([
    [5,6],
    [7,8],
]) # 2,2

# rows dimension should be the same
print(np.hstack((y,x))) 

# columns dimensions should be same
print(np.vstack((x,y)))

# both dimensions should be same
print(np.dstack((x,y)))

