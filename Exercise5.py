def getdate():
    import datetime
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1 for exercise 2 for food\n"))
        if c==1:
            value = input("Type here\n")
            with open("harry_ex.txt", "a") as f:
                f.write(str([getdate()]) + ":" + value + "\n")
            print("successfully written")
        elif c==2:
            value = input("Type here\n")
            with open("harry_food.txt", "a") as f:
                f.write(str([getdate()]) + ":" + value + "\n")
            print("successfully written")
    elif k==2:
        c=int(input("Enter 1 for exercise 2 for food\n"))
        if c==1:
            value = input("Type here\n")
            with open("rohan_ex.txt", "a") as f:
                f.write(str([getdate()]) + ":" + value + "\n")
            print("successfully written")
        elif c==2:
            value = input("Type here\n")
            with open("rohan_food.txt", "a") as f:
                f.write(str([getdate()]) + ":" + value + "\n")
            print("successfully written")
    elif k==3:
        c=int(input("Enter 1 for exercise 2 for food\n"))
        if c==1:
            value = input("Type here\n")
            with open("hammad_ex.txt", "a") as f:
                f.write(str([getdate()]) + ":" + value + "\n")
            print("successfully written")
        elif c==2:
            value = input("Type here\n")
            with open("hammad_food.txt", "a") as f:
                f.write(str([getdate()]) + ":" + value + "\n")
            print("successfully written")
    else:
        print("Please enter vallid input")
def retrive(k):
    if k==1:
        c=int(input("Enter 1 for exercise 2 for food\n"))
        if c==1:
            with open("harry_ex.txt") as f:
                print(f.readlines(),end="")
        elif c==2:
            with open("harry_food.txt")as f:
                print(f.readlines(),end="")
    elif k==2:
        c=int(input("Enter 1 for exercise 2 for food\n"))
        if c==1:
            with open("rohan_ex.txt") as f:
                print(f.readlines(),end="")
        elif c==2:
            with open("rohan_food.txt")as f:
                print(f.readlines(),end="")
    elif k==3:
        c=int(input("Enter 1 for exercise 2 for food\n"))
        if c==1:
            with open("hammad_ex.txt") as f:
                print(f.readlines(),end="")
        elif c==2:
            with open("hammad_food.txt")as f:
                print(f.readlines(),end="")
    else:
        print("Please enter vallid input")


print("Welcome To Health Management\n")
d=int(input("Enter 1 for LOG 2 for RETRIVE\n"))
if d==1:
    b = int(input("Enter your choice\n 1.for HARRY\n 2.for ROHAN\n 3.for HAMMAD\n"))
    take(b)
elif d==2:
    b = int(input("Enter your choice\n 1.for HARRY\n 2.for ROHAN\n 3.for HAMMAD\n"))
    retrive(b)
else:
    print("Please enter vallid input")

