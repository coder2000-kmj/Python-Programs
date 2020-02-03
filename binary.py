#python program to convert the given integer into it's binary equivalent
num=int(input("Enter the decimal number"))
def bin(n):
    if n>1:
        bin(n//2)
    print(n%2,end="")
bin(num)
print()