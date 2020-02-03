#this program is partially correct
from array import *
a = array('i', [2, 4, 6, 8, 1, 2, 3, 4, 5, 6, 7, 8, 7, 10, 11, 12, 13, 14, 15, 16])
a1=list(a)
a2=[]
print(a1)
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
a2=Repeat(a1)
n=0
while n<len(a1):
    for i in range(len(a2)):
        if a1[i] == a2[i]:
            a1[i] = a[i + 1] + 10
            n+=1

        else:
            continue
    n+=1
print(a1)




