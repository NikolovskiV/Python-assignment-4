import csv
import uuid

# Define a class for BankAccount
# BankAccount class: Manages individual bank accounts, allowing deposits, withdrawals, balance retrieval, and merging of accounts belonging to the same person.
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        # Initialize attributes for a bank account
        self.account_number = str(uuid.uuid4())  # Generate a unique account number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []  # Keep track of transactions

    def deposit(self, amount):
        # Allow the account holder to deposit a specified amount into their account
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(("Deposit", amount))
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        # Allow the account holder to withdraw a specified amount if they have sufficient funds
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(("Withdrawal", amount))
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        # Return the current balance of the account
        return self.balance

    def display_account_info(self):
        # Display account information, including account number, account holder, and balance
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")

    def merge_account(self, other_account):
        # Merge accounts if they belong to the same account holder
        if isinstance(other_account, BankAccount) and self.account_holder == other_account.account_holder:
            self.balance += other_account.balance
            self.transaction_history.extend(other_account.transaction_history)
            print("Accounts merged successfully.")
        else:
            print("Invalid account for merging.")

# Define a class for Bank
# Bank class: Represents a bank, allowing the creation, addition, and closure of bank accounts. It can also generate an accounts report and retrieve accounts for a specific person.
class Bank:
    def __init__(self, name, owner, location):
        # Initialize attributes for a bank
        self.name = name
        self.owner = owner
        self.location = location
        self.bank_accounts = []  # Keep track of bank accounts

    def create_bank_account(self, account_holder, initial_balance=0):
        # Create a new bank account and add it to the list of bank accounts
        new_account = BankAccount(account_holder, initial_balance)
        self.bank_accounts.append(new_account)
        return new_account

    def add_bank_account(self, account):
        # Add an existing BankAccount object to the bank
        if account not in self.bank_accounts:
            self.bank_accounts.append(account)
            print("Account added successfully.")
        else:
            print("Account already exists in the bank.")

    def close_bank_account(self, account):
        # Close and remove a BankAccount from the bank
        if account in self.bank_accounts:
            self.bank_accounts.remove(account)
            print("Account closed successfully.")
        else:
            print("Account not found.")

    def generate_accounts_report(self):
        # Generate a CSV report with relevant information for bank accounts
        with open("accounts_report.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Account Number", "Account Holder", "Balance"])
            for account in self.bank_accounts:
                writer.writerow([account.account_number, account.account_holder, account.balance])

    def get_accounts_for_person(self, person_identifier):
        # Return all BankAccounts for a given person or person identifier
        person_accounts = [account for account in self.bank_accounts if account.account_holder == person_identifier]
        return person_accounts

# Define a class for Person
# Person class: Represents an individual, keeping track of associated bank accounts and providing methods to get all accounts and total balance.
class Person:
    def __init__(self, first_name, last_name):
        # Initialize attributes for a person
        self.first_name = first_name
        self.last_name = last_name
        self.accounts = []  # Keep track of bank accounts for the person

    def get_all_bank_accounts(self):
        # Return all BankAccounts associated with the person
        return self.accounts

    def get_total_balance(self):
        # Return the total balance across all bank accounts for the person
        return sum(account.balance for account in self.accounts)

    def __eq__(self, other):
        # Implement equality check for two Person objects
        return isinstance(other, Person) and self.first_name == other.first_name and self.last_name == other.last_name

    def __ne__(self, other):
        # Implement inequality check for two Person objects
        return not self.__eq__(other)
