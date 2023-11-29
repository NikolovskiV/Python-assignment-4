
# Your code goes here

from solution import Bank, BankAccount, Person

def main():
    # Create a bank
    bank = Bank(name="Evil Bank Corp", owner="Commander Lambda", location="Secret Lair")

    # Create bank accounts
    account1 = bank.create_bank_account(account_holder="John Doe", initial_balance=1000)
    account2 = bank.create_bank_account(account_holder="Jane Doe", initial_balance=1500)

    # Perform transactions
    account1.deposit(1500)
    account2.withdraw(800)

    # Display account information
    account1.display_account_info()
    account2.display_account_info()

    # Merge accounts if they belong to the same person
    account3 = bank.create_bank_account(account_holder="John Doe", initial_balance=2000)
    account1.merge_account(account3)

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


if __name__ == "__main__":
    main()
