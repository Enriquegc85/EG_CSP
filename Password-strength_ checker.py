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
if characters == True:
    score += 1
if uppercase == True:
    score += 1
if lowercase == True:
    score += 1
if number == True:
    score += 1
if symbol == True:
    score += 1

print(f"At least 8 characters: {characters}")
print(f"Has an uppercase letter: {uppercase}")
print(f"Has a lowercase letter: {lowercase}")
print(f"Has a number: {number}")
print(f"Has a symbol: {symbol}")
print(f"Password strength score: {score}")

if score == 5:
    print("Your password is very strong.")
if score == 4:
    print("Your password is strong.")
if score == 3:
    print("Your password is moderate.")
if score == 2:
    print("Your password is weak.")
if score == 1:
    print("Your password is very weak.")


print("Suggestions:")

if characters == False:
    print("Add at least 8 characters.")

if uppercase == False:
    print("Add an uppercase letter.")

if lowercase == False:
    print("Add a lowercase letter.")

if number == False:
    print("Add a number.")

if symbol == False:
    print("Add a symbol.")