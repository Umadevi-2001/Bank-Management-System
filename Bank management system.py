class Bank:
    def __init__(self, name, acc_no, balance, acc_type):
        self.name = name
        self.__acc_no = acc_no
        self.__balance = balance
        self.acc_type = acc_type

    def show_details(self):
        print("Name:", self.name)
        print("Account Number:", self.__acc_no)
        print("Account Type:", self.acc_type)
        print("Available Balance:", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit Successful")
            print("New Balance:", self.__balance)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal Successful")
            print("Remaining Balance:", self.__balance)
        else:
            print("Insufficient Balance")


# User Input
name = input("Enter account holder name: ")
acc_no = int(input("Enter account number: "))
balance = int(input("Enter balance: "))
acc_type = input("Enter account type: ")

deposit_amount = int(input("Enter deposit amount: "))
withdraw_amount = int(input("Enter withdraw amount: "))

obj = Bank(name, acc_no, balance, acc_type)

obj.show_details()
obj.deposit(deposit_amount)
obj.withdraw(withdraw_amount)
