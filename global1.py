# a=20 #Global variable
# def func1(n):
#     global  a
#     m=10 # Local variable
#     print(a+m)
#     print(n,"i have printed")
#
# func1("yes")

x=89
def harry():
    x=20
    def rohan():
        global x
        x=88
    print("before calling rohan",x)
    rohan()
    print("After calling rohan",x)
harry()
print(x)