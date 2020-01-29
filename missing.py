'''
This is a program for finding the missing number in a series
provided the successive difference between elements in series
should be equal
'''
lst=[] #series of elements will be stored in this list
dif=[] #this list stores the difference between successive elements
x=int(input("Enter the Number of elements"))
for i in range(x): #first for loop is append all the elements entered into a list
    ele=int(input())
    lst.append(ele)
    '''
    second for loop is to store the successive differences of all the
    elements in a list
    '''
for j in range(len(lst)-1):  
    res=lst[j+1]-lst[j]
    dif.append(res)
    '''
    Third for loop is for finding which difference is out of order
    '''
for k in range(len(dif)-1):
    if dif[k+1]!=dif[k]:
        a=k+1
        st=dif[k+1]-dif[k]
        break
    else:
        continue
num=lst[a]+st
print("the missing number is:",str(num))
    
    

