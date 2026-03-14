
expenses = []

while True:
    print("\n1 Add Expense")
    print("2 Show Expenses")
    print("3 Exit")

    choice = input("Choose option: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append((item, amount))

    elif choice == "2":
        total = 0
        for item, amount in expenses:
            print(item, amount)
            total += amount
        print("Total:", total)
    elif choice == "3":
        break