import time

print("=======================================")
print("Welcome to the password strength checker!")
print("=======================================")
time.sleep(3)
password = input("Enter your password to check its strength(Out of 5): ")
print("=======================================")
time.sleep(2)
strength = 0
if len(password) >= 8:
    strength += 1
if any(char.islower() for char in password):
    strength += 1
if any(char.isupper() for char in password):
    strength += 1
if any(char.isdigit() for char in password):
    strength += 1
if any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
    strength += 1
print("Evaluating password strength...")
time.sleep(2)
print("=======================================")
time.sleep(2)
if strength == 5:
    print("Your password is Very Strong!", "Great job!")
elif strength == 4:
    print("Your password is Strong!", "try adding more special characters.")
elif strength == 3:
    print("Your password is Moderate.", "Consider adding uppercase letters, digits, or special characters.")
elif strength == 2:
    print("Your password is Weak." , "Try making it longer and adding a mix of character types.")
else:
    print("Your password is Very Weak!", "Make it longer and include a variety of character types.")