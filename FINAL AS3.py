import tkinter as tk
from tkinter import messagebox

# Encapsulation: The BankAccount class encapsulates the account_number, account_name, and balance attributes.
# These attributes are private and can only be accessed through public methods.
class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
         # Encapsulation: The account_number, account_name, and balance attributes are private.
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    # Abstraction: The deposit method abstracts the process of adding money to the account.
    # It hides the complexity of the operation and provides a simple interface.
    def deposit(self, amount):
        # Encapsulation: The balance attribute is modified through the deposit method.
        self.balance += amount
        return self.balance

    # Abstraction: The withdraw method abstracts the process of removing money from the account.
    # It hides the complexity of the operation and provides a simple interface.
    def withdraw(self, amount):
        # Encapsulation: The balance attribute is modified through the withdraw method.
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

    # Abstraction: The get_balance method abstracts the process of retrieving the account balance.
    # It hides the complexity of the operation and provides a simple interface.
    def get_balance(self):
        # Encapsulation: The balance attribute is accessed through the get_balance method.
        return self.balance

# Composition: The BankingSystem class contains a collection of BankAccount objects.
class BankingSystem:
    def __init__(self):
        # Composition: The accounts attribute is a collection of BankAccount objects.
        self.accounts = {}

    # Polymorphism: The create_account method has the same name as the BankAccount class's __init__ method.
    # However, it has different behavior and is used to create a new BankAccount object in the BankingSystem.
    def create_account(self, account_number, account_name, initial_balance=0):
        # Encapsulation: The accounts attribute is modified through the create_account method.
        if account_number in self.accounts:
            return "Account already exists"
        self.accounts[account_number] = BankAccount(account_number, account_name, initial_balance)
        return "Account created successfully"

    # Polymorphism: The deposit method has the same name as the BankAccount class's deposit method.
    # However, it has different behavior and is used to deposit money into a BankAccount object in the BankingSystem.
    def deposit(self, account_number, amount):
        # Encapsulation: The accounts attribute is accessed through the deposit method.
        if account_number not in self.accounts:
            return "Account not found"
        return self.accounts[account_number].deposit(amount)

    # Polymorphism: The withdraw method has the same name as the BankAccount class's withdraw method.
    # However, it has different behavior and is used to withdraw money from a BankAccount object in the BankingSystem.
    def withdraw(self, account_number, amount):
        # Encapsulation: The accounts attribute is accessed through the withdraw method.
        if account_number not in self.accounts:
            return "Account not found"
        return self.accounts[account_number].withdraw(amount)

    # Polymorphism: The get_balance method has the same name as the BankAccount class's get_balance method.
    # However, it has different behavior and is used to retrieve the balance of a BankAccount object in the BankingSystem.
    def get_balance(self, account_number):
        # Encapsulation: The accounts attribute is accessed through the get_balance method.
        if account_number not in self.accounts:
            return "Account not found"
        return self.accounts[account_number].get_balance()

# Inheritance: The BankingSystemGUI class inherits the properties and behavior of the BankingSystem class.
class BankingSystemGUI:
    def __init__(self):
        # Inheritance: The BankingSystemGUI class inherits the BankingSystem class's properties and behavior.
        self.bank = BankingSystem()
        self.window = tk.Tk()
        self.window.title("Banking System")

        # The "Create account" frame
        self.create_account_frame = tk.Frame(self.window)
        self.create_account_frame.pack()
        tk.Label(self.create_account_frame, text="Create Account").pack()
        tk.Label(self.create_account_frame, text="Account Number:").pack()
        self.create_account_number_entry = tk.Entry(self.create_account_frame)
        self.create_account_number_entry.pack()
        tk.Label(self.create_account_frame, text="Account Name:").pack()
        self.create_account_name_entry = tk.Entry(self.create_account_frame)
        self.create_account_name_entry.pack()
        tk.Button(self.create_account_frame, text="Create Account", command=self.create_account).pack()

        # The "Deposit" frame
        self.deposit_frame = tk.Frame(self.window)
        self.deposit_frame.pack()
        tk.Label(self.deposit_frame, text="Deposit").pack()
        tk.Label(self.deposit_frame, text="Account Number:").pack()
        self.deposit_account_number_entry = tk.Entry(self.deposit_frame)
        self.deposit_account_number_entry.pack()
        tk.Label(self.deposit_frame, text="Amount:").pack()
        self.deposit_amount_entry = tk.Entry(self.deposit_frame)
        self.deposit_amount_entry.pack()
        tk.Button(self.deposit_frame, text="Deposit", command=self.deposit).pack()

        # The "Withdraw" frame
        self.withdraw_frame = tk.Frame(self.window)
        self.withdraw_frame.pack()
        tk.Label(self.withdraw_frame, text="Withdraw").pack()
        tk.Label(self.withdraw_frame, text="Account Number:").pack()
        self.withdraw_account_number_entry = tk.Entry(self.withdraw_frame)
        self.withdraw_account_number_entry.pack()
        tk.Label(self.withdraw_frame, text="Amount:").pack()
        self.withdraw_amount_entry = tk.Entry(self.withdraw_frame)
        self.withdraw_amount_entry.pack()
        tk.Button(self.withdraw_frame, text="Withdraw", command=self.withdraw).pack()

        # The "Check balance" frame
        self.check_balance_frame = tk.Frame(self.window)
        self.check_balance_frame.pack()
        tk.Label(self.check_balance_frame, text="Check Balance").pack()
        tk.Label(self.check_balance_frame, text="Account Number:").pack()
        self.check_balance_account_number_entry = tk.Entry(self.check_balance_frame)
        self.check_balance_account_number_entry.pack()
        tk.Button(self.check_balance_frame, text="Check Balance", command=self.check_balance).pack()

    def create_account(self):
        account_number = self.create_account_number_entry.get()
        account_name = self.create_account_name_entry.get()
        result = self.bank.create_account(account_number, account_name)
        messagebox.showinfo("Result", result)

    def deposit(self):
        account_number = self.deposit_account_number_entry.get()
        amount = float(self.deposit_amount_entry.get())
        result = self.bank.deposit(account_number, amount)
        messagebox.showinfo("Result", f"New balance: {result}")

    def withdraw(self):
        account_number = self.withdraw_account_number_entry.get()
        amount = float(self.withdraw_amount_entry.get())
        result = self.bank.withdraw(account_number, amount)
        if result == "Insufficient funds":
            messagebox.showerror("Error", result)
        else:
            messagebox.showinfo("Result", f"New balance: {result}")

    def check_balance(self):
        account_number = self.check_balance_account_number_entry.get()
        result = self.bank.get_balance(account_number)
        if result == "Account not found":
            messagebox.showerror("Error", result)
        else:
            messagebox.showinfo("Result", f"Balance: {result}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = BankingSystemGUI()
    gui.run()
    
print("https://github.com/DeathGod1198/HIT137-AS2")