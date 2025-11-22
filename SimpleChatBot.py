import time
import random

print("==========================================")
print("Welcome to the Chat Bot made from python")
print("==========================================")
time.sleep(2)
print("""
────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████──██████─██████████████─██████████████─██████████████───██████████████─██████████████─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██──██░░██─██░░██████░░██─██████░░██████─██░░██████░░██───██░░██████░░██─██████░░██████─
─██░░██─────────██░░██──██░░██─██░░██──██░░██─────██░░██─────██░░██──██░░██───██░░██──██░░██─────██░░██─────
─██░░██─────────██░░██████░░██─██░░██████░░██─────██░░██─────██░░██████░░████─██░░██──██░░██─────██░░██─────
─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─────██░░██─────██░░░░░░░░░░░░██─██░░██──██░░██─────██░░██─────
─██░░██─────────██░░██████░░██─██░░██████░░██─────██░░██─────██░░████████░░██─██░░██──██░░██─────██░░██─────
─██░░██─────────██░░██──██░░██─██░░██──██░░██─────██░░██─────██░░██────██░░██─██░░██──██░░██─────██░░██─────
─██░░██████████─██░░██──██░░██─██░░██──██░░██─────██░░██─────██░░████████░░██─██░░██████░░██─────██░░██─────
─██░░░░░░░░░░██─██░░██──██░░██─██░░██──██░░██─────██░░██─────██░░░░░░░░░░░░██─██░░░░░░░░░░██─────██░░██─────
─██████████████─██████──██████─██████──██████─────██████─────████████████████─██████████████─────██████─────
────────────────────────────────────────────────────────────────────────────────────────────────────────────""")
print("==========================================")
time.sleep(3)
print("preparing to chat with ChatBot!")
time.sleep(2)
print("===========================================")
time.sleep(1)
print("Tip: Type commands or help to see a list of commands you can use.")
time.sleep(1)
print("===========================================")
time.sleep(2)

while True:
    user_input = input("You: ")
    time.sleep(1)
    if "hello" in user_input.lower():
        print("ChatBot: Hi there! How can I help you today?")
    elif "how are you" in user_input.lower():
        print("ChatBot: I'm just a program, but thanks for asking!")
    elif "bye" in user_input.lower():
        print("ChatBot: Goodbye! Have a great day!")
        break
    elif "time" in user_input.lower():
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"ChatBot: The current time is {current_time}.")
    elif "date" in user_input.lower():
        current_date = time.strftime("%Y-%m-%d", time.localtime())
        print(f"ChatBot: Today's date is {current_date}.")
    elif "help" in user_input.lower():
        print("ChatBot: You can ask me about the time, date, or ask me to tell you a joke!")
    elif "weather" in user_input.lower():
        print("ChatBot: I'm not connected to the internet, so I can't provide weather updates.")
        print("ChatBot: But I hope it's a nice day where you are!")
    elif "name" in user_input.lower():
        print("ChatBot: I'm ChatBot, your friendly assistant!")
    elif "rename" in user_input.lower():
        new_name = input("ChatBot: What would you like to rename me to? ")
        print(f"ChatBot: From now on, you can call me {new_name}!")
    elif "thank you" in user_input.lower():
        print("ChatBot: You're welcome! If you have more questions, feel free to ask.")
    elif "song" in user_input.lower():
        print("ChatBot: I can't play songs, but I can recommend you to listen to 'Imagine' by John Lennon!")
    elif "motivate me" in user_input.lower():
        print("ChatBot: Believe in yourself! You can achieve anything you set your mind to.")
    elif "quote" in user_input.lower():
        print("ChatBot: 'The only way to do great work is to love what you do.' - Steve Jobs")
    elif "fact" in user_input.lower():
        print("ChatBot: Did you know? Honey never spoils. Archaeologists have found edible honey in ancient Egyptian tombs!")
    elif "joke" in user_input.lower() or "jokes" in user_input.lower():
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why did the bicycle fall over? Because it was two-tired!"
        ]
        print("ChatBot:", random.choice(jokes))
    elif user_input.lower() in ["exit", "quit", "stop"] :
        print("ChatBot: Exiting the chat. Goodbye!")
        break
    elif user_input.strip() == "":
        print("ChatBot: Please say something so we can chat!")
    elif len(user_input) > 200:
        print("ChatBot: That's quite a long message! Could you please be more concise?")
    elif any(char.isdigit() for char in user_input):
        print("ChatBot: I see you included numbers in your message!")
    elif user_input.isupper():
        print("ChatBot: No need to shout! I'm here to help.")
    elif "compliment me" in user_input.lower():
        compliments = [
            "You're doing a great job!",
            "You have a fantastic sense of humor!",
            "Your creativity is inspiring!"
        ]
        print("ChatBot:", random.choice(compliments))
    elif user_input.lower().startswith("spell "):
        word_to_spell = user_input[6:].strip()
        if word_to_spell:
            spelled_out = ' '.join(list(word_to_spell))
            print(f"ChatBot: The spelling of '{word_to_spell}' is: {spelled_out}")
    
        else:
            print("ChatBot: Please provide a word to spell.")
    elif "commands" in user_input.lower():

        print("ChatBot: Here are some commands you can use:")
        print("- hello")
        print("- how are you")
        print("- time")
        print("- date")
        print("- help")
        print("- weather")
        print("- name")
        print("- rename")
        print("- thank you")
        print("- song")
        print("- motivate me")
        print("- quote")
        print("- fact")
        print("- joke or jokes")
        print("- compliment me")
        print("- spell <word>")
        print("- exit, quit, or stop")
        print("- commands or help")


    else:
        print("ChatBot: I'm sorry, I don't understand that.")