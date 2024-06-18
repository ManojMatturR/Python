from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_number, acc_holder):
        if acc_number not in self.accounts:
            self.accounts[acc_number] = Account(acc_number, acc_holder)
            return True
        else:
            print(f"Account creation failed. Account number {acc_number} already exists.")
            return False

    def get_account(self, acc_number):
        return self.accounts.get(acc_number)

    def remove_account(self, acc_number):
        if acc_number in self.accounts:
            del self.accounts[acc_number]
            return True
        return False

    def get_all_accounts(self):
        return self.accounts.values()

    def transfer(self, acc_number_from, acc_number_to, amount):
        account_from = self.get_account(acc_number_from)
        account_to = self.get_account(acc_number_to)

        if account_from and account_to:
            if account_from.withdraw(amount):
                if account_to.deposit(amount):
                    return True
                else:
                    # Rollback the withdrawal if deposit fails
                    account_from.deposit(amount)
                    return False
            else:
                return False
        else:
            return False
