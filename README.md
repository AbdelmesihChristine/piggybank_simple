# PiggyBank (Simple OOP Python Project)

This is a tiny, **intentionally simple** Python project to demonstrate:
- Basic OOP (classes, inheritance, abstract base classes, properties)
- Encapsulation (private-ish `_balance` with safe methods)
- Validation via helper functions and custom exceptions
- A clean **main entry point** (`main.py`) and a minimal CLI using `argparse`

## Project Layout

```
piggybank_simple/
├─ main.py                 # Entry point (run this)
└─ piggybank/
   ├─ __init__.py          # Package exports
   ├─ account.py           # OOP models (Owner, Savings, Checking)
   ├─ errors.py            # Custom exceptions
   └─ rules.py             # Small validation helpers
```

## How to Run

```bash
# (Optional) Create and activate a virtual environment
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

# Run the demo
python main.py --demo
```

You should see output like:

```
=== PiggyBank Demo ===
Savings balance (after month end): 127.50
Checking balance (after withdraw 4.0 + fee 0.5): 5.50
```

## Notes

- The **CheckingAccount.withdraw** method validates that the balance can cover
  **both** the amount and the fee *before* any deduction. This avoids a common
  bug where the fee is charged even if the withdrawal itself would fail.
- Keep it simple: no I/O, no databases, no tests—just enough OOP to shine in an interview.
