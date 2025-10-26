#reshaping does not create a copy it only returns a view of teh numpy matrix

import numpy as np
arr=np.array([1,2,3,4,5,6])
reshaped_arr=arr.reshape(2,3)
print(reshaped_arr)


