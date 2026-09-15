#EG, Hello user assignment
while True:
    name = input("What is your name: ").strip().capitalize()
    if name.isnumeric():
        print("That is a number not a name!")
    else:
        break  
print(f"Hello {name} hope you have a great day!")