import numpy as np

# ایجاد دو ماتریس تصادفی با ابعاد 3x3
matrix1 = np.random.rand(3, 3)
matrix2 = np.random.rand(3, 3)

# چاپ ماتریس‌های ایجاد شده
print("ماتریس 1:")
print(matrix1)
print("ماتریس 2:")
print(matrix2)

# جمع دو ماتریس
result_sum = matrix1 + matrix2
print("جمع دو ماتریس:")
print(result_sum)

# ضرب یک ماتریس در یک عدد صحیح
scalar = 2
result_scalar_multiply = matrix1 * scalar
print(f"ضرب ماتریس 1 در {scalar}:")
print(result_scalar_multiply)

# ضرب دو ماتریس
result_matrix_multiply = np.dot(matrix1, matrix2)
print("ضرب دو ماتریس:")
print(result_matrix_multiply)
