#EG, cipher program

def caesar_shift(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += shifted_char
        else:
            result += char
    return result


choices = ""
while choices not in ['E', 'D']:
    choices = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").strip().upper()
    if choices not in ['E', 'D']:
        print("Invalid! stop joking around. Please enter 'E' to encrypt or 'D' to decrypt.")

message = input("Enter your message: ")
shift = int(input("Enter a shift amount: "))

if choices == 'E':
    output = caesar_shift(message, shift)
    print(output)
else:
    output = caesar_shift(message, -shift)
    print(output)
