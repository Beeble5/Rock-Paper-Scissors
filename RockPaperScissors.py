#!/bin/python3

from random import randint

player = input("rock (r), paper (p), or scissors (s)?")
print(player, "vs", end = " ")

chosen = randint(1,3)
#print(chosen)

if chosen == 1:
  computer = "r"
elif chosen == 2:
  computer = "p"
else:
  computer = "s"
  
print(computer)

if player == "r" and chosen == 1:
  print("Draw!")
elif player == "r" and chosen == 2:
  print("Computer wins!")
elif player == "r" and chosen == 3:
  print("Player wins!")
elif player == "p" and chosen == 1:
  print("Player wins!")
elif player == "p" and chosen == 2:
  print("Draw!")
elif player == "p" and chosen == 3:
  print("Computer wins!")
elif player == "s" and chosen == 1:
  print("Computer wins!")
elif player == "s" and chosen == 2:
  print("Player wins!")
else:
  print("Draw!")