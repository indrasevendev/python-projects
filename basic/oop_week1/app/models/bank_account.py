from app.exceptions.insufficient_balance import InsufficientBalanceError
from app.services.transaction_logger import log_info, log_error


class BankAccount:
    """Represents a bank account with basic deposit and withdrawal features."""

    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be numeric.")

        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self._balance += amount
        log_info(f"{self.owner} deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount: float):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be numeric.")

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self._balance:
            log_error("Insufficient balance.")
            raise InsufficientBalanceError("Balance is not enough.")

        self._balance -= amount
        log_info(f"{self.owner} withdrew {amount}. Remaining balance: {self._balance}")

    def __repr__(self):
        return f"BankAccount(owner={self.owner}, balance={self._balance})"
