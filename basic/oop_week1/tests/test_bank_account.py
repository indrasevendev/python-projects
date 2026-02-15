import pytest
from app.models.bank_account import BankAccount
from app.exceptions.insufficient_balance import InsufficientBalanceError


def test_deposit_success():
    acc = BankAccount("Test", 100)
    acc.deposit(50)
    assert acc.balance == 150


def test_withdraw_success():
    acc = BankAccount("Test", 200)
    acc.withdraw(50)
    assert acc.balance == 150


def test_withdraw_insufficient_balance():
    acc = BankAccount("Test", 100)

    with pytest.raises(InsufficientBalanceError):
        acc.withdraw(200)


def test_deposit_invalid_type():
    acc = BankAccount("Test", 100)

    with pytest.raises(TypeError):
        acc.deposit("100")

def test_deposit_negative():
    acc = BankAccount("Test", 100)

    with pytest.raises(ValueError):
        acc.deposit(-50)

def test_withdraw_negative():
    acc = BankAccount("Test", 100)

    with pytest.raises(ValueError):
        acc.withdraw(-10)


def test_withdraw_invalid_type():
    acc = BankAccount("Test", 100)

    with pytest.raises(TypeError):
        acc.withdraw("50")

def test_repr():
    account = BankAccount("Indra", 500)
    result = repr(account)
    assert result == "BankAccount(owner=Indra, balance=500)"
