from bank import *
def add(start=0,end=10):
    if start<end:
        trans.append(input("Enter credit/debit"))
        start+=1;add(start,end)
    else:
        return
def findNPut(start=0,end=len(trans),count=0,fee=0):
    if start<end:
        if trans[start]=="debit":
            count+=1
            if count>5:
                fee+=20
        start+=1;findNPut(start,end,count,fee)
    else:
        print("Charges for this month is: ",fee);return
print(trans)
add()
findNPut(0,len(trans));
