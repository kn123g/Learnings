from numpy import *

mat1 = array([[1,2,3],[4,5,6],[7,8,9]])
mat2 = array([[1,2,3],[4,5,6],[7,8,9]])
array = array([[1,2,3],[4,5,6]])
arrdim = array.ndim
arrshape = array.shape
arraysize = array.size
flattenarray = array.flatten()
reshapearray=flattenarray.reshape(2,3)
newarr = arange(12)
reshape3DArray = newarr.reshape(2,2,3)

matrix1=matrix([[1,2,3],[4,5,6],[7,8,9]],int)
matrix2=matrix('1 2 3; 4 5 6; 7 8 9',int)


print("normal array :  ",array)
print("array dimension :  ",arrdim)
print("array shape :  ",arrshape)
print("array size :  ",arraysize)
print("flattenarray array :  ",flattenarray)
print("reshaped array  :  ",reshapearray)
print("new array :  ",newarr)
print("reshaped 3D Array :  ",reshape3DArray)
print("Addition of two matrix :  ",matrix1 + matrix2)
print("Mutliplication of two matrix :  ",matrix1 * matrix2)
print("Mutliplication of two matrix without matrix function :  ",mat1 * mat2)

#print(mat1.shape[0])
mat3=zeros((3,3),int)
for i in range(mat1.shape[0]) : 
    for j in range(mat1.shape[1]) : 
        mat3[i][j]=0;
        for k in range(mat1.shape[1]) :
            mat3[i][j] = mat3[i][j] + (mat1[i][k] * mat2[k][j])
print()
print("Normal Matrix Multiplication",mat3)

print(type(mat3))
print(type(matrix1))

        


