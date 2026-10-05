#EG, hangman game yayayaya
import random
with open("words.txt", "r") as file:
    words = file.read().splitlines()
    words = random.choice(words)
content = file.read(",").split