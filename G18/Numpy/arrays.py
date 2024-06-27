import numpy as np

x1 = ("hi","ok","how")
x2 = [
    [
        [2,3,7],
        [9,2,4]
    ],
    [
        [4,2,0],
        [5,3,6]
    ]
]


y1 = np.array(x1)
y2 = np.array(x2, dtype=np.uint8)

# n- dimentional arrays

# print(y2)
# print(len(y2))
# print(y2.size)
# print(y2.ndim)
# print(y2.dtype)
# print(y2.shape)

arr = np.array([
    [
        [[0,0,0],[0,0,0]],
        [[0,0,0],[0,0,0]]
    ],
    [
        [[0,0,0],[0,0,0]],
        [[0,0,0],[0,0,0]]
    ]
])

print(arr)
print(arr.size)
print(arr.ndim)
print(arr.shape)
print(arr.dtype)

