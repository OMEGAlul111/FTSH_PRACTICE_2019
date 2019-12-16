import numpy as np

print('введите n')
n=int(input())

print('введите вектор')
a0=int(input())
b0=int(input())

b=np.array([a0,b0])

for i in range(n):
    print('введите матрицу передачи')
    a00=int(input())
    a01=int(input())
    a10=int(input())
    a11=int(input())
    
    a=np.array([[a00,a01],[a10,a11]])
    
    
    b=a.dot(b)
    
    
print(b[0])
print(b[1])
