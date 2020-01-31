def cross(str,len):
    for i in range(0,len):
        j=len-i-1
        for k in range(0,len):
            if k==i or k==j:
                print(str[k],end=" ")
            else:
                print(end=" ")
        print(" ")

str="android"
len=len(str)
cross(str,len)
