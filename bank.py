# recursive 
trans=[0]

def show(index=0):
    if index<len(trans):
        print(trans[index])
        index+=1;show(index)
    else:
        return

