class Account:
    def __init__(self, acc_number, acc_holder, balance=0.0):
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append((amount, 'Deposit'))
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append((amount, 'Withdrawal'))
            return True
        return False

    def get_balance(self):
        return self.balance

    def account_info(self):
        return f"Account Number: {self.acc_number}, Account Holder: {self.acc_holder}, Balance: {self.balance}"

    def get_transactions(self):
        return self.transactions
