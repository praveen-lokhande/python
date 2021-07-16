#Lambda Functions  or anonymous Functions

# def add(a,b):
#     return a+b
# print(add(4,2))

add=lambda a,b: a+b
print(add(4,4))

minus=lambda x,y:x-y
print(minus(9,5))

a=[[4,8],[3,7],[2,6]]
a.sort(key=lambda x:x[1])
print(a)