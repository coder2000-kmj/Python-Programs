'''
An IT company going to hire for following technology: java, python, script
of 20 people for the project among which 3 people were already booked in the odd positions
and 4 people in alternate even position,
now write a program to hire rest
'''
for i in range(1,21):
    skill=input("Enter your skill")
    if i<=6:
        print(i,"'st position already booked")
        continue
    if skill=='java' or skill=='python' or skill=='script':
        print("you're hired")
    else:
        print("Sorry better luck next time")
    

            
