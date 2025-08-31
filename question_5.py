import numpy as np
import matplotlib.pyplot as mpl

numsX = np.random.normal(loc=0, scale=1, size=1000)
numsY = np.random.normal(loc=0, scale=1, size=1000)

mpl.scatter(numsX, numsY)
mpl.xlabel('X-axis')
mpl.ylabel('Y-axis')
mpl.title('Scatter Plot of Randomly Generated Normally Chosen Numbers')
mpl.show()


