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
arr=np.array([10,20,30,40,50])
print(arr)
new_arr=np.insert(arr,2,90,axis=0)
print(new_arr)
