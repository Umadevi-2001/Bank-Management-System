import sqlite3

# Database connection
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    acc_no INTEGER PRIMARY KEY,
    name TEXT,
    balance REAL,
    acc_type TEXT
)
""")
conn.commit()


class Bank:
    def __init__(self, name, acc_no, balance, acc_type):
        self.name = name
        self.__acc_no = acc_no
        self.__balance = balance
        self.acc_type = acc_type

    def save_to_db(self):
        cursor.execute("INSERT INTO accounts VALUES (?, ?, ?, ?)",
                       (self.__acc_no, self.name, self.__balance, self.acc_type))
        conn.commit()

    def show_details(self):
        print("Name:", self.name)
        print("Account Number:", self.__acc_no)
        print("Account Type:", self.acc_type)
        print("Available Balance:", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            cursor.execute("UPDATE accounts SET balance=? WHERE acc_no=?",
                           (self.__balance, self.__acc_no))
            conn.commit()
            print("Deposit Successful")
            print("New Balance:", self.__balance)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            cursor.execute("UPDATE accounts SET balance=? WHERE acc_no=?",
                           (self.__balance, self.__acc_no))
            conn.commit()
            print("Withdrawal Successful")
            print("Remaining Balance:", self.__balance)
        else:
            print("Insufficient Balance")


# Menu system
while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        acc_no = int(input("Enter account number: "))
        balance = float(input("Enter initial balance: "))
        acc_type = input("Enter account type: ")

        obj = Bank(name, acc_no, balance, acc_type)
        obj.save_to_db()
        print("Account created successfully!")

    elif choice == 2:
        acc_no = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))

        cursor.execute("SELECT * FROM accounts WHERE acc_no=?", (acc_no,))
        data = cursor.fetchone()

        if data:
            obj = Bank(data[1], data[0], data[2], data[3])
            obj.deposit(amount)
        else:
            print("Account not found")

    elif choice == 3:
        acc_no = int(input("Enter account number: "))
        amount = float(input("Enter withdraw amount: "))

        cursor.execute("SELECT * FROM accounts WHERE acc_no=?", (acc_no,))
        data = cursor.fetchone()

        if data:
            obj = Bank(data[1], data[0], data[2], data[3])
            obj.withdraw(amount)
        else:
            print("Account not found")

    elif choice == 4:
        acc_no = int(input("Enter account number: "))

        cursor.execute("SELECT * FROM accounts WHERE acc_no=?", (acc_no,))
        data = cursor.fetchone()

        if data:
            obj = Bank(data[1], data[0], data[2], data[3])
            obj.show_details()
        else:
            print("Account not found")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
