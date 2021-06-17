cric=["bat","ball","stump","field"]
print(cric)
print(cric[::-1])

numbers=[2,4,3,6,9,11]
print(numbers)
numbers.sort()
print(numbers)
numbers.append(12)
print(numbers)
numbers.insert(0,1)
numbers.insert(4,5)
numbers.reverse()
print(numbers)
numbers=[]
numbers.append(5)
numbers.append(4)
numbers.append(3)
print(numbers)
numbers.remove(4)
print(numbers)

tp=("pavi","lokhande")
print(tp)
#tp.remove("pavi")  #in '()' we cannot change the objects called mutable method
                   #in '[]' we can change and add the objects called unmutable method

a=4
b=5
temp=a
a=b
b=temp
print(a,b)

a,b=b,a
print(a,b)

cric.extend(tp)
print(cric)
cric.sort()
print(cric)




