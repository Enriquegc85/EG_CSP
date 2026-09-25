#EG, number guessing game

import random

max_attempts = 6
low = 1
high = 100

number = random.randint(low, high)
print(f"Guess a number between {low} and {high}. You have {max_attempts} attempts.")

for max_attempts in range (1, max_attempts  + 1):
    guess = int(input(f"guess #{max_attempts}: "))
    if guess == number:
        print(f"You Guessed it in {max_attempts}")
    elif guess > number:
        print("Too high")
    if guess < number:
        print("Too low")
else:
    print(f"You're out of guesses! The number was {number}.")