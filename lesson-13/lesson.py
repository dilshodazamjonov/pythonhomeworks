import numpy as np


# a = np.array([1, 2, 3, 4], np.int8)

# print(a)

# # Creating two dimentional array

# two_dimentional = np.array([[1, 2, 3, 4], [2,3,4,5]])
# print(two_dimentional, two_dimentional.ndim)

# # gettign shape 

# print(two_dimentional.shape)

# # getting the Type

# print(two_dimentional.dtype)

# # Get size

# print(two_dimentional.itemsize)

# # Total Size

# print(a.size)
# print(a.nbytes)

# a = np.array([[1, 2, 2, 4, 5, 7, 1], [8, 9, 10, 11, 12, 13, 14]])

# print(a)

# # Getting specific element

# print(a[1, 5])

# # Getting specific row

# print(a[1, :])

# # Getting specific column

# print(a[:, 2])

# # changing specific element
# a[1, 5] = 12
# print(a)

# INitializing all 0s array

a = np.ones((6,4))
print(a)

b = np.full((2,2), 99)
print(b)


# random numbers filling

c = np.random.rand(10,5)
print(c)

# random numbers specified 

d = np.random.randint(100, size=(3,3))
print(d.size)

# Getting identity matrix

e = np.identity(d.size)

print(e)

