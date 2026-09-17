"""
=============================================================================
HELPER MODULE: my_calculator.py (User-Defined Module)
=============================================================================
This is a custom module built to demonstrate user-defined modules in Python.
It defines basic mathematical operations, constants, and a utility Helper class.

Conceptual Overview:
--------------------
- This file can be run directly as an independent script, or imported into
  other programs using `import my_calculator`.
- The `if __name__ == '__main__':` block ensures that unit testing code executes
  only when this file is run directly, not when it is imported by another module.
=============================================================================
"""

# Constant Variables
PI_VALUE = 3.14159
VERSION = "1.0.0"

# User-Defined Functions
def add(a, b):
    """Adds two numbers and returns their sum."""
    return a + b

def subtract(a, b):
    """Subtracts 'b' from 'a' and returns the difference."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers and returns the product."""
    return a * b

def divide(a, b):
    """Divides 'a' by 'b' with zero-division validation."""
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b

def calculate_simple_interest(principal, rate, time):
    """
    Calculates Simple Interest using formula: (P * R * T) / 100
    - principal: Principal amount (initial investment or loan)
    - rate: Annual interest rate in percentage (%)
    - time: Time period in years
    """
    si = (principal * rate * time) / 100
    total_amount = principal + si
    return {"Simple_Interest": si, "Total_Amount": total_amount}

# Helper Class inside a Module
class NumberHelper:
    """Utility class to inspect properties of numerical values."""
    
    @staticmethod
    def is_even(num):
        """Checks whether a number is Even."""
        return num % 2 == 0

    @staticmethod
    def is_prime(num):
        """Checks whether a number is Prime."""
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True


# -----------------------------------------------------------------------------
# REAL-WORLD USE CASE OF: if __name__ == '__main__':
# -----------------------------------------------------------------------------
# When this file is run DIRECTLY -> __name__ is set to '__main__' (Tests execute)
# When this file is IMPORTED into another module -> __name__ is set to 'my_calculator' (Tests do NOT run)
if __name__ == "__main__":
    print(">>> Direct Execution Mode: Testing my_calculator module...")
    print(f"Test Add: 10 + 20 = {add(10, 20)}")
    print(f"Test Prime (7): {NumberHelper.is_prime(7)}")
    print(f"Test Even (8): {NumberHelper.is_even(8)}")
    print(">>> Module tests passed successfully!")
