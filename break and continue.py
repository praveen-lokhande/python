'''i=0
while(True):
    if i+1<=5:
        i=i+1
        continue
    print(i,end=" ")
    if(i==50):
        break
    i=i+1'''
while(True):
    i=int(input("enter a number\n"))
    if(i>100):
        print("congrats you have enter greater than 100\n",i)
        break
    else:
        print("try again\n")
        continue