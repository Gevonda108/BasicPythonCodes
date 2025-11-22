import time

print("=======================================")
print("Welcome to the Caesar Cipher Encoder/Decoder!")
print("""
░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░  ░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░
██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝  ██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝
██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗  ██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗
╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║  ╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║
░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝""")
print("=======================================")
time.sleep(3)
print("Preparing to encode or decode your messages securely.")
time.sleep(2)
print("=======================================")
time.sleep(2)
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encode':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decode':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result
while True:
    mode = input("Would you like to encode or decode a message? (type 'encode' or 'decode'): ").lower()
    if mode not in ['encode', 'decode']:
        print("Invalid option. Please type 'encode' or 'decode'.")
        continue
    text = input("Enter your message: ")
    shift = int(input("Enter the shift number (1-25): "))
    if shift < 1 or shift > 25:
        print("Invalid shift number. Please enter a number between 1 and 25.")
        continue
    processed_text = caesar_cipher(text, shift, mode)
    print("=======================================")
    time.sleep(2)
    print(f"The {mode}d message is: {processed_text}")
    print("=======================================")
    time.sleep(2)
    again = input("Would you like to encode/decode another message? (yes/no): ").lower()
    if again != 'yes':
        print("Exiting the Caesar Cipher Application. Goodbye!")
        break