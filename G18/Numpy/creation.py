import numpy as np


a1 = np.array([
    [0,0,0,0],
    [0,0,0,0]
])
# print(a1)


a1 = np.zeros( (2,3,2,3) , dtype = int )
a1 = np.ones( (3,2,3) , dtype = int)
a1 = np.full( (2,3), 3 , dtype = np.float32)
a1 = np.arange(1,11, dtype=int)

a1 = np.random.rand(2,3,4)
a1 = np.random.randn(10,5)
a1 = np.random.randint(1,11, (2,3,4))
a1 = np.random.choice(["hi","hey","hello"], (3,2))
   
print(a1)