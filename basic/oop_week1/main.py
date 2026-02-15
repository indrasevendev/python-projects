from app.models.bank_account import BankAccount
from app.exceptions.insufficient_balance import InsufficientBalanceError

account = BankAccount("Indra", 1000)

try:
    account.deposit(100)
    account.withdraw(300)
    print("Final Balance:", account.balance)

except InsufficientBalanceError as e:
    print("Transaction failed:", e)

except Exception as e:
    print("Unexpected error:", e)
