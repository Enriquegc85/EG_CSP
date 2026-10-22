#EG, fixed code :)
age_input = input("Enter your age: ")

if not age_input.isnumeric():
    print("Invalid age: Please enter a whole number using digits only.")
else:
    age = int(age_input)
    matinee = input("Is this a matinee? (yes/no): ").lower()

    if age <= 4:
        price = 0
    elif age <= 12:
        price = 8
    elif age <= 64:
        price = 12
    else:
        price = 9

    if matinee == "yes":
        price = price - 3

    if price < 0:
        price = 0

    print(f"Ticket price: ${price}.00")
