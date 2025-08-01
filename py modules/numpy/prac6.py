import numpy as np

a = np.array([1,5,7,6,10,30,2])

print(np.sum(a))
print(np.min(a))             # min element in the array
print(np.max(a))             # max element in the array
print(np.size(a))
print(np.cumsum(a))          # cumulative sum
print(np.cumprod(a),'\n')    # cumulative product

price = np.array([100,500,700,420,120])
quantity = np.array([20,40,5,13,32])

print(price, '\n', quantity,'\n')

s = np.cumprod([price, quantity], axis = 0)
print(s[1])
print('Total price: ',s[1].sum())