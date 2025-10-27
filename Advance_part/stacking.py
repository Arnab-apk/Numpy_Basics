import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[7,8,9],[10,11,12]])
#vertical stacking
v_stack=np.vstack((arr1,arr2))
print(f"Vertical Stacking:\n{v_stack}\n")
#horizontal stacking
h_stack=np.hstack((arr1,arr2))
print(f"Horizontal Stacking:\n{h_stack}\n")

