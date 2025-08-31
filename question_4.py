import numpy as np
import random as rd

arr = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(rd.randint(1, 100))
    arr.append(row)
arr = np.array(arr)

newArr = arr[1:4, 1:4]
print(newArr)

lcol = newArr[:, 2:3]
frow = newArr[0:1, :]

print(np.dot(frow, lcol)[0][0])