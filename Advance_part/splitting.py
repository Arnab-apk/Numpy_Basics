"""
np.slpit(array,indices_or_sections,axis=0)
splits an array into multiple sub-arrays along a specified axis.
np.hsplit() - splits along the horizontal axis (columns).
np.vsplit() - splits along the vertical axis (rows).

"""
import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[7,8,9],[10,11,12]])
print(np.split(arr1,2,axis=0)) #splits into 2 arrays along rows
print(np.split(arr2,2,axis=0)) #splits into 2 arrays along rows
