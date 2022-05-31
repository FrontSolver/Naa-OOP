import numpy as np
r = int(input("Enter the number of rows:")) 
c = int(input("Enter the number of columns:")) 
array1 = np.random.randint(10,size=(r,c))
print(array1)


r = int(input("Enter the number of rows:")) 
c = int(input("Enter the number of columns:")) 
array2 = np.random.randint(10,size=(r,c))
m3 = np.dot(array1,array2)
print(array2)

print(m3)

sumtotal = []

for i in range(len(array1)):
    for j in range(len(array1[0])):
        sumtotal = array1[i][j] + array2[i][j]
        print(sumtotal)
