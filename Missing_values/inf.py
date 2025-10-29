import numpy as np
arr=np.array([1, 2, 3,np.inf, 4, -np.inf, 5])
print(np.isinf(arr))
print("Number of infinite values:", np.isinf(arr).sum())
