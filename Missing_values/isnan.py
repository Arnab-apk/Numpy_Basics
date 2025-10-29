import numpy as np
arr=np.array([1, 2, np.nan, 3,np.nan, 4])
print(np.isnan(arr))
print("Number of missing values:", np.isnan(arr).sum())
