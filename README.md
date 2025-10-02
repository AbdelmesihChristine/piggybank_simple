
## 📌 Project Introduction – PiggyBank

The **PiggyBank project** is a small Python program that demonstrates **Object-Oriented Programming (OOP)** principles using a simple banking system.

The system models **bank accounts** and their owners, while enforcing safe rules like preventing negative deposits or overdrafts. It includes:

* **AccountOwner**: a simple data class that stores the name and ID of the account holder.
* **BankAccount**: an abstract base class (interface-like) that defines the *core functions* all accounts must implement (`withdraw`, `apply_month_end`).
* **SavingsAccount**: a concrete account that earns monthly interest but does not allow overdrafts.
* **CheckingAccount**: a concrete account that charges a fixed fee on every withdrawal, and validates that the balance can cover both the withdrawal amount and the fee.

Validation rules are separated into a helper file (`rules.py`) and errors are represented with custom exceptions (`ValidationError`).

## ⚙️ How the Accounts Work

* **Balance Handling:**
  Each account has an internal `_balance` attribute (encapsulated). The balance can only be changed through safe methods like `deposit()` or `withdraw()`.

* **Deposits:**
  Deposits must be **positive**; otherwise a `ValidationError` is raised.

* **Withdrawals:**

  * Savings accounts block overdrafts — the withdrawal cannot exceed the balance.
  * Checking accounts charge a **fixed fee per withdrawal**. Before withdrawing, the system checks that the balance can cover both the amount and the fee.

* **Month-End Processing:**

  * Savings accounts apply monthly interest (e.g., 2%).
  * Checking accounts don’t do anything at month end in this demo.

## 🔑 Functions and Their Purpose

1. **`deposit(amount)`**

   * Adds money to the account (must be positive).

2. **`withdraw(amount)` (abstract method)**

   * Must be implemented by each account type.
   * Savings → subtracts amount if balance is sufficient.
   * Checking → subtracts fee and amount if balance covers both.

3. **`apply_month_end()` (abstract method)**

   * Savings → applies interest.
   * Checking → does nothing in this version.

4. **`balance` (property)**

   * Returns the account’s balance (read-only).

5. **`owner` (property)**

   * Returns the `AccountOwner` object that owns the account.


## 🎯 Purpose of the Project

This project is not about real banking—it’s a **teaching/demo tool** to show:

* Encapsulation (`_balance` is private-like, safe access via methods).
* Abstraction (BankAccount defines required methods).
* Inheritance (SavingsAccount, CheckingAccount extend BankAccount).
* Polymorphism (different `apply_month_end` behavior per account type).
* Error handling with **custom exceptions**.
* A small **CLI entry point** in `main.py` to demo how accounts behave.


## Project Layout

piggybank_simple/
├─ main.py                 # Entry point (run this)
└─ piggybank/
   ├─ __init__.py          # Package exports
   ├─ account.py           # OOP models (Owner, Savings, Checking)
   ├─ errors.py            # Custom exceptions
   └─ rules.py             # Small validation helpers


## How to Run

bash
# (Optional) Create and activate a virtual environment
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

# Run the demo
python main.py --demo


You should see output like:

=== PiggyBank Demo ===
Savings balance (after month end): 127.50
Checking balance (after withdraw 4.0 + fee 0.5): 5.50

