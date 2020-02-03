from array import *
a = array('i', [1,2,3,5,7,3,2,4,6,4,20,25,20])
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
x=int(input("Enter the number"))
for item in range(len(a2)):
    if a2[item]%x==0:
        print(a2[item])
    else:
        continue