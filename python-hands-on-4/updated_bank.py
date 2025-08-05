import time

print("""
....................................................................

                  WELCOME TO PAWA BANK Inc. 🏦  💱
....................................................................

select any option below to perform an operation:

1. Create Account
2. Withdrawal
3. Transfer
4. Deposit
5. Paybill
6. History
7. Exit

""")

database = []
balance = 0
choice = int(input("Select option: "))

if choice >= 1 and choice <= 7:
    if choice == 1:
        print("\nFill in the form below to create your account")
        print("\n....................................................................")
        surName = input("\nSurname:  ")
        print("\n....................................................................")
        firstName = input("\nFirstname:  ")
        print("\n....................................................................")
        userName = input("\nUsername:  ")
        print("\n....................................................................")
        createPin = int(input("\nPin:  "))
        print("\n....................................................................")
        comfirmPin = int(input("Confirm your Pin:  "))
        print("\n....................................................................")

        if comfirmPin == createPin:
            users = {
                "surname": surName,
                "firstname": firstName,
                "username": userName,
                "pin": createPin
            }
            print(f"\nAccount created successfully!")
            print("\nWelcome to Pawa Bank!", userName.upper())

            database.append(users)

            option = int(input("""
Select option
1. Deposit
2. Account Details
3. Check balance
4. Exit
>> """))

            if option >= 1 and option <= 4:
                if option == 1:
                    deposit = int(input("\nEnter amount you wish to deposit:\n "))
                    balance += deposit
                    print(f"\nDeposit of ₦{deposit} successful. Current Balance: ₦{balance}")
                elif option == 2:
                    print("Fetching account details.....")
                    time.sleep(1)
                    print(database)
                elif option == 3:
                    print(f"Your current balance is: ₦{balance}")
                elif option == 4:
                    print("Thank you for banking with us.")
        else:
            print("Pin doesn't match ❌ 🚫, please try again!...")

    elif choice == 2:
        amount = int(input("Enter withdrawal amount:  "))
        # Add logic here

