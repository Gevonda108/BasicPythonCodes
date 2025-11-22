import time
import random

while True:

    print()
    print("======================================")
    print("Welcome to CALCULATOR made from python")
    print("======================================")
    time.sleep(1)
    print()
    print("Select operation -\n"
                "1. Add\n"
                "2. Subtract\n"
                "3. Multiply\n"
                "4. Divide\n"
                "5. Modulus\n"
                "6. Random Number between two numbers\n"
                "7. Round a number\n"
                "8. Power of a number\n"
                "9. Floor Division\n"
                "10. Exit")
    print()
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")



    print()

    print()

    if choice == "1":
        Num1 = int(input("Enter your first Number:"))
        Num2 = int(input("Enter your second Number:"))
        print(Num1 + Num2)

    elif choice == "2":
        Num1 = int(input("Enter your first Number:"))
        Num2 = int(input("Enter your second Number:"))
        print(Num1 - Num2)

    elif choice == "3":
        Num1 = int(input("Enter your first Number:"))
        Num2 = int(input("Enter your second Number:"))
        print(Num1 * Num2)

    elif choice == "4":
        Num1 = int(input("Enter your first Number:"))
        Num2 = int(input("Enter your second Number:"))
        print(Num1 / Num2)

    elif choice == "5":
        Num1 = int(input("Enter your first Number:"))
        Num2 = int(input("Enter your second Number:"))
        print(Num1 %  Num2)

    elif choice == "6":
        Num1 = int(input("Enter your first Number:"))
        Num2 = int(input("Enter your second Number:"))
        print(random.randint(Num1,Num2))

    elif choice == "7":
        Num1 = float(input("Enter your first Number:"))
        Num2 = float(input("Enter your second Number:"))
        print()
        Q1 = input("what arithmetic Operator do you want to use:")
        if Q1 == "+":
                result = Num1 + Num2
        elif Q1 == "-":
                result = Num1 - Num2
        elif Q1 == "*":
                result = Num1 * Num2
        elif Q1 == "/":
                result = Num1 / Num2
        elif Q1 == "%":
                result = Num1 % Num2
        print()
        decimal_places = int(input("How many decimal places do you want to round to? "))
        print()
        rounded_result = round(result, decimal_places)
        print("Result before being Rounded: ", result)
        time.sleep(1)
        print("=======================================")
        time.sleep(2)
        print("Here is your ROUNDED result:", rounded_result)
   
    elif choice == "8":
        base = float(input("Enter the base number: "))
        exponent = float(input("Enter the exponent: "))
        result = pow(base, exponent)  # or result = base ** exponent
        print("Result:", result)

    elif choice == "9":
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        result = num1 // num2
        print("Result:", result)

    else:
         break
      




