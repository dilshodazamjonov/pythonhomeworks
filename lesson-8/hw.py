import csv
import uuid
import os

# ## Model a Farm

# In this assignment, you’ll create a simplified model of a farm. As you work through this assignment, keep in mind that there are a number of correct answers.

# The focus of this assignment is less about the Python class syntax and more about software design in general, which is highly subjective. This assignment is intentionally left open-ended to encourage you to think about how you would organize your code into classes.

# Before you write any code, grab a pen and paper and sketch out a model of your farm, identifying classes, attributes, and methods. Think about inheritance. How can you prevent code duplication? Take the time to work through as many iterations as you feel are
# necessary.

# The actual requirements are open to interpretation, but try to adhere to these guidelines:

# 1. You should have at least four classes: the parent `Animal` class, and then at least three child animal classes that inherit from Animal.
# 2. Each class should have a few attributes and at least one method that models some behavior appropriate for a specific animal or all animals—such as walking, running, eating, sleeping, and so on.
# 3. Keep it simple. Utilize inheritance. Make sure you output details about the animals and their behaviors.
class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def walk(self):
        print(f"{self.name} is walking around the farm.")

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, sound="Woof")
        self.breed = breed

    def guard(self):
        print(f"{self.name} the {self.breed} is guarding the farm.")


class Cow(Animal):
    def __init__(self, name, age, milk_yield):
        super().__init__(name, age, sound="Moo")
        self.milk_yield = milk_yield  # liters/day

    def produce_milk(self):
        print(f"{self.name} produced {self.milk_yield} liters of milk today.")


class Chicken(Animal):
    def __init__(self, name, age, eggs_per_day):
        super().__init__(name, age, sound="Cluck")
        self.eggs_per_day = eggs_per_day

    def lay_eggs(self):
        print(f"{self.name} laid {self.eggs_per_day} eggs today.")


# Farm to manage animals
class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_all(self):
        for animal in self.animals:
            print(f"{animal.name} ({animal.__class__.__name__}) - Age: {animal.age}")

if __name__ == "__main__":
    farm = Farm()

    dog = Dog("Buddy", 5, "German Shepherd")
    cow = Cow("Bessie", 3, 20)
    chicken = Chicken("Clucky", 1, 5)

    farm.add_animal(dog)
    farm.add_animal(cow)
    farm.add_animal(chicken)

    farm.show_all()

    dog.guard()
    cow.produce_milk()
    chicken.lay_eggs()

    

# ---

# ## Build a Bank Application

# #### **Objective:**
# Develop a command-line banking application that allows users to perform basic banking operations like creating an account, depositing money, and withdrawing money. This will help you practice using object-oriented programming (OOP), file handling, and error handling in Python.


# ### **Tasks:**

# #### **Step 1: Define the Classes**
# 1. Create a class `Account` with attributes:
#    - `account_number`
#    - `name`
#    - `balance`

# 2. Create a class `Bank` to manage all accounts. It should have:
#    - A dictionary to store accounts (`accounts`).
#    - Methods for each operation:
#      - `create_account(name, initial_deposit)`
#      - `view_account(account_number)`
#      - `deposit(account_number, amount)`
#      - `withdraw(account_number, amount)`
#      - `save_to_file()` and `load_from_file()` (for file handling).


# #### **Step 2: Implement the Methods**
# 1. **Account Creation**
#    - Generate a unique `account_number`.
#    - Create an `Account` object and store it in the dictionary.
#    - Save account details to a file.

# 2. **View Account Details**
#    - Prompt the user to input their account number.
#    - Retrieve and display the account details if found; otherwise, show an error.

# 3. **Deposit Money**
#    - Prompt the user for their account number and deposit amount.
#    - Validate the amount and update the account balance.

# 4. **Withdraw Money**
#    - Prompt the user for their account number and withdrawal amount.
#    - Validate that the amount is less than or equal to the balance and update the account balance.

# 5. **File Handling**
#    - Use `save_to_file` to write account details to `accounts.txt`.
#    - Use `load_from_file` to load account details when the program starts.

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"Account({self.account_number}): {self.name}, Balance: {self.balance:.2f}"


class Bank:
    FILE_NAME = "accounts.csv"

    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = str(uuid.uuid4())[:8]  # collision-proof
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        return account_number

    def view_account(self, account_number):
        return str(self.accounts.get(account_number, "Account not found."))

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account and account.deposit(amount):
            self.save_to_file()
            return f"Deposited {amount}. New balance: {account.balance:.2f}"
        return "Deposit failed."

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account and account.withdraw(amount):
            self.save_to_file()
            return f"Withdrew {amount}. New balance: {account.balance:.2f}"
        return "Withdrawal failed."

    def save_to_file(self):
        with open(self.FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            for acc in self.accounts.values():
                writer.writerow([acc.account_number, acc.name, acc.balance])

    def load_from_file(self):
        if not os.path.exists(self.FILE_NAME):
            return
        with open(self.FILE_NAME, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    acc_num, name, balance = row
                    self.accounts[acc_num] = Account(acc_num, name, float(balance))


if __name__ == "__main__":
    bank = Bank()
    while True:
        print("\n1. Create Account\n2. View Account\n3. Deposit\n4. Withdraw\n5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            try:
                deposit = float(input("Enter initial deposit: "))
                acc_num = bank.create_account(name, deposit)
                print(f"Account created. Your number: {acc_num}")
            except ValueError:
                print("Invalid deposit amount.")
        elif choice == "2":
            acc_num = input("Enter account number: ")
            print(bank.view_account(acc_num))
        elif choice == "3":
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to deposit: "))
                print(bank.deposit(acc_num, amount))
            except ValueError:
                print("Invalid amount.")
        elif choice == "4":
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to withdraw: "))
                print(bank.withdraw(acc_num, amount))
            except ValueError:
                print("Invalid amount.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


# ---