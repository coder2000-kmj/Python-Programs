def isprime(n,i=2):
    if n<=2:
        return True if n==2 else False
    if n%i==0:
        return False
    if i*i>n:
        return True
    return isprime(n,i+1)
n=int(input("Enter the initial Number"))
num=int(input("enter the number of prime numbers you want"))
count=1
while count<=num:
    if(isprime(n)):
        print(n)
        count+=1
        n+=1
    else:
        n+=1
