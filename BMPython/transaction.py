from datetime import datetime

class Transaction:
    def __init__(self):
        self.transactions = []

    def log_transaction(self, acc_number, transaction_type, amount):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = f"{timestamp} - Account: {acc_number}, Type: {transaction_type}, Amount: {amount}"
        self.transactions.append(transaction)

    def view_transactions(self, acc_number):
        account_transactions = []
        for transaction in self.transactions:
            if f"Account: {acc_number}" in transaction:
                account_transactions.append(transaction)
        return account_transactions
