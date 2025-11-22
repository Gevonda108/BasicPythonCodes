import time

print("=======================================")
print("Welcome to the Quiz Application!")
print("=======================================")
time.sleep(3)
while True:
    print("\nSelect a quiz to take:")
    print("1. English Quiz")
    print("2. Math Quiz")
    print("3. Science Quiz")
    print("4. Coding Quiz")
    print("5. Ethical Hacking Quiz")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    time.sleep(2)
    print("preparing your quiz...")
    print("=======================================")
    time.sleep(2)
    if choice == '1':
        Q1 = input("What is the synonym of 'happy'?\nA. Sad\nB. Joyful\nC. Angry\nD. Tired\nYour answer: ")
        if Q1.lower() == 'b':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is B. Joyful")
        Q2 = input("Fill in the blank: She ___ to the store yesterday.\nA. Go\nB. Goes\nC. Went\nD. Going\nYour answer: ")
        if Q2.lower() == 'c':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is C. Went")
        Q3 = input("Choose the correct form: They have ___ their homework.\nA. Do\nB. Did\nC. Done\nD. Doing\nYour answer: ")
        if Q3.lower() == 'c':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is C. Done")
        Q4 = input("What is the antonym of 'difficult'?\nA. Hard\nB. Easy\nC. Tough\nD. Challenging\nYour answer: ")
        if Q4.lower() == 'b':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is B. Easy")
        Q5 = input("Select the correct sentence:\nA. He don't like ice cream.\nB. She doesn't likes ice cream.\nC. They doesn't like ice cream.\nD. She doesn't like ice cream.\nYour answer: ")
        if Q5.lower() == 'd':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is D. She doesn't like ice cream.")
        print("You have completed the English Quiz!")

    elif choice == '2':
        Q1 = input("What is 8 + 5?\nA. 12\nB. 13\nC. 14\nD. 15\nYour answer: ")
        if Q1.lower() == 'b':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is B. 13")
        Q2 = input("What is 15 - 7?\nA. 6\nB. 7\nC. 8\nD. 9\nYour answer: ")
        if Q2.lower() == 'c':
            print("Correct!")
        Q3 = input("What is 6 x 4?\nA. 20\nB. 22\nC. 24\nD. 26\nYour answer: ")
        if Q3.lower() == 'c':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is C. 24")
        Q4 = input("What is 20 ÷ 5?\nA. 3\nB. 4\nC. 5\nD. 6\nYour answer: ")
        if Q4.lower() == 'b':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is B. 4")
        Q5 = input("What is the square root of 81?\nA. 7\nB. 8\nC. 9\nD. 10\nYour answer: ")
        if Q5.lower() == 'c':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is C. 9")
        print("You have completed the Math Quiz!")
    elif choice == '3':
        Q1 = input("What planet is known as the Red Planet?\nA. Earth\nB. Mars\nC. Jupiter\nD. Venus\nYour answer: ")
        if Q1.lower() == 'b':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is B. Mars")
        Q2 = input("What is H2O commonly known as?\nA. Oxygen\nB. Hydrogen\nC. Water\nD. Carbon Dioxide\nYour answer: ")
        if Q2.lower() == 'c':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is C. Water")
        Q3 = input("What gas do plants absorb from the atmosphere?\nA. Oxygen\nB. Nitrogen\nC. Carbon Dioxide\nD. Helium\nYour answer: ")
        if Q3.lower() == 'c':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is C. Carbon Dioxide")
        Q4 = input("What part of the cell contains genetic material?\nA. Cytoplasm\nB. Nucleus\nC. Cell Membrane\nD. Mitochondria\nYour answer: ")
        if Q4.lower() == 'b':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is B. Nucleus")
        Q5 = input("What force keeps us grounded on Earth?\nA. Magnetism\nB. Friction\nC. Gravity\nD. Inertia\nYour answer: ")
        if Q5.lower() == 'c':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is C. Gravity")
        print("You have completed the Science Quiz!")
    elif choice == '4':
        Q1 = input("What does HTML stand for?\nA. Hyper Trainer Marking Language\nB. Hyper Text Markup Language\nC. Hyper Text Marketing Language\nD. Hyper Text Markup Leveler\nYour answer: ")
        if Q1.lower() == 'b':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is B. Hyper Text Markup Language")
        Q2 = input("Which language is primarily used for web development?\nA. Python\nB. Java\nC. JavaScript\nD. C++\nYour answer: ")
        if Q2.lower() == 'c':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is C. JavaScript")
        Q3 = input("What does CSS stand for?\nA. Computer Style Sheets\nB. Creative Style Sheets\nC. Cascading Style Sheets\nD. Colorful Style Sheets\nYour answer: ")
        if Q3.lower() == 'c':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is C. Cascading Style Sheets")
        Q4 = input("Which of the following is a Python web framework?\nA. Django\nB. React\nC. Angular\nD. Vue\nYour answer: ")
        if Q4.lower() == 'a':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is A. Django")
        Q5 = input("What symbol is used to denote comments in Python?\nA. //\nB. #\nC. <!-- -->\nD. /* */\nYour answer: ")
        if Q5.lower() == 'b':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is B. #")
        print("You have completed the Coding Quiz!")
    elif choice == '5':
        Q1 = input("What does 'phishing' refer to in cybersecurity?\nA. A type of malware\nB. A method of stealing sensitive information\nC. A firewall technique\nD. A password encryption method\nYour answer: ")
        if Q1.lower() == 'b':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is B. A method of stealing sensitive information")
        Q2 = input("What is a 'firewall' used for?\nA. To cool down a computer\nB. To block unauthorized access to a network\nC. To store data securely\nD. To speed up internet connection\nYour answer: ")
        if Q2.lower() == 'b':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is B. To block unauthorized access to a network")
        Q3 = input("What does 'VPN' stand for?\nA. Virtual Private Network\nB. Very Personal Network\nC. Virtual Public Network\nD. Verified Private Network\nYour answer: ")
        if Q3.lower() == 'a':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is A. Virtual Private Network")
        Q4 = input("What is 'two-factor authentication'?\nA. A method of encrypting data\nB. A security process requiring two forms of identification\nC. A type of malware\nD. A network protocol\nYour answer: ")
        if Q4.lower() == 'b':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is B. A security process requiring two forms of identification")
        Q5 = input("What is the purpose of 'ethical hacking'?\nA. To exploit security vulnerabilities for malicious purposes\nB. To test and improve security systems legally\nC. To create viruses\nD. To steal data\nYour answer: ")
        if Q5.lower() == 'b':
            print("Correct!")
        else:
            print("Incorrect. The correct answer is B. To test and improve security systems legally")
        print("You have completed the Ethical Hacking Quiz!")
    elif choice == '6':
        print("Thank you for using the Quiz Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
