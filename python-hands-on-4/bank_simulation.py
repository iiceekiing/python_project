import time

print("""
....................................................................

                WELCOME TO PAWA BANK Inc. 🏦 💱
....................................................................

Select any option below to perform an operation:

1. Create Account
2. Withdrawal
3. Transfer
4. Deposit
5. Paybill
6. History
7. Exit

""")

# ------------------ DATABASE ---------------------
users_db = {}   # user_name: {details}
transactions = []  # log all transactions
logged_in_user = None
user_balance = {}

# ------------------ MAIN MENU ---------------------
while True:
    try:
        choice = int(input("Select option: "))
    except ValueError:
        print("Invalid input! Enter a number from 1 to 7.\n")
        continue

    # ----------- CREATE ACCOUNT -----------
    if choice == 1:
        print("\nFill in the form below to create your account.")
        print("....................................................................")
        surName = input("Surname: ").strip()
        firstName = input("Firstname: ").strip()
        userName = input("Username (unique): ").strip()

        if userName in users_db:
            print("Username already taken. Try again.\n")
            continue

        try:
            createPin = int(input("Create PIN (digits only): "))
            confirmPin = int(input("Confirm your PIN: "))
        except ValueError:
            print("Invalid PIN format. Must be digits.\n")
            continue

        if createPin != confirmPin:
            print("PIN mismatch ❌ 🚫. Please try again.\n")
            continue

        # Save account
        users_db[userName] = {
            "firstName": firstName,
            "surName": surName,
            "pin": createPin
        }
        user_balance[userName] = 0
        transactions.append(f"Account created for {userName}")
        logged_in_user = userName

        print(f"\n✅ Account created successfully for {userName.upper()}!\n")

    # ----------- WITHDRAWAL -----------
    elif choice == 2:
        if not logged_in_user:
            print("⚠️ You must create an account or login first.\n")
            continue
        try:
            amount = int(input("Enter withdrawal amount: "))
            if amount <= 0:
                raise ValueError
        except ValueError:
            print("Invalid amount.\n")
            continue

        if user_balance[logged_in_user] >= amount:
            user_balance[logged_in_user] -= amount
            transactions.append(f"{logged_in_user} withdrew ₦{amount}")
            print(f"✅ You withdrew ₦{amount}. Current Balance: ₦{user_balance[logged_in_user]}")
        else:
            print("❌ Insufficient balance.\n")

    # ----------- TRANSFER -----------
    elif choice == 3:
        if not logged_in_user:
            print("⚠️ You must create an account or login first.\n")
            continue
        recipient = input("Enter recipient username: ").strip()
        if recipient not in users_db:
            print("❌ Recipient not found.\n")
            continue

        try:
            amount = int(input("Enter amount to transfer: "))
            if amount <= 0:
                raise ValueError
        except ValueError:
            print("Invalid amount.\n")
            continue

        if user_balance[logged_in_user] >= amount:
            user_balance[logged_in_user] -= amount
            user_balance[recipient] += amount
            transactions.append(f"{logged_in_user} transferred ₦{amount} to {recipient}")
            print(f"✅ Transfer successful. New Balance: ₦{user_balance[logged_in_user]}")
        else:
            print("❌ Insufficient balance.\n")

    # ----------- DEPOSIT -----------
    elif choice == 4:
        if not logged_in_user:
            print("⚠️ You must create an account or login first.\n")
            continue
        try:
            amount = int(input("Enter amount to deposit: "))
            if amount <= 0:
                raise ValueError
        except ValueError:
            print("Invalid amount.\n")
            continue

        user_balance[logged_in_user] += amount
        transactions.append(f"{logged_in_user} deposited ₦{amount}")
        print(f"✅ ₦{amount} deposited successfully. New Balance: ₦{user_balance[logged_in_user]}")

    # ----------- PAY BILL -----------
    elif choice == 5:
        if not logged_in_user:
            print("⚠️ You must create an account or login first.\n")
            continue
        bill_type = input("Enter bill type (e.g., NEPA, Internet): ").strip()
        try:
            amount = int(input(f"Enter amount to pay for {bill_type}: "))
        except ValueError:
            print("Invalid amount.\n")
            continue

        if user_balance[logged_in_user] >= amount:
            user_balance[logged_in_user] -= amount
            transactions.append(f"{logged_in_user} paid ₦{amount} for {bill_type}")
            print(f"✅ You paid ₦{amount} for {bill_type}. Remaining Balance: ₦{user_balance[logged_in_user]}")
        else:
            print("❌ Insufficient funds.\n")

    # ----------- VIEW HISTORY -----------
    elif choice == 6:
        if not logged_in_user:
            print("⚠️ You must create an account or login first.\n")
            continue
        print(f"\n📜 Transaction History for {logged_in_user}:\n")
        for tx in transactions:
            if logged_in_user in tx:
                print("•", tx)
        print()

    # ----------- EXIT -----------
    elif choice == 7:
        print("\nThanks for banking with PAWA BANK Inc. 💰\n")
        break

    else:
        print("❌ Invalid option! Enter a number from 1 to 7.\n")

    # Display Menu Again
    print("""
....................................................................

Select another option:

1. Create Account
2. Withdrawal
3. Transfer
4. Deposit
5. Paybill
6. History
7. Exit

""")

