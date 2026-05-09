balance = 5000

while True:
    print("\n1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = float(input("Enter amount: "))
        balance += amount
        print("Deposited Successfully")

    elif choice == 2:
        amount = float(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
            print("Withdraw Successful")
        else:
            print("Insufficient Balance")

    elif choice == 3:
        print("Balance =", balance)

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")