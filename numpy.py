import numpy as np

#Create two 3x3 random matrices
matrix1 = np.random.rand(3, 3)
matrix2 = np.random.rand(3, 3)

# Print the created matrices
print("matrix 1:")
print(matrix1)
print("matrix 2:")
print(matrix2)

# Addition of two matrices
result_sum = matrix1 + matrix2
print("Addition of two matrices:")
print(result_sum)

# Multiplying a matrix by an integer
scalar = 2
result_scalar_multiply = matrix1 * scalar
print(f"Matrix multiplication in {scalar}:")
print(result_scalar_multiply)

# Multiplication of two matrices
result_matrix_multiply = np.dot(matrix1, matrix2)
print("Multiplication of two matrices:")
print(result_matrix_multiply)

# Multiplication of three matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

C = np.array([[0, 1, 0],
              [1, 0, 1],
              [0, 1, 0]])
result = np.dot(np.dot(A, B), C)
print("The result of multiplying three matrices:")
