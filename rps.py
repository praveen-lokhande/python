from random import  randint
t=["rock","Paper","Scissors"]
computer=t[randint(0,2)]
player=False
while player==False:
    player=input("Rock,Paper,scissors")
    if player==computer:
        print("Tie!")
    elif player=="Rock":
        if computer=="paper":
            print("You lose!",computer,"covers",player)
        else:
            print("You win!",player,"smashes",computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("Thats not a vallid play.check your speeling!")
    player=False
    computer=t[randint(0,2)]

