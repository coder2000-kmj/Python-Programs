#This is a python program to reverse an integer
def reverse(n):
    d=0
    rev=0
    while n>0:
        d=n%10 #a variable to store single digit of reversed number in each iteration
        n=n//10 #to store the remaining number
        rev=(rev*10)+d #core logic to add the digits 
    return rev
x=int(input("Enter the number to be reversed"))
r=reverse(x)
print(r)
