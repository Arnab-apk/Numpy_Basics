import numpy as np
arr1=np.array([[1, 2, 3],[4, 5,np.nan],[7, np.nan, 9]])
cleaned_arr=np.nan_to_num(arr1, nan=0)
print(cleaned_arr)