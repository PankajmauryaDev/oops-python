import numpy as np

# 1. Create Array
arr = np.array([1, 2, 3, 4])
print("Array:", arr)

# 2. 2D Array
matrix = np.array([[1, 2], [3, 4]])
print("\nMatrix:\n", matrix)

# 3. Properties
print("\nShape:", arr.shape)
print("Dimension:", arr.ndim)
print("Data Type:", arr.dtype)

# 4. Special Arrays
zeros = np.zeros((2, 3))
ones = np.ones((2, 2))
range_arr = np.arange(1, 10)
linspace_arr = np.linspace(1, 10, 5)

print("\nZeros:\n", zeros)
print("Ones:\n", ones)
print("Range:", range_arr)
print("Linspace:", linspace_arr)

# 5. Indexing & Slicing
print("\nSecond Element:", arr[1])
print("Slice (1:3):", arr[1:3])

# 6. Math Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nAddition:", a + b)
print("Multiplication:", a * b)
print("Square Root:", np.sqrt(a))
print("Sum:", np.sum(a))

# 7. Reshape
reshaped = np.array([1,2,3,4,5,6]).reshape(2,3)
print("\nReshaped Array:\n", reshaped)

# 8. Random Numbers
rand = np.random.rand(3)
rand_int = np.random.randint(1, 10, 3)

print("\nRandom Float:", rand)
print("Random Int:", rand_int)

# 9. Statistics
data = np.array([10, 20, 30, 40])
print("\nMean:", np.mean(data))
print("Max:", np.max(data))
print("Min:", np.min(data))

print("\nProgram Finished")
