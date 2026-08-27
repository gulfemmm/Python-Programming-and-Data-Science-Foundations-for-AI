import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

# print("Addition: \n",A+B)
# print("Subtraction: \n",B-A)

C = 2*A
# print("Scalar Multiplication \n",C)

result =np.dot(A,C)
# print("Matrix Multiplication \n",result)

I = np.eye(5)
print("Identity Matrix \n",I)
