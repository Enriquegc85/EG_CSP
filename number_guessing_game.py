# EG, number guessing game
import random

max_attempts = 6
low = 1
high = 100

number = random.randint(low, high)
print(f"Guess a number between {low} and {high}. You have {max_attempts} attempts.")

guesses_taken = 0

while guesses_taken < max_attempts:
    guesses_taken = guesses_taken + 1
    
    guess = int(input(f"guess #{guesses_taken}: "))
    
    if guess == number:
        print(f"You Guessed it in {guesses_taken} attempts!")
        break
    elif guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")

if guess != number:
    print(f"You're out of guesses! The number was {number}.")
