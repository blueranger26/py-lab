from abc import ABC, abstractmethod

# Define an interface (abstract base class)
class BankAccountInterface(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def check_balance(self):
        pass
    
    @abstractmethod
    def transfer(self, target_account, amount):
        pass


# BankAccount class implements the BankAccountInterface
class BankAccount(BankAccountInterface):
    def __init__(self, holder_name, initial_balance):
        self.holder_name = holder_name  # Name of the account holder
        self.balance = initial_balance  # Initial balance in the account
        print(f"Account created for {self.holder_name} with an initial balance of {self.balance}.")
    
    # Implement deposit method from BankAccountInterface
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    # Implement withdraw method from BankAccountInterface
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
    
    # Implement check_balance method from BankAccountInterface
    def check_balance(self):
        print(f"Current balance: {self.balance}")
    
    # Implement transfer method from BankAccountInterface
    def transfer(self, target_account, amount):
        if amount <= 0:
            print("Transfer amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds for transfer.")
        else:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transferred {amount} to {target_account.holder_name}. New balance: {self.balance}")
            print(f"{target_account.holder_name}'s new balance: {target_account.balance}")


# Get user input for the first account (Account 1)
holder_name1 = input("Enter your name (Account 1): ")
initial_balance1 = float(input(f"Enter the initial balance for {holder_name1}: "))
account1 = BankAccount(holder_name1, initial_balance1)

# Get user input for the second account (Account 2)
holder_name2 = input("Enter the name for the second account (Account 2): ")
initial_balance2 = float(input(f"Enter the initial balance for {holder_name2}: "))
account2 = BankAccount(holder_name2, initial_balance2)

# Main Menu for user actions
while True:
    print("\n--- Bank Account Operations ---")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Transfer Money")
    print("5. Exit")

    choice = input("Select an option (1-5): ")

    if choice == '1':
        # Deposit money
        amount = float(input(f"Enter amount to deposit into {account1.holder_name}'s account: "))
        account1.deposit(amount)

    elif choice == '2':
        # Withdraw money
        amount = float(input(f"Enter amount to withdraw from {account1.holder_name}'s account: "))
        account1.withdraw(amount)

    elif choice == '3':
        # Check balance
        account1.check_balance()

    elif choice == '4':
        # Transfer money to another account
        amount = float(input(f"Enter amount to transfer from {account1.holder_name}'s account to {account2.holder_name}'s account: "))
        account1.transfer(account2, amount)

    elif choice == '5':
        # Exit the program
        print("Thank you for using the bank system. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
