print("Welcome to the Bank Chatbot 🏦💰!")
name = input("What is your name? ")

while True:
    age = input("How old are you? ")
    try:
        age = int(age)
        if age < 18:
            print("Since you are under 18, we recommend opening a Student or Youth Savings Account.")
        else:
            print("Great! You are eligible for all our account types, including Checking and Savings Accounts.")
        break
    except ValueError:
        print("That does not look like a valid age. Please enter a number.")

print("Hello " + name + "!, I am here to help with your banking services. ")

balance = 0

print("\nPlease select an option down below from the list by entering the number: ")

while True:
    print("\nHow can I help you today?")
    print("1. Open a new account")
    print("2. Learn about our loan options")
    print("3. Find out about our hours and location")
    print("4. Check your bank account balance") # new feature
    print("5. Make a deposit") # new feature
    print("6. Withdraw money") # new feature
    print("7. Speak to a live agent")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        print("\nWe offer the following accounts:")
        print("a. Checking Account")
        print("b. Savings Account")
        print("c. Student Account")
        account_choice = input("Which account would you like to open? (a-c): ").lower()

        if account_choice == "a":
            print("You chose Checking Account. It comes with a debit card and free bill pay.")
        elif account_choice == "b":
            print("You chose Savings Account. It earns monthly interest and has no fees.")
        elif account_choice == "c":
            print("You chose Student Account. Good choice for students who are under 18!")
        else:
            print("Invalid choice.")
    elif choice == "2":
        print("\nWe provide personal loans, auto loans, and home loans. Interest rates can vary. You can apply online or schedule an appointment.")
    elif choice == "3":
        print("\nOur main location is at 123 Main St. We are open from 8 AM - 10 PM Monday through Sunday.")
    elif choice == "4":
        print(f"\n{name}, your current bank account balance is: ${balance:.2f}")
    elif choice =="5":
        deposit = input("Enter the amount of money you want to deposit: $")
        try:
            deposit_amount = float(deposit)
            if deposit_amount > 0:
                balance += deposit_amount
                print(f"💰 You have successfully deposited ${deposit_amount:.2f} to your account. New balance: ${balance:.2f}")
            else:
                print("Please enter a positive amount")
        except ValueError:
            print("Invalid amount. Please enter a number.")
    elif choice == "6":
        withdraw = input("Enter the amount you want to withdraw: $")
        try:
            withdraw_amount = float(withdraw)
            if withdraw_amount > 0 and withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"💳 You have withdrawn ${withdraw_amount:.2f}. New balance: ${balance:.2f}")
            elif withdraw_amount > balance:
                print("⚠️ You have insufficient funds.")
            else:
                print("Please enter a positive amount.")
        except ValueError:
            print("Invalid amount. Please enter a number!")
    elif choice == "7":
        print("\n👋 Connecting you with a live agent now... Thank you for visiting!")
        break
    else:
        print("Not an option. Please choose a number between (1-7).")

# You are working for a bank/financial institution/credit 
# card company and you need to create a chatbot that 
# will help new customers choose what kind of account 
# they want and help get them started signing up