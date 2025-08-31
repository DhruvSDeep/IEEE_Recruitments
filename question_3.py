import numpy as np
import random as rd

arr = []     #creating array, 1-100, 5x5
for i in range(5):
    row = []
    for j in range(5):
        row.append(rd.randint(1, 100))
    arr.append(row)
arr = np.array(arr)

max = max(arr.flatten())     # finding max, min, mean
min = min(arr.flatten())
mean = np.mean(arr)
print("The maximum value in the array is:", max)
print("The minimum value in the array is:", min)
print("The mean value in the array is:", mean)


# Normalizing the array
arr = ((arr - min) / (max - min))

arr = arr.flatten()      #flattening and sorting the array
arr.sort()
print("The sorted array is:", arr)