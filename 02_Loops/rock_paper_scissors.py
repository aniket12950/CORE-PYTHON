

import random

choices = ["rock", "paper", "scissors"]

computer_choice = random.choice(choices)

user_choice = input("Enter rock, paper, or scissors: ").lower()

print("Computer choice:", computer_choice)

if user_choice == computer_choice:
    print("It's a Tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You Win!")
else:
    print("Computer Wins!")
