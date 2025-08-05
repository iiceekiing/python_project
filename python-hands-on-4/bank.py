import time

bal = 10000
notes = 1000
amount= int(input("Enter amount you wish to withdrawal: "))

if amount % notes == 0 and amount <= bal and amount > 0:
    print("Processing your transaction....")
    time.sleep(1)
    print(" ")
    debit = bal - amount
    balance = bal - debit
    print("Transaction Successful\n")
    time.sleep(1)
    print("you have been debited: ", balance)
    print(" ")
    print("your remaining balance is: ", debit)

elif amount % notes != 0  and amount <= bal:

    print("Can only dispence 1000 notes, please enter a valid amount")

elif amount > bal:
    time.sleep(1)
    print("Insufficient balance, please try again!")

elif amount < 0:
    time.sleep(1)
    print("Invalid amount, must be greater than 1000 NGN")
else:
    time.sleep(1)
    print("Invalid input!")
