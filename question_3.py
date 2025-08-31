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
print("The maximum value in the array is:", max)
print("The minimum value in the array is:", min)
print("The mean value in the array is:", mean)

arr = ((arr - min) / (max - min))
print(arr)

arr = arr.flatten()
arr.sort()
print("The sorted array is:", arr)