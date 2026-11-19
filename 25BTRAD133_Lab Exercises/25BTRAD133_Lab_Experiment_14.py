
# BANK ACCOUNT SYSTEM USING OOP

class BankAccount:

    # Constructor
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid deposit amount!")

    # Withdrawal method
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print("Amount withdrawn successfully!")

    # Balance enquiry method
    def check_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance: Rs.", self.__balance)


# Main program

name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

if balance < 0:
    print("Initial balance cannot be negative!")
else:
    account = BankAccount(name, balance)

    while True:
        print("\n===== BANK ACCOUNT SYSTEM =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Enquiry")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            print("Thank you for using the Bank Account System!")
            break

        else:
            print("Invalid choice! Please try again.")
