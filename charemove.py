def removecha(str):
    str1=""
    str=input("Enter your string")
    s=list(str)
    N=int(input("Enter the number of charactars you wanna remove"))
    for j in range(N):
            n=int(input("Enter the index"))
            s.pop(n)
    
    for i in s:
        str1+=i
    print(str1)
removecha(str)
    
    
