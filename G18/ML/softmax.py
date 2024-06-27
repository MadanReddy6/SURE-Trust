x = [1,2,3,-4]



def softmax(arr):
    e = 2.7

    for i in range(len(arr)):
        arr[i] = e**arr[i]

    total = sum(arr)

    for i in range(len(arr)):
        arr[i] = arr[i]/total

    return arr



print(softmax(x))
