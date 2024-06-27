import numpy as np

x = np.arange(1,16, dtype=int).reshape(3,5)

a = np.ones((1,5), dtype=int)
x = np.vstack((a,x))

b = np.full((4,1),2)
x = np.hstack((x,b))

x_ = x.mean(axis=1).reshape(-1,1)
# print(x.mean(axis=0))
# print(x)
# print(x_)
# bool_arr = x > x_
# print(bool_arr)
# print(x[bool_arr])

for i in np.nditer(x):
    print(i)


 


