#a=3
#b=4
#print(sum((a,b)))

#Simple without argument function definng
def Func1():
    '''this function return some statement'''
    print("This Is My First Function")

Func1()

#with arguments function defining
def Func2(a,b):
    '''this function return sum of two numbers'''
    print("the sum of two numbers are",a+b)
Func2(5,5)


#doc string
def Func3(a,b):
    '''This function will return average of two numbers'''
    average=(a+b)//2
    return "Average of two numbers",average
v=Func3(8,8)
print(v)


Func1()
print(Func1.__doc__)

Func2(4,4)
print(Func2.__doc__)

v=Func3(5,5)
print(v)
print(Func3.__doc__)