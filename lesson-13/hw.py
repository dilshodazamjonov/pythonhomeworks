import numpy as np

# 1. Create a vector with values ranging from 10 to 49.

vec = np.arange(10, 49)
print(vec)

# 2. Create a 3x3 matrix with values ranging from 0 to 8.

matrix_0_8 = np.arange(9).reshape(3,3)
print("\n3x3 matrix 0-8:\n", matrix_0_8)

# 3. Create a 3x3 identity matrix.

identity_matrix = np.eye(3)
print(identity_matrix)

# 4. Create a 3x3x3 array with random values.

random_matrix = np.random.rand(3, 3, 3)
print(random_matrix)

# 5. Create a 10x10 array with random values and find the minimum and maximum values.

array_10_10 = np.random.rand(10, 10)
print("\nMin:", array_10_10.min(), "Max:", array_10_10.max())

# 6. Create a random vector of size 30 and find the mean value.

vec_30 = np.random.rand(30)
print("\nMean of 30-size random vector:", vec_30.mean())

# 7. Normalize a 5x5 random matrix.

mat_5x5 = np.random.rand(5, 5)
normalized = (mat_5x5 - mat_5x5.min()) / (mat_5x5.max() - mat_5x5.min())
print("\nNormalized 5x5 matrix:\n", normalized)

# 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).

mat_5x3 = np.random.rand(5, 3)
mat_3x2 = np.random.rand(3, 2)
product_5x2 = np.dot(mat_5x3, mat_3x2)
print("\nProduct of 5x3 and 3x2:\n", product_5x2)

# 9. Create two 3x3 matrices and compute their dot product. 

A = np.random.rand(3, 3)
B = np.random.rand(3, 3)
dot_product = np.dot(A, B)
print("\nDot product of 3x3 matrices:\n", dot_product)

# 10. Given a 4x4 matrix, find its transpose.  

matrix_4x4 = np.random.rand(4, 4)
print("\nTranspose of 4x4:\n", matrix_4x4.T)

# 11. Create a 3x3 matrix and calculate its determinant. 

matrix_3x3 = np.random.rand(3, 3)
det = np.linalg.det(matrix_3x3)
print("\nDeterminant of 3x3 matrix:", det)

# 12. Create two matrices \( A \) (3x4) and \( B \) (4x3), and compute the matrix product \( A \cdot B \). 

A_3x4 = np.random.rand(3, 4)
B_4x3 = np.random.rand(4, 3)
product_3x3 = np.dot(A_3x4, B_4x3)
print("\nProduct of 3x4 and 4x3:\n", product_3x3)

# 13. Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.  

matrix = np.random.rand(3, 3)
vector = np.random.rand(3, 1)
mv_product = np.dot(matrix, vector)
print("\nMatrix-vector product:\n", mv_product)

# 14. Solve the linear system \( Ax = b \) where \( A \) is a 3x3 matrix, and \( b \) is a 3x1 column vector.  

A_sys = np.random.rand(3, 3)
b_sys = np.random.rand(3, 1)
x = np.linalg.solve(A_sys, b_sys)
print("\nSolution to Ax = b:\n", x)


# 15. Given a 5x5 matrix, find the row-wise and column-wise sums.

matrix_5x5 = np.random.rand(5, 5)
row_sums = matrix_5x5.sum(axis=1)
col_sums = matrix_5x5.sum(axis=0)
print("\nRow sums:\n", row_sums)
print("Column sums:\n", col_sums)