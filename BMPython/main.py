from bank import Bank
from transaction import Transaction
from customer import Customer

def main():
    bank = Bank()
    transaction_log = Transaction()

    while True:
        print("\n===== Bank Management System =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer Funds")
        print("5. View Account Details")
        print("6. View Transaction Log")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            acc_number = input("Enter account number: ")
            acc_holder = input("Enter account holder name: ")
            if bank.create_account(acc_number, acc_holder):
                print("Account created successfully.")
            else:
                print("Account creation failed. Account number already exists or invalid input.")

        elif choice == '2':
            acc_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            account = bank.get_account(acc_number)
            if account:
                if account.deposit(amount):
                    transaction_log.log_transaction(acc_number, 'Deposit', amount)
                    print("Deposit successful.")
                else:
                    print("Deposit failed. Invalid amount.")
            else:
                print("Account not found.")

        elif choice == '3':
            acc_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            account = bank.get_account(acc_number)
            if account:
                if account.withdraw(amount):
                    transaction_log.log_transaction(acc_number, 'Withdrawal', amount)
                    print("Withdrawal successful.")
                else:
                    print("Withdrawal failed. Insufficient balance or invalid amount.")
            else:
                print("Account not found.")

        elif choice == '4':
            acc_number_from = input("Enter account number to transfer from: ")
            acc_number_to = input("Enter account number to transfer to: ")
            amount = float(input("Enter amount to transfer: "))
            if bank.transfer(acc_number_from, acc_number_to, amount):
                transaction_log.log_transaction(acc_number_from, 'Transfer Out', amount)
                transaction_log.log_transaction(acc_number_to, 'Transfer In', amount)
                print("Transfer successful.")
            else:
                print("Transfer failed. Check account numbers and balances.")

        elif choice == '5':
            acc_number = input("Enter account number: ")
            account = bank.get_account(acc_number)
            if account:
                print(account.account_info())
                print("Transaction History:")
                for transaction in transaction_log.view_transactions(acc_number):
                    print(transaction)
            else:
                print("Account not found.")

        elif choice == '6':
            print("\n===== Transaction Log =====")
            for transaction in transaction_log.transactions:
                print(transaction)

        elif choice == '7':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
