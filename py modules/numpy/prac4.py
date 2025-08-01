import numpy as np

a = np.array([[1,2,1],[3,4,5]])
b = np.array([[6,7,6],[8,9,10]])

c = np.array([10,20,30,40,50])

print(np.concatenate([a,b]))  # adds the array whether vertically or horizontally

print(np.concatenate([a,b], axis = 1)) # 0 for vertical and 1 for horizontal

# we can also use np.hstack for horizontal and np.vstack for vertical

print(np.array_split(c,3))  # splits array in parts given like here is 3