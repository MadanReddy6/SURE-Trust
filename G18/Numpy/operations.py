import numpy as np

arr = np.array([
    [
        [[0,0,0],
        [0,0,0]],

        [[0,0,0],
        [0,0,0]]
    ],
    [
        [[0,0,0],
        [0,0,0]],

        [[0,0,0],
        [0,0,0]]
    ]
], dtype=int)

(2,2,2,3)


(1,2,2,3)
a1 = np.array([
    [
        [[1,1,1],
        [2,2,2]],

        [[3,3,3],
        [4,4,4]]
    ]
])


(2,1,2,3)
a2 = np.array([
    
    [
        [[1,1,1],
        [2,2,2]]
        
    ],
    [
        [[3,3,3],
        [4,4,4]]   
    ]
])
# print(arr.shape)

(2,2,1,3)
a3 = np.array([
    
    [
        [[1,1,1]],
        [[2,2,2]]
        
    ],
    [
        [[3,3,3]],
        [[4,4,4]]
    ]
])

(2,2,2,1)
a4 = np.array([
    [
        [[1],
         [2]],
        [[3],
         [4]]
    ],
    [
        [[5],
         [6]],
        [[7],
         [8]]
    ]
])

print(a1.shape)
print(arr+a1)

print(a2.shape)
print(arr+a2)

print(a3.shape)
print(arr+a3)

print(a4.shape)
print(arr+a4)
