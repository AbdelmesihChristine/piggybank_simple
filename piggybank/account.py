# Enable modern Python type annotations (not strictly necessary, but nice to have)
from __future__ import annotations
# Import ABC and abstractmethod to define an abstract base class
from abc import ABC, abstractmethod
# Import dataclass to define simple data containers for owners
from dataclasses import dataclass
# Import our ValidationError to signal invalid inputs or states
from .errors import ValidationError
# Import rule helpers to keep validation code tidy and reusable
from . import rules

# A simple, data container for the owner of a bank account
@dataclass
class AccountOwner:
    name: str
    id: str

# An abstract base class (ABC) capturing the common behavior of bank accounts
class BankAccount(ABC):
    # Docstring explains intent: a minimal, safe interface for accounts
    """Abstract account with minimal, safe interface."""

    # Constructor enforces basic invariants (e.g., non-negative opening balance)
    def __init__(self, owner: AccountOwner, opening_balance: float = 0.0) -> None:
        # Opening balance must not be negative
        if opening_balance < 0:
            raise ValidationError("opening balance cannot be negative")
        # Save a reference to the account owner
        self._owner = owner
        # Store balance as float; underscore marks it as "internal" (encapsulation)
        self._balance = float(opening_balance)

    # Read-only property for current balance, rounded to 2 decimals for display
    @property
    def balance(self) -> float:
        # Return a rounded copy so callers cannot mutate internal state directly
        return round(self._balance, 2)

    # Read-only property exposing the owner
    @property
    def owner(self) -> AccountOwner:
        # Return the owner object (safe to expose)
        return self._owner

    # Deposit money into the account
    def deposit(self, amount: float) -> None:
        # Validate the input amount is positive
        rules.ensure_positive(amount)
        # Increase the balance by the deposit amount
        self._balance += amount

    # Abstract method: subclasses must implement withdrawal policy
    @abstractmethod
    def withdraw(self, amount: float) -> None:
        # No body here; subclasses provide the behavior
        ...

    # Abstract method: subclasses define month-end processing (e.g., interest)
    @abstractmethod
    def apply_month_end(self) -> None:
        # No body here; subclasses provide the behavior
        ...

# A savings account that accrues interest and does not allow overdrafts
class SavingsAccount(BankAccount):
    # Constructor requires an interest rate (defaults to 1%)
    def __init__(self, owner: AccountOwner, opening_balance: float = 0.0, interest_rate: float = 0.01) -> None:
        # Initialize the base class first
        super().__init__(owner, opening_balance)
        if interest_rate < 0:
            raise ValidationError("interest_rate cannot be negative")
        # Save the rate for month-end calculations
        self._rate = interest_rate

    # Withdraw funds with overdraft protection
    def withdraw(self, amount: float) -> None:
        # Validate the requested amount is positive
        rules.ensure_positive(amount)
        # Ensure we have enough money to cover the withdrawal
        rules.ensure_sufficient(self._balance, amount)
        # Deduct the amount from the internal balance
        self._balance -= amount

    # Apply monthly interest to the savings balance
    def apply_month_end(self) -> None:
        # Add interest (simple monthly interest for this demo)
        self._balance += self._balance * self._rate

# A checking account that charges a fixed per-withdrawal fee (no monthly processing)
class CheckingAccount(BankAccount):
    # Constructor requires a per-withdrawal fee (defaults to 0.25)
    def __init__(self, owner: AccountOwner, opening_balance: float = 0.0, withdraw_fee: float = 0.25) -> None:
        # Initialize the base class first
        super().__init__(owner, opening_balance)
        if withdraw_fee < 0:
            raise ValidationError("withdraw_fee cannot be negative")
        # Save the fee for use during withdrawals
        self._fee = withdraw_fee

    # Withdraw funds with a fixed fee, preventing overdrafts including the fee
    def withdraw(self, amount: float) -> None:
        # Validate the requested amount is positive
        rules.ensure_positive(amount)
        # First validate that balance can cover both amount and fee (prevents bug)
        rules.ensure_sufficient(self._balance, amount + self._fee)
        # Deduct the fee from the internal balance
        self._balance -= self._fee
        # Deduct the withdrawal amount
        self._balance -= amount

    # Checking accounts have no monthly processing in this simple demo
    def apply_month_end(self) -> None:
        # Explicitly do nothing so the intent is clear
        pass
