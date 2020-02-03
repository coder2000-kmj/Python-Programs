# recursive
from typing import List

warebank: List[int] = [0]
def show(index=0):
    if index < len(warebank):
        print(warebank[index])
        index += 1
        show(index)
    else:
        return
def add(count, fee, start=0, end=10):
    global decide
    if start < end:
        decide = input("What do you wish to do")
        if decide == "withdraw":
            count += 1
            amt=int(input("Tell us money wish to take: "))
            if amt>=warebank[start]:
                warebank.append(0)
            else:
                warebank.append(warebank[start]-amt)

            #start += 1

        elif decide == "deposit":
            amt=int(input("Enter the amount"))
            warebank.append(warebank[start] + amt)
            #start+=1


        else:
            print("check the amount later")
        start += 1
        if count > 5:
            fee += 20
            print("The remaining amount is", warebank[start] - fee)
        add(count, fee, start, end)


    else:
        return
add(count=0,fee=0)
show()

