"""
np.delete(array,index,axis=None)
deletes elements from an array along a specified axis.
asix none is default and deletes the flattened array. 
"""
import numpy as np
arr=np.array([10,20,30,40])
new_arr=np.delete(arr,0)
print(f"{new_arr}\n")

