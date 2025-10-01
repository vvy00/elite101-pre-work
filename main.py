print("Welcome to the Bank Chatbot!")
name = input("What is your name? ")
print("Hello " + name + "!, I am here to help with your banking services. ")

print("How can I help you today?")
print("\nPlease select an option down below from the list by entering the number: ")

print("1. Open a new account")
print("2. Learn about our loan options")
print("3. Find out about our hours and location")
print("4. Exit the conversation to speak with live agent")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("\nWe offer Checking, Savings, and Student Accounts. Each comes with online banking access. Would you like me to further explain them?")
elif choice == "2":
    print("\nWe provide personal loans, auto loans, and home loans. Interest rates can vary. You can apply online or schedule an appointment.")
elif choice == "3":
    print("\nOur main location is at 123 Main St. We are open from 8 AM - 10 PM Monday through Sunday.")
elif choice == "4":
    print("\nConnecting you with a live agent now... Thank you for visiting!")
else:
    print("Not an option. Please restart again and choose an option (1-4).")
