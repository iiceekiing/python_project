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

if choice >=1 and choice <= 7:
    if choice == 1:
        users = {
            print("\nFill in the form below to createa your account")
            print("\n....................................................................")
            surName = input("\nSurname:  ")
            print("\n....................................................................")
            firstName = input("\nFirstname:  ")
            print("\n....................................................................")
            userName = input("\n Username:  ")
            print("\n....................................................................")
            createPin = int(input("\nPin:  "))
            print("\n....................................................................")
            comfirmPin = int(input("Confirm your Pin:  "))
            print("\n....................................................................")
        
            if comfirmPin == createPin:
                print(f"\naccount created successfully!")
                print("\nWelcome to Pawa Bank! ", userName.upper())
            database.append(users)
                option = int(input("""\nSelect option
                1. Deposit
                2. Account Details
                3. Check balance
                4. Exit
                                   """))
                if option >= 1 and option <= 4:
                    if option == 1:
                        deposit = int(input("\nEnter amount you wish to deposit:\n "))
                        balance += deposit
                elif option == 2:
                    print("fetching account details.....")
                    time.sleep(1)
                    print(database)
            else:
            print("Pin doesn't match ❌ 🚫, please try again!...")

        }
    elif choice == 2:
        amount = int(input("Enter withdrawal amount:  "))
        #if amount 
