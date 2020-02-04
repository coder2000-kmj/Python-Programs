from array import *
arr=array('i',[4,2,6,7,2,5])
lst=list(arr)
lst.sort()
min=lst[0]
smin=lst[1]
if min==smin:
    min=lst[2]
    smin=lst[3]
hai=arr.index(smin)
for i in range(len(arr)):
    if arr[i]==min:
        temp=arr[i]
        arr[i]=smin
        arr[hai]=temp
    else:
        continue
print(arr)





