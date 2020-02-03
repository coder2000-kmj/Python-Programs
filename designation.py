des={"Kaushal":"RI","Robert":"Thalisthar","Jim":"VAO","Avinash":"VAO"}

print(des)
'''
for i in des:
    if des[i]=="VAO":
        des[i]="RI"
        print(i,des[i])
print(des)
'''

def repl(i=0):
    if des[i]=="VAO":
        des[i]="RI"
        i+=1
        repl(i)
    else:
        i+=1
        repl(i)    
repl()
    
            

