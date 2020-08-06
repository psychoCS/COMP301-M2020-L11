import numpy as np

#numbers = np.array([2, 3, 5, 7, 11])

#row1 = np.arange(1,5)
#row2 = np.arange(5,9)
#row3 = np.arange(9,13)
#row4 = np.arange(13,17)

matrix2 = []
colCount = 0

for row in range(5):
        matrix2.append(np.arange(1 + colCount,5 + colCount))
        colCount +=4

matrix2 = np.array(matrix2)

print(matrix2)

matrix =[[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16]]

#print(matrix)

multi = np.array(matrix)

#print (multi)

#print(multi.dtype)

#print(multi.ndim)

#print(multi.shape)

''' in columns
for row in multi:
    for col in row:
        print(col, end='\t')
    print()
'''

#for row in multi.flat:
#   print(row, end=' ')

matrix3 = np.arange(1,17).reshape(4,4)

print(matrix3)

matrix4 = np.arange(1,16).reshape(3,5)

print(matrix4)

print(matrix4.sum())