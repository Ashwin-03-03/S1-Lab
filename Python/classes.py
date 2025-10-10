# WAP to create a bank account class

class BankAccount:
    def __init__(self, account_number, account_holder, balance = 0.0):
        
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):

        self.amount = amount
        self.balance += amount
    
    def withdrawal(self, amount):
        self.amount = amount
        if(amount > self.balance):
            print("Insufficient balance!")
        else:
            self.balance -= amount
    def showBalance(self):
        print(f"Your account balance is {self.balance}")

    def accountInfo(self):
        print(f"Account number: {self.account_number}")
        print(f"Account holder: {self.account_holder}")
        print(f"Account balance: {self.balance}")

""" jobin = BankAccount("123456", "Jobin Joshy", 100)
jobin.deposit(100)
jobin.showBalance()

account_number = input("Enter your account number: ")
account_holder = input("Enter your account holder: ")
amount = float(input("Enter the amount: "))
ashwin = BankAccount(account_number, account_holder, amount)
ashwin.showBalance() """

accounts = []
for i in range(5):
    print(f"Enter the details for user {i+1}: ")
    account_number = input("Enter account number: ")
    account_holder = input("Enter the name of the account holder: ")
    amount = float(input("Enter the amount: "))
    account = BankAccount(account_number, account_holder, amount)
    accounts.append(account)
print("\nAll accounts created successfully\n")

for acc in accounts:
    acc.accountInfo()

    