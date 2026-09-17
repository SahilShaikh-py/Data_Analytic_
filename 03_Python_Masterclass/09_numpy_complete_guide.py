"""
=============================================================================
TOPIC 05: NUMPY (NUMERICAL PYTHON) COMPLETE MASTER GUIDE
=============================================================================
Author: Python Mastery Course
Level: Beginner to Intermediate

Conceptual Overview:
--------------------
1. What is NumPy and Why is it Used?
   - NumPy (Numerical Python) is the foundational scientific computing library in Python.
   - It provides high-performance multi-dimensional array objects (ndarray) and 
     tools for working with these arrays.

2. Python Lists vs NumPy Arrays (Why NumPy is Superior for Analytics):
   - Fast Execution: Implemented in C, running 10x to 50x faster than standard Python lists.
   - Memory Efficiency: Contiguous memory storage ensures optimized cache utilization and lower RAM overhead.
   - Vectorization: Allows element-wise operations directly across arrays without explicit Python `for` loops.

3. Core Topics Covered in this Guide:
   - 1D, 2D, and 3D Array Creation (`np.array`, `zeros`, `ones`, `arange`, `linspace`, `eye`)
   - Array Attributes: `shape`, `ndim`, `dtype`, `size`
   - Array Indexing, Slicing & Reshaping (`reshape`, `flatten`)
   - Vectorized Arithmetic & Broadcasting Rules
   - Statistical Functions: `mean()`, `median()`, `std()`, `min()`, `max()`, `sum()`, `argmax()`
   - Boolean Indexing & Conditional Filtering
   - Advanced Array Manipulation (Stacking & Splitting)
   - Linear Algebra (`np.dot`, `np.linalg.det`)
   - Random Data Generation (`np.random`)
=============================================================================
"""

import numpy as np

print("=" * 65)
print(">>> PART 1: ARRAY CREATION & BASIC ATTRIBUTES <<<")
print("=" * 65)

# 1. 1D Array (Vector)
arr_1d = np.array([10, 20, 30, 40, 50])
print(f"• 1D Array:\n  {arr_1d}")
print(f"  Shape: {arr_1d.shape} | Dimensions: {arr_1d.ndim} | Data Type: {arr_1d.dtype}")

# 2. 2D Array (Matrix - Rows and Columns)
arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f"\n• 2D Matrix (3x3):\n{arr_2d}")
print(f"  Shape (Rows, Cols): {arr_2d.shape} | Dimensions: {arr_2d.ndim} | Total Elements: {arr_2d.size}")

# 3. Built-in Array Creation Functions
zeros_arr = np.zeros((2, 4))             # 2 Rows, 4 Cols filled with zeros
ones_arr = np.ones((3, 2), dtype=int)    # 3 Rows, 2 Cols filled with ones
range_arr = np.arange(10, 30, 2)         # Array from 10 to 30 with step size 2
linspace_arr = np.linspace(0, 1, 5)      # 5 evenly spaced numbers between 0 and 1
identity_matrix = np.eye(3)              # 3x3 Identity Matrix (Diagonal 1s, others 0)

print(f"\n• np.zeros((2,4)):\n{zeros_arr}")
print(f"\n• np.arange(10, 30, 2): {range_arr}")
print(f"\n• np.linspace(0, 1, 5): {linspace_arr}")
print(f"\n• 3x3 Identity Matrix (np.eye):\n{identity_matrix}")


print("\n" + "=" * 65)
print(">>> PART 2: INDEXING, SLICING & RESHAPING <<<")
print("=" * 65)

# Indexing & Slicing in 2D Array
# Syntax: array[row_start:row_end, col_start:col_end]
matrix = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
print(f"• Original Matrix (3x4):\n{matrix}")

# Accessing a specific element (Row 1, Column 2 -> 70)
print(f"\n• Element at Row 1, Col 2: {matrix[1, 2]}")

# Slicing the entire first row
print(f"• Row 0 complete: {matrix[0, :]}")

# Slicing the entire second column
print(f"• Column 1 complete: {matrix[:, 1]}")

# Slicing a sub-matrix (First 2 rows and middle 2 columns)
sub_matrix = matrix[0:2, 1:3]
print(f"\n• Sliced Sub-matrix (Rows 0-1, Cols 1-2):\n{sub_matrix}")

# Reshaping: Transforming a 1D array (12 elements) into (4x3)
flat_arr = np.arange(1, 13) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
reshaped_4x3 = flat_arr.reshape(4, 3)
print(f"\n• Reshaped from 1D to 4x3:\n{reshaped_4x3}")

# Flatten: Converting multi-dimensional array back to 1D
flattened = reshaped_4x3.flatten()
print(f"• Flattened back to 1D: {flattened}")


print("\n" + "=" * 65)
print(">>> PART 3: VECTORIZATION & BROADCASTING <<<")
print("=" * 65)

# Vectorization: Performing operations on all elements without explicit loops
salaries = np.array([30000, 45000, 60000, 80000])
print(f"• Base Salaries: {salaries}")

# Applying a 10% bonus across all salaries in a vectorized operation
updated_salaries = salaries * 1.10
print(f"• Salaries after 10% Bonus: {updated_salaries}")

# Element-wise arithmetic between two arrays of identical shape
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print(f"• Array a + b: {a + b}")
print(f"• Array a * b: {a * b}")

# Broadcasting: Performing arithmetic between arrays of different compatible shapes
grid = np.zeros((3, 3))
row_to_add = np.array([1, 2, 3])
broadcasted_result = grid + row_to_add
print(f"\n• Broadcasting (3x3 Zeros + [1, 2, 3]):\n{broadcasted_result}")


print("\n" + "=" * 65)
print(">>> PART 4: STATISTICAL & MATHEMATICAL FUNCTIONS <<<")
print("=" * 65)

marks = np.array([45, 67, 89, 92, 55, 76, 88, 95, 34, 70])
print(f"• Student Marks: {marks}")

print(f"• Minimum Marks : {np.min(marks)}")
print(f"• Maximum Marks : {np.max(marks)} (Index: {np.argmax(marks)})")
print(f"• Mean (Average): {np.mean(marks):.2f}")
print(f"• Median Marks  : {np.median(marks)}")
print(f"• Standard Dev  : {np.std(marks):.2f}")
print(f"• Sum of Marks  : {np.sum(marks)}")

# Row-wise and column-wise aggregations (axis=0 for columns, axis=1 for rows)
data_grid = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(f"\n• Grid:\n{data_grid}")
print(f"  - Column-wise Sum (axis=0): {np.sum(data_grid, axis=0)}")
print(f"  - Row-wise Sum    (axis=1): {np.sum(data_grid, axis=1)}")


print("\n" + "=" * 65)
print(">>> PART 5: BOOLEAN INDEXING & CONDITIONAL FILTERING <<<")
print("=" * 65)

scores = np.array([32, 45, 78, 90, 22, 65, 84, 55])
print(f"• Scores: {scores}")

# Boolean conditional check (Generates a boolean mask)
pass_mask = scores >= 40
print(f"• Boolean Mask (Score >= 40): {pass_mask}")

# Filtering: Returns only elements where mask evaluates to True
passed_scores = scores[scores >= 40]
print(f"• Passed Students Scores: {passed_scores}")

# Compound condition filtering (& for AND, | for OR)
first_class = scores[(scores >= 60) & (scores <= 90)]
print(f"• First Class Scores (60 to 90): {first_class}")

# np.where(condition, value_if_true, value_if_false)
result_labels = np.where(scores >= 40, "Pass", "Fail")
print(f"• Result Labels (np.where): {result_labels}")


print("\n" + "=" * 65)
print(">>> PART 6: ADVANCED ARRAY MANIPULATION (STACKING & SPLITTING) <<<")
print("=" * 65)
# Concept: Joining multiple arrays (stacking) or dividing an array into parts (splitting).
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Vertical Stacking (Row upon row)
v_stack = np.vstack((arr1, arr2))
print(f"• Vertical Stack (vstack):\n{v_stack}")

# Horizontal Stacking (Column beside column)
h_stack = np.hstack((arr1, arr2))
print(f"• Horizontal Stack (hstack): {h_stack}")

# Splitting array into equal partitions
split_arr = np.split(h_stack, 2)
print(f"• Array Split into 2 parts:\n  Part 1: {split_arr[0]}\n  Part 2: {split_arr[1]}")


print("\n" + "=" * 65)
print(">>> PART 7: LINEAR ALGEBRA (LINALG) <<<")
print("=" * 65)
# Concept: Matrix multiplication (dot product) and determinants in scientific computing.
mat_a = np.array([[1, 2], [3, 4]])
mat_b = np.array([[5, 6], [7, 8]])

# Dot Product (Matrix Multiplication - Row by Column)
dot_product = np.dot(mat_a, mat_b)
print(f"• Dot Product of A and B:\n{dot_product}")

# Determinant of Matrix A (ad - bc for 2x2 matrix)
determinant = np.linalg.det(mat_a)
print(f"• Determinant of Matrix A: {determinant:.2f}")


print("\n" + "=" * 65)
print(">>> PART 8: RANDOM DATA GENERATION <<<")
print("=" * 65)
# Concept: Generating random values, arrays, and distributions for testing and simulation.

# Generate 5 random float values between 0 and 1
rand_floats = np.random.rand(5)
print(f"• Random Floats (0 to 1): {rand_floats}")

# Generate 3x3 array of random integers between 10 and 50
rand_ints = np.random.randint(10, 50, size=(3, 3))
print(f"• Random Integers (10 to 50, 3x3 Matrix):\n{rand_ints}")


print("\n" + "=" * 65)
print(">>> TOPIC 05 (NUMPY MASTER GUIDE) COMPLETED! <<<")
print("=" * 65)
