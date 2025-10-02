# Define a base exception so all library errors share a common ancestor
class PiggyBankError(Exception):
    # A simple marker subclass of Exception for PiggyBank-specific errors
    pass

# Define a specific error used when inputs are invalid or a rule is violated
class ValidationError(PiggyBankError):
    pass
