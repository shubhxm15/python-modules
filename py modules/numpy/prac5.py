import numpy as np

a = np.array([[2,6,4,9,0],[5,1,2,5,7]])

s = np.sort(a)
e = np.where(a % 2 == 0)   # to find a specific element in the array 

print(s)
print(e)
