print("\n Welcome to Basic Chatbot")
print("Type 'bye' to exit the chat.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hi! Nice to meet you.")

    elif user_input == "how are you":
        print("Bot: I'm fine, thanks for asking.")

    elif user_input == "your name":
        print("Bot: I am a simple Python chatbot.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")