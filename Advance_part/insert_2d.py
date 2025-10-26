"""
#np.insert(array,index,data,axix=None)
array-original array
index-position for insertion
value-the element to be inserted
axis-erturns a flatnned array if none
0-for 2 d array row wise insertion
1-for 2 d array column wise insertion

"""
import numpy as np
arr=np.array([[1,2],[3,4]])
print(f"{arr}\n")
#insert a new row
new_arr=np.insert(arr,0,[5,6],axis=0)
print(f"{new_arr} \n") 
#insert a new column
new_arr=np.insert(arr,0,[5,6],axis=1)
print(f"{new_arr}\n") 