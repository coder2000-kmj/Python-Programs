def firstN(N):
    i=0;j=0;flag=0
    print("The prime numbers are: ")
    for i in range(1,N+1):
        if i==0 or i==1: 
            continue
        flag=1
        for j in range(2,(i//2)+1):
            if i%j==0:
                flag=0
                break
        if flag==1:
            print(i,end=" ")
firstN(15)
