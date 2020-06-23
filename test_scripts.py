import numpy as np

a=[]
a[1:10]=np.zeros(10, dtype=int)
i=0
while i<100:
    i=i+1
    a.append(i)

print(a[-10:-1])

b=np.zeros(10, dtype=int)
print(b)