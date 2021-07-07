f=open("pavi.txt","r")
content=f.read()
print(content)
f.close()

f=open("pavi.txt","r")
content=f.read(3)
print(content)
content=f.read(3)
print(content)
f.close()

# for line reading by using for loop
'''f=open("pavi.txt","rt")
for line in f:
    print(line,end="")'''

#read file line by using readline funcion
f=open("pavi.txt","r")
print(f.readline(),end="")
print(f.readline())

#using readlines(),this function print statement by creating a list
f=open("pavi.txt")
print(f.readlines())

