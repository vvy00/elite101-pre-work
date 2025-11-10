print("Welcome to the Bank Chatbot 🏦💰!")
name = input("What is your name? ")
print("Hello " + name + "!, I am here to help with your banking services. ")

balance = 0

print("How can I help you today?")
print("\nPlease select an option down below from the list by entering the number: ")

print("1. Open a new account")
print("2. Learn about our loan options")
print("3. Find out about our hours and location")
print("4. Check your bank account balance") # new feature
print("5. Make a deposit") # new feature
print("6. Exit the conversation to speak with live agent")

choice = input("Enter your choice (1-6): ")

if choice == "1":
    print("\nWe offer Checking, Savings, and Student Accounts. Each comes with online banking access. Would you like me to further explain them?")
elif choice == "2":
    print("\nWe provide personal loans, auto loans, and home loans. Interest rates can vary. You can apply online or schedule an appointment.")
elif choice == "3":
    print("\nOur main location is at 123 Main St. We are open from 8 AM - 10 PM Monday through Sunday.")
elif choice == "4":
    print(f"\nYour current bank account balance is: ${balance:.2f}")
elif choice =="5":
    deposit = input("Enter the amount of money you want to deposit: $")
    try:
        deposit_amount = float(deposit)
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"You have sucessfully deposited ${deposit_amount:.2f} to your account. New balance: {balance:.2f}")
        else:
            print("Please enter a positive amount")
    except ValueError:
        print("Invalid amount. Please enter a number.")
elif choice == "6":
    print("\nConnecting you with a live agent now... Thank you for visiting!")
else:
    print("Not an option. Please restart again and choose an option (1-4).")


# You are working for a bank/financial institution/credit 
# card company and you need to create a chatbot that 
# will help new customers choose what kind of account 
# they want and help get them started signing up