import numpy as np


arr_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr_2d)

# element = arr_2d[1, 2]
# print(element)

# dim = arr_2d.ndim
# print(dim)

# arr_shape = arr_2d.shape # shape sa rreshta sa kolona jan
# print(arr_shape)

# arr_size = arr_2d.size
# print(arr_size)

# sub_arr = arr_2d[:2, :2] #2 rresht 2 colon
# print(sub_arr)

# sub_arr_3 = arr_2d[-4:, -4:]
# print(sub_arr_3)

# sub_arr_4 = arr_2d[:, ::2]
# print(sub_arr_4)

# total_sum = np.sum(arr_2d)  #mledh krejt numrat
# print(total_sum)

# mean = np.mean(arr_2d) #mesatarja e numrave pjestim
# print(mean)

# sum_cols = np.sum(arr_2d, axis=0)  #numri par reshti par me numrin e par rreshtit 2
# print(sum_cols)

# sum_rows = np.sum(arr_2d, axis=1)
# print(sum_rows)

reshaped_arr = arr_2d.reshape((5,2))
print(reshaped_arr)