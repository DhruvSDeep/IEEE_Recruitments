import numpy as np
import random as rd

arr = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(rd.randint(1, 100))
    arr.append(row)
arr = np.array(arr)

max = max(arr.flatten())     
min = min(arr.flatten())
mean = np.mean(arr)
arr = ((arr - min) / (max - min))    # Till here is creating 5x5 normalised array



newArr = arr[1:4, 1:4]    # extracting 3x3 array
print(newArr)

lcol = newArr[:, 2:3]
frow = newArr[0:1, :] 

print(np.dot(frow, lcol)[0][0])     # finding dot product of first row and last column of 3x3 array