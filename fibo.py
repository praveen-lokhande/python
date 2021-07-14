#0 1 1 2 3 5 8 13
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
num=int(input("Engter a number\n"))
print("Fibonacci of",num,"is",fibonacci(num))

#0 1 1 2 3 5 8 13
def fibonacci1(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n+2)

number=(int(input("Enter a number")))
print(fibonacci1(number))
