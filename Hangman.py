#EG, hangman game yayayaya
import random
with open("hangman.txt", "r") as file:
    word = file.read().splitlines()
secret_word = random.choice(word).lower()

