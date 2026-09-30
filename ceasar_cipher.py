#EG, cipher program
choices = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").strip().upper()
message = input("Enter your message: ")
shift = int(input("Enter a shift amount: "))

for char in message:
    
