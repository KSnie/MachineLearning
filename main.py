import numpy as np
#
# # arr1: [ 1  2  3  4  5  6  7  8  9 10]
# arr1 = np.arange(1,11)
# print(f"arr1: {arr1}")
#
# # arr2: [[0. 0. 0.]
# #  [0. 0. 0.]
# #  [0. 0. 0.]]
# arr2 = np.zeros((3,3))
# print(f"arr2: {arr2}")
#
# # arr3: [[1 1 1]
# #  [1 1 1]
# #  [1 1 1]]
# arr3 = np.ones((3,3), dtype=int)
# print(f"arr3: {arr3}")
#
# # arr4: [[1. 0. 0. 0. 0.]
# #  [0. 1. 0. 0. 0.]
# #  [0. 0. 1. 0. 0.]
# #  [0. 0. 0. 1. 0.]
# #  [0. 0. 0. 0. 1.]]
# arr4 = np.eye(5)
# print(f"arr4: {arr4}")
#
# # arr5: [0.01589469 0.55549448 0.59355799 0.59414788 0.73331069]
# arr5 = np.random.rand(5)
# print(f"arr5: {arr5}")
#
# # arr6: [[16 17 20]
# #  [19 15 13]
# #  [13 12 15]]
# arr6 = np.random.randint(1,21,(3,3))
# print(f"arr6: {arr6}")
#
# # arr7: [0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556
# #  0.66666667 0.77777778 0.88888889 1.        ]
# arr7 = np.linspace(0,1,10)
# print(f"arr7: {arr7}")
#
# # arr8: [1 3 5 7 9]
# py_list = [1,3,5,7,9]
# arr8 = np.array(py_list)
# print(f"arr8: {arr8}")

# # Question 1
# arr7 = np.linspace(10,20,5)
# print(f"arr7: {arr7}")
#
# # Question 2
# arr6 = np.linspace(1,25,25, dtype=int).reshape(5,5)
# sum_diag = np.sum(np.diag(arr6))
# print(f"arr6: {sum_diag}")
#
# arr6 = np.random.randint(1,21,(3,3))
# print(arr6)
# print(f"arr6: {arr6.shape}")
# print(f"arr6: {arr6.ndim}")
# print(f"arr6: {arr6.dtype}")
#
# arr11 =np.array([1,2,"hello"])
# print(arr11)
# print("Arr11",arr11.dtype)
#
# arr1 = np.arange(1,11)
# arr12 = arr1.reshape(2,5)
# print(arr12)
#
# arr13_flatten = arr12.flatten()
# arr13_ravel = arr12.ravel()
#
# print(f"Arr13_flatten",arr13_flatten)
# print(f"Arr13_ravel",arr13_ravel)
#
# arr14_orig = np.arange(12).reshape(4,3)
# arr14_transposed = arr14_orig.T
# print(f"arr14_orig",arr14_orig)
# print(f"arr14_transposed",arr14_transposed)
# print(f"arr14_transposed_shape",arr14_transposed.shape)

# MyAnswer = np.zeros((8,8))
# MyAnswer[1::2,::2] =1
# MyAnswer[::2,1::2] =1
# print(MyAnswer)

# print(np.full((3,3),7))
#
base_arr = np.arange(20).reshape(4,5)
# element = base_arr[2,3]
# print(element)
#
# row1 = base_arr[0,:]
# print(row1)
# col1 = base_arr[:,0]
# print(col1)
# # print(base_arr)

# sub_matrix = base_arr[:2,:2]
# print(sub_matrix)
# Create an array of random integers between 1 and 50
# Question = np.random.randint(1, 51, size=50)  # total 20 numbers
#
# # Reshape into 4 rows and 5 columns
# Q_reshape = Question.reshape(-1, 5)
#
# # Extract first 4 rows (optional, same shape here)
# Q_4x5 = Q_reshape[:4, :]
#
# # Extract the 3rd column (index 2)
# Q_col3 = Q_4x5[:, 2]
#
# print("Question array:\n", Q_4x5)
# print("Third column:\n", Q_col3)

# import numpy as np
#
# A = np.random.randint(1, 101, size=100)
# A[A < 50] = 0
# A[A >= 50 ] = -1
#
# print(A.reshape(10,10))

# print(10 % 2)  # Result odd number
# print(10 // 2) # คัวคูณ

# (0,0) (1,1) (2,2) (base_arr[[0,1,2],[0,1,2]])

# (base_arr[[0,1]] = base_arr[[1,0]])
# A = np.arange(25).reshape(5,5)
# # A[:,:1] = -1
# # A[:,-1] = -1
# A[:,[0,-1]] = -1
# # A[:1,:] = -1
# # A[-1,:] = -1
# A[[0,-1],:] = -1
# print(A)

#
# A = np.random.randint(1,100,(10,10))
# B = np.max(A)
# C = np.where(A == B)
# print(A[C[0]])
#
# A = np.arange(6).reshape(2,3)
# B = np.ones((2,3) ,dtype=int) * 5
# # print(A+B)
#
# C = np.arange(6).reshape(3,2)
# matrix_product = A @ C
#
# print(A)
# print(C)
# print(matrix_product)
#
# A = np.arange(6).reshape(3,2)
#
# total_sum = np.sum(A,axis=1)
# print(total_sum)

col_vec = np.array([[1],[2],[3]])
row_vec = np.array([10,20,30,40])
#
# [10,20,30,40] + 1
# [10,20,30,40] + 2
# [10,20,30,40] + 3

broadcasted_sum = col_vec + row_vec
print(col_vec)
print(row_vec)
print(broadcasted_sum)
