rows=int(input("Enter the number of rows\n"))
n=int(input("Enter a one or two\n"))
a=bool(n)
if a==True:
 for i in range(rows):
  for j in range(i+1):
   print("*",end="")
  print()
elif a==False:
 for i in range(rows,0,-1):
  for j in range(i):
   print("*",end="")
  print()

