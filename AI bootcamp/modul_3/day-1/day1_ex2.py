import numpy as np

#Create matrix and vektor
M = np.array([[1,2,3],[4,5,6],[7,8,9]])
V = np.array([0,1,-1])

#Matrix-Vector multiplication
result = np.dot(M,V)
print("Matrix<-Vector multiplication: \n",result)