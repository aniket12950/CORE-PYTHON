# Number Guessing Game

import random

secret_number = random.randint(1, 50)
attempts = 0

print("Guess the number between 1 and 50")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
