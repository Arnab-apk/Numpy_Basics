import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"{arr}\n")
new_arr=np.delete(arr,0,axis=0) #deletes first row
print(f"{new_arr}\n")
new_arr=np.delete(arr,1,axis=1) #deletes second column
print(f"{new_arr}\n")