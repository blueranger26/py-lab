# Parent Class (BankAccount)
class BankAccount:
    def __init__(self, holder_name, initial_balance):
        self.holder_name = holder_name  # Name of the account holder
        self.balance = initial_balance  # Initial balance in the account
        print(f"Account created for {self.holder_name} with an initial balance of {self.balance}.")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
    
    def check_balance(self):
        print(f"Current balance: {self.balance}")
    
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


# Child Class (SavingsAccount) inherits from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, holder_name, initial_balance, interest_rate):
        # Call the constructor of the parent class (BankAccount)
        super().__init__(holder_name, initial_balance)
        self.interest_rate = interest_rate  # Interest rate for savings account
        print(f"Interest rate for {self.holder_name}'s savings account: {self.interest_rate}%")
    
    def apply_interest(self):
        """Apply interest to the account balance."""
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        print(f"Interest applied. New balance: {self.balance}")


# Get user input for the first account (Account 1)
holder_name1 = input("Enter your name (Account 1): ")
initial_balance1 = float(input(f"Enter the initial balance for {holder_name1}: "))
account1 = BankAccount(holder_name1, initial_balance1)

# Get user input for the second account (Savings Account)
holder_name2 = input("Enter the name for the savings account (Account 2): ")
initial_balance2 = float(input(f"Enter the initial balance for {holder_name2}: "))
interest_rate = float(input(f"Enter the interest rate for {holder_name2}: "))
savings_account = SavingsAccount(holder_name2, initial_balance2, interest_rate)

# Main Menu for user actions
while True:
    print("\n--- Bank Account Operations ---")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Transfer Money")
    print("5. Apply Interest (Savings Account only)")
    print("6. Exit")

    choice = input("Select an option (1-6): ")

    if choice == '1':
        # Deposit money into Account 1 (Bank Account)
        amount = float(input(f"Enter amount to deposit into {account1.holder_name}'s account: "))
        account1.deposit(amount)

    elif choice == '2':
        # Withdraw money from Account 1 (Bank Account)
        amount = float(input(f"Enter amount to withdraw from {account1.holder_name}'s account: "))
        account1.withdraw(amount)

    elif choice == '3':
        # Check balance of Account 1 (Bank Account)
        account1.check_balance()

    elif choice == '4':
        # Transfer money from Account 1 (Bank Account) to Savings Account
        amount = float(input(f"Enter amount to transfer from {account1.holder_name}'s account to {savings_account.holder_name}'s account: "))
        account1.transfer(savings_account, amount)

    elif choice == '5':
        # Apply interest for Savings Account
        savings_account.apply_interest()

    elif choice == '6':
        # Exit the program
        print("Thank you for using the bank system. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
