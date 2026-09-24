# EG - Password Strength Checker

password = input("Enter a password: ")

characters = False
upercase = False
lowercase = False
number = False
symbol = False

for letter in password:
    if letter.isupper():
        upercase = True

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
    score = score + 1

if upercase:
    score = score + 1

if lowercase:
    score = score + 1

if number:
    score = score + 1

if symbol:
    score = score + 1

print("At least 8 characters:", characters)
print("Has an uppercase letter:", upercase)
print("Has a lowercase letter:", lowercase)
print("Has a number:", number)
print("Has a symbol:", symbol)

if score == 5:
    print("Your password strength is: Strong")

if score == 3 or score == 4:
    print("Your password strength is: Medium")

if score <= 2:
    print("Your password strength is: Weak")

if score < 5:
    print("To make it Strong, add:")

    if not characters:
        print("- At least 8 characters")

    if not upercase:
        print("- An uppercase letter")

    if not lowercase:
        print("- A number")

    if not number:
        print("- A number")

    if not symbol:
        print("- A symbol")