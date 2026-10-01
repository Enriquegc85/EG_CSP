#EG, cipher program
choices = ""
while choices not in ['E', 'D']:
    choices = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").strip().upper()
    if choices not in ['E', 'D']:
        print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")
message = input("Enter your message: ")
shift = int(input("Enter a shift amount: "))

for char in message:
    if char.isalpha():
        shift_base = ord('A') if char.isupper() else ord('a')
        if choices == 'E':
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            print(encrypted_char, end='')
        elif choices == 'D':
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            print(decrypted_char, end='')
    else:
        print(char, end='')
print()
