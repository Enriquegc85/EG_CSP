#EG, hangman yayyayayayayayayayayyayayayayyaayayayayayayayayyayayayayyayayayayayyayayayayayyy
import random
def show_word():
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display


def show_hangman():
    stages = [
        """
  +---+
  |   |
      |
      |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
        """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
    ]
    print(stages[wrong_guesses])


with open("words.txt", "r") as file:
    word_text = file.read()
    if "," in word_text:
        words = word_text.split(",")
    else:
        words = word_text.split()

secret_word = random.choice(words).strip().upper()

with open("wincount_and_loosecount.txt", "r") as file:
    stats_data = file.read().split(",")
    wins = int(stats_data[0])
    losses = int(stats_data[1])

print(f"Win/loose counts: Wins: {wins}, Losses: {losses}")

guessed_letters = []
wrong_guesses = 0
won = False

while wrong_guesses < 6:
    show_hangman()
    print("Word: " + show_word())
    print("Guessed letters:", guessed_letters)
    print("Wrong guesses remaining:", 6 - wrong_guesses)

    guess = input("Guess a letter buddy -_-: ").strip().upper()

    if len(guess) != 1 or not guess.isalpha():
        print(
            "Invalid! Stop joking around before Ms.Larose slimes you out buddy, you will be dealt with. Please enter one single letter."
        )
        continue

    if guess in guessed_letters:
        print("You already guessed that letter dummy >;( !")
        continue

    guessed_letters += [guess]

    if guess in secret_word:
        print("good i guess...", guess, "is in the word")
    else:
        wrong_guesses += 1
        print("Sorry not sorry,", guess, "is not in the word HAHA.")

    won = True
    for letter in secret_word:
        if letter not in guessed_letters:
            won = False

    if won:
        break

if won:
    wins += 1
    print("oh! You guessed the word im surprised...i didint think you would actually do it, now go away >:( ):", secret_word)
else:
    losses += 1
    show_hangman()
    print("You lost heh! The word was:", secret_word)

with open("wincount_and_loosecount.txt", "w") as file:
    file.write(str(wins) + "," + str(losses))

print(f"Updated Win/Loose Counts - Wins: {wins}, Losses: {losses}")