import numpy as np

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("original matrix: \n", matrix)

#Transpose
transpose = matrix.T
print("Transpose:\n",transpose)

another_matrix= np.array([[9,8,7],[6,5,4], [63,2,1]])
print("Addition: \n", matrix + another_matrix)
print("multiplication : \n", matrix * another_matrix)