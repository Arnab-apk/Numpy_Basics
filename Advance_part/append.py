import numpy as np
arr=np.array([[1,2],[3,4]])
print(f"{arr}\n")
#append a new row
new_arr=np.append(arr,[[5,6]],axis=0)
print(f"{new_arr}\n")
#append a new column
new_arr=np.append(arr,[[5],[6]],axis=1)
print(f"{new_arr}\n")