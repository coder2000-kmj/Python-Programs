pd={400:"Sony",450:"sandisk",550:"hp",650:"kingston",750:"toshiba"}
price=0
print(pd)
def delete(start=0):
    price=int(input("Which price pendrive do you want to delete"))
    if pd.get(price,"This does not exist"):
        del pd[price]
        print(pd)
        start+=1
        if start>len(pd)-1:
            return
        delete()
    else:
        print("The price you selected does not exists")
        return
    delete()
delete()


            
    
