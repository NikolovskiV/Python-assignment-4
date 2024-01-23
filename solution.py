import csv
import uuid

# Define a class for BankAccount
class BankAccount:
    class InvalidDepositAmount(Exception):
        pass

    class InvalidWithdrawalAmount(Exception):
        pass

    def __init__(self, account_holder, initial_balance=0):
        self.account_number = str(uuid.uuid4())
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            raise self.InvalidDepositAmount("Invalid deposit amount. Amount must be greater than 0.")

        self.balance += amount
        self.transaction_history.append(("Deposit", amount))

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            raise self.InvalidWithdrawalAmount("Invalid withdrawal amount. Amount must be greater than 0 and not exceed the balance.")

        self.balance -= amount
        self.transaction_history.append(("Withdrawal", amount))

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")

    # def merge_account(self, other_account):
    #     raise NotImplementedError("Merge operation should be handled by the Bank class.")

    def merge_account(self, other_account, bank_instance):
        bank_instance.merge_accounts(self, other_account)

# Define a class for Bank
class Bank:
    def __init__(self, name, owner, location):
        self.name = name
        self.owner = owner
        self.location = location
        self.bank_accounts = []

    def create_bank_account(self, account_holder, initial_balance=0):
        new_account = BankAccount(account_holder, initial_balance)
        self.bank_accounts.append(new_account)
        return new_account

    def add_bank_account(self, account):
        if account not in self.bank_accounts:
            self.bank_accounts.append(account)
            print("Account added successfully.")
        else:
            print("Account already exists in the bank.")

    def close_bank_account(self, account):
        if account in self.bank_accounts:
            self.bank_accounts.remove(account)
            print("Account closed successfully.")
        else:
            print("Account not found.")

    def merge_accounts(self, source_account, destination_account):
        if source_account not in self.bank_accounts or destination_account not in self.bank_accounts:
            raise ValueError("Invalid source or destination account for merging.")

        destination_account.balance += source_account.balance
        destination_account.transaction_history.extend(source_account.transaction_history)

        self.close_bank_account(source_account)
        print("Accounts merged successfully.")

    def generate_accounts_report(self):
        with open("accounts_report.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Account Number", "Account Holder", "Balance", "Transaction History", "Bank Name"])
            for account in self.bank_accounts:
                writer.writerow([
                    account.account_number,
                    account.account_holder,
                    account.balance,
                    account.transaction_history,
                    self.name
                ])

    def get_accounts_for_person(self, person_identifier):
        person_accounts = [account for account in self.bank_accounts if account.account_holder == person_identifier]
        return person_accounts

# Define a class for Person
class Person:
    def __init__(self, first_name, last_name):
        self.person_id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.accounts = []

    def get_all_bank_accounts(self):
        return self.accounts

    def get_total_balance(self):
        return sum(account.balance for account in self.accounts)

    def __eq__(self, other):
        return isinstance(other, Person) and self.person_id == other.person_id

    def __ne__(self, other):
        return not self.__eq__(other)
