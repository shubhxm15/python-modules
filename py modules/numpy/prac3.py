import numpy as np

a = ([1,2,3],[2,3,4])

array = np.array(a)

print(array)
print(array.shape) # rows and columns 
print(len(array)) # number of nested values
print(np.size(array)) # number of elements
print(array.dtype) # datatype of elements
print(type(array)) # datatype of array
print(array.astype(float)) # conversion of datatype
