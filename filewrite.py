#writing a file
f=open("pavi2.txt","w")
f.write("welcome to coding world\n")
f.close()

#reading file
f=open("pavi2.txt","r")
print(f.read())
f.close()

#appending file (adding text)
f=open("pavi2.txt","a")
f.write("thank you\n")
f.close()

#read and write (both) file and charecters count
f=open("pavi2.txt","r+")
print(f.read())
a=f.write("art")
print(a)
f.close