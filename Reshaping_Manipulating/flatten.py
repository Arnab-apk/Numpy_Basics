#used in cases when a multidimentioninal array need sto be converted to a 1d array
#.ravel->return a view(original array is affected)
#.flatten ->copy(original array is not affected)
import numpy as np
arr=np.array([[1,2,3,4,5],[10,20,30,40,50]])
print(f"{arr.ravel()} dimension is {(arr.ravel()).ndim}")
print(f"{arr.flatten()} dimension is {(arr.ravel()).ndim}")

