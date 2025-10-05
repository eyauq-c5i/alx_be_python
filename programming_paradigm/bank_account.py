class BankAccount:
    """
    A simple class to represent a bank account, demonstrating basic OOP principles.
    """
    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount with an optional starting balance.
        :param initial_balance: The starting amount in the account (defaults to 0).
        """
        
        self._account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds funds to the account balance.
        :param amount: The amount to deposit.
        """
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deducts funds from the account balance if sufficient funds are available.
        :param amount: The amount to withdraw.
        :return: True if the withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
            
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        # Using .2f for standard currency display
        print(f"Current Balance: ${self._account_balance:.2f}")

# End of bank_account.py