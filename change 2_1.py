***Implement a class called BankAccount that represents a bank account. The class should have private
attributes for account number, account holder name, and account balance. Include methods to
deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the
BankAccount class and test the deposit and withdrawal functionality.***
class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      return f"Deposited ${amount}. New balance: ${self.__account_balance}"
    else:
      return "Invalid deposit amount. Please deposit a positive amount."

  def withdraw(self, amount):
    if 0 < amount <= self.__account_balance:
      self.__account_balance -= amount
      return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
    elif amount > self.__account_balance:
      return "Insufficient funds. Cannot withdraw that amount."
    else:
      return "Invalid withdrawal amount. Please withdraw a positive amount."

  def display_balance(self):
    return f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}"


# Test the BankAccount class
if __name__ == "__main__":
  # Create an instance of BankAccount
  my_account = BankAccount("12345", "John Doe", 1000.0)

  # Deposit money
  print(my_account.deposit(
      500))  # Should print "Deposited $500. New balance: $1500"

  # Withdraw money
  print(my_account.withdraw(
      200))  # Should print "Withdrew $200. New balance: $1300"

  # Attempt to withdraw more money than available
  print(my_account.withdraw(
      1500))  # Should print "Insufficient funds. Cannot withdraw that amount."

  # Attempt to deposit a negative amount
  print(
      my_account.deposit(-100)
  )  # Should print "Invalid deposit amount. Please deposit a positive amount."

  # Display the account balance
  print(my_account.display_balance()
        )  # Should print "Account Balance for John Doe: $1300"
