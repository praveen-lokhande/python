n=18
a=1
print("Welcome to a guess game")
while(a<=9):
  b=int(input("Enter your guess:\n"))
  if(b<n):
   print("You are enter a low number:\n")
  elif(b>n):
   print("You are enter a higher number:\n")
  elif(b==n):
   print("YOU WON")
   print(a, "no of guesses you took to finish\n")
   break
  print(9 - a, "no of guesses are left")
  a=a+1
else:
   print("GAME OVER!....")