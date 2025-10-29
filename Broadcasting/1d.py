#expanding 1d array to 2d array
import numpy as np
prices = np.array([[1,2,3],[4,5,6]])#2d
vector = np.array([10,20,30])#1d
result = prices + vector
print(result)
