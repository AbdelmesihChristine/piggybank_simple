# Import the argparse module to build a tiny command-line interface (CLI)
import argparse
# Import classes and functions from our local package 'piggybank'
from piggybank.account import AccountOwner, SavingsAccount, CheckingAccount
from piggybank.errors import ValidationError

# Define a small function that runs a demonstration of the OOP classes
def demo() -> None:
    print("=== PiggyBank Demo ===")
    # Create an account owner named Alice with id 'A1'
    alice = AccountOwner("Alice", "A1")
    # Open a SavingsAccount for Alice with 100.0 starting balance and 2% monthly interest
    sav = SavingsAccount(alice, opening_balance=100.0, interest_rate=0.02)
    sav.deposit(50.0)
    sav.withdraw(25.0)
    # Apply month-end processing (adds interest for savings accounts)
    sav.apply_month_end()
    print(f"Savings balance (after month end): {sav.balance:.2f}") #two decimals

    # Create an account owner named Bob with id 'B1'
    bob = AccountOwner("Bob", "B1")
    chk = CheckingAccount(bob, opening_balance=10.0, withdraw_fee=0.5)
    # Try to withdraw 4.0 (this will charge a 0.5 fee on success)
    chk.withdraw(4.0)
    print(f"Checking balance (after withdraw 4.0 + fee 0.5): {chk.balance:.2f}") #two decimals

# The main() function is the program's entry point
def main() -> None:
    # Create the top-level CLI parser with a program name and description
    ap = argparse.ArgumentParser(prog="piggybank", description="Tiny OOP demo with CLI")
    # Add a single subcommand called 'demo' to run our scenario
    ap.add_argument("--demo", action="store_true", help="run a short scenario for Savings & Checking")
    # Parse command-line arguments from sys.argv
    args = ap.parse_args()
    if args.demo:
        demo()
    else:
        ap.print_help()

# This conditional makes sure main() only runs when the file is executed directly
if __name__ == "__main__":
    main()
