Bank Account Management System

Overview
This project implements a Bank Account Management System with classes representing a Bank, Bank Accounts, and Persons. The system allows users to create bank accounts, perform transactions, close accounts, merge accounts, and generate account reports. The code is organized into three main classes: Bank, BankAccount, and Person.

Classes

1. Bank
   The Bank class represents a financial institution and provides functionality to manage bank accounts. It allows creating new accounts, adding existing accounts, closing accounts, merging accounts, and generating account reports.

2. BankAccount
   The BankAccount class represents an individual bank account. It supports operations such as deposits, withdrawals, checking the balance, displaying account information, and merging accounts. The merge operation is handled by the Bank class to ensure proper management of source and destination accounts.

3. Person
   The Person class represents an individual and is associated with one or more bank accounts. It has methods to retrieve all bank accounts associated with the person, calculate the total balance, and provide a unique identifier for comparison.

Usage
To use the system, create an instance of the Bank class and interact with it by creating accounts, performing transactions, closing accounts, and generating reports.

from solution import Bank, BankAccount, Person

# Create a bank

bank = Bank(name="Evil Bank Corp", owner="Commander Lambda", location="Secret Lair")

# Create bank accounts

account1 = bank.create_bank_account(account_holder="John Doe", initial_balance=1000)
account2 = bank.create_bank_account(account_holder="Jane Doe", initial_balance=1500)

# Perform transactions

account1.deposit(1500)
account2.withdraw(800)

# Merge accounts if they belong to the same person

account3 = bank.create_bank_account(account_holder="John Doe", initial_balance=2000)
account1.merge_account(account3, bank) # Pass the bank instance

# Add an existing account to the bank

bank.add_bank_account(account2)

# Close an account

bank.close_bank_account(account2)

# Generate accounts report

bank.generate_accounts_report()

# Get accounts for a person

person = Person(first_name="John", last_name="Doe")
person.accounts = [account1, account3]
person_accounts = bank.get_accounts_for_person(person_identifier=person)

# Print person's accounts

print(f"Accounts for {person.first_name} {person.last_name}:")
for account in person_accounts:
account.display_account_info()

# Display total balance for the person

print(f"Total balance for {person.first_name} {person.last_name}: ${person.get_total_balance()}")

Requirements

Python 3.x

Installation

Clone the repository and run the project using a Python interpreter.

git clone https://github.com/your-username/bank-account-management.git
cd bank-account-management
python3 verification.py
