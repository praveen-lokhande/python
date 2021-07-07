#using seek() and tell() in Files
f=open("pavi2.txt","r+")
f.seek(0)
f.write("Welcome to code world\n")
f.write("Thank you\n")
f.write("Art")
print(f.read())
print(f.tell())
f.close()