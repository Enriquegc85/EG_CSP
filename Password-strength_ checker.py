# EG - Password Strength Checker
password = input("Enter a password: ")

characters = False
uppercase = False
lowercase = False
number = False
symbol = False

for letter in password:
    if letter.isupper():
        uppercase = True
    if letter.islower():
        lowercase = True
    if letter.isnumeric():
        number = True
    if not letter.isalnum():
        symbol = True

if len(password) >= 8:
    characters = True

score = 0
if characters:
    score += 1
if uppercase:
    score += 1
if lowercase:
    score += 1
if number:
    score += 1
if symbol:
    score += 1

print(f"At least 8 characters: {characters}")
print(f"Has an uppercase letter: {uppercase}")
print(f"Has a lowercase letter: {lowercase}")
print(f"Has a number: {number}")
print(f"Has a symbol: {symbol}")
print(f"Password strength score: {score}")


if score == 5:
    print("Your password is Strong.")
elif score >= 3:
    print("Your password is Medium.")
else:
    print("Your password is Weak.")


if score != 5:
    print("Suggestions:")
    if not characters:
        print("Add at least 8 characters.")
    if not uppercase:
        print("Add an uppercase letter.")
    if not lowercase:
        print("Add a lowercase letter.")
    if not number:
        print("Add a number.")
    if not symbol:
        print("Add a symbol.")
