print("Welcome to the retail store Chatbot!")
name = input("What is your name? ")
age = input("Hello " + name + ", how old are you? ")

print("How can I help you today?")
print("\nPlease select an option down below from the list by entering the number: ")

print("1. Place Holder for Option 1")
print("2. Place Holder for Option 2")
print("3. Place Holder for Option 3")
print("4. Exit the conversation to speak with live agent")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("\nThe hours are from 8AM - 10PM Monday through Sunday.")
elif choice == "2":
    print("\nWe are located at this address 123 Main St.")
elif choice == "3":
    print("\nWe have these products available...")
elif choice == "4":
    print("\nConnecting you with a live agent now.")
else:
    print("Not an option. Please restart again and choose an option (1-4).")
