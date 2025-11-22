import time
import random

random_password = ""
print("=========================================")
print("Welcome to the Random Password Generator!")
print("=========================================")
time.sleep(1)
print()
length = int(input("Enter the length of the password you want to generate: "))
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
for i in range(length):
    random_password += random.choice(characters)
print("Generating your password...")
print("=======================================")
time.sleep(2)
print("=======================================")
time.sleep(2)
print()
print("Your generated password is:", random_password)