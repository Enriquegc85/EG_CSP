#EG, Password Strength Checker



password = input("Enter a password: ")

charecters = False
upercase = False
lowercase = False
number = False 
symbol = False

for letter in password:
    if letter.isupper():
        upercase = True
    elif letter.islower():
        lowercase = True
    elif letter.isnumeric():
        number = True
    else:
        symbol = True
        characters = True
    if len(password) < 8:
        characters = False

if upercase and lowercase and number and symbol and characters:
    print("Your password is strong")
if upercase and lowercase and number and symbol and not characters:
    print("Your password is medium")
if upercase and lowercase and number and not symbol and not characters:
    print("Your password is weak")
