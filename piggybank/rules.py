# Import our custom ValidationError to raise consistent, typed errors
from .errors import ValidationError

# Ensure the amount is strictly positive (> 0)
def ensure_positive(amount: float) -> None:
    if amount <= 0:
        raise ValidationError("amount must be positive")

# Ensure a balance covers a desired withdrawal amount 
def ensure_sufficient(balance: float, amount: float) -> None:
    # If the desired amount exceeds the current balance, signal a validation error
    if amount > balance:
        raise ValidationError("insufficient funds")
