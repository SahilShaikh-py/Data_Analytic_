"""
=============================================================================
TOPIC 02: USER-DEFINED MODULES & BEST PRACTICES
=============================================================================
Author: Python Mastery Course
Level: Beginner to Intermediate

Conceptual Overview:
--------------------
1. What is a User-Defined Module?
   - When we create our own `.py` file (such as `my_calculator.py`) and import
     its functions, variables, or classes into another Python script, it is 
     referred to as a User-Defined Module.

2. Understanding `if __name__ == '__main__':`:
   - Every Python script has a special built-in variable named `__name__`.
   - Case 1: If the file is executed directly, `__name__` is assigned `"__main__"`.
   - Case 2: If the file is imported into another script, `__name__` is assigned 
     the module's filename (without the `.py` extension).
   - Purpose: It prevents test or demonstration code from executing automatically
     when the file is imported elsewhere.

3. Module Information & Inspection:
   - `dir(module_name)`: Returns a list of all functions, classes, and attributes defined inside the module.
   - `module_name.__doc__`: Displays the docstring (documentation) of the module.
   - `module_name.__file__`: Displays the file system path of the module.
=============================================================================
"""

print("=" * 65)
print(">>> PART 1: IMPORTING USER-DEFINED MODULES <<<")
print("=" * 65)

# Importing the custom 'my_calculator.py' created earlier
import my_calculator as calc
from my_calculator import calculate_simple_interest, NumberHelper

print("\n--- 1. Calling Functions from Custom Module ---")
num1 = 50
num2 = 10

# Calling functions via the 'calc' alias
sum_res = calc.add(num1, num2)
sub_res = calc.subtract(num1, num2)
mul_res = calc.multiply(num1, num2)
div_res = calc.divide(num1, num2)

print(f"• Addition ({num1} + {num2})       = {sum_res}")
print(f"• Subtraction ({num1} - {num2})    = {sub_res}")
print(f"• Multiplication ({num1} * {num2}) = {mul_res}")
print(f"• Division ({num1} / {num2})       = {div_res}")
print(f"• Module Constant PI               = {calc.PI_VALUE}")
print(f"• Module Version                   = {calc.VERSION}")

print("\n" + "=" * 65)
print(">>> PART 2: ADVANCED FUNCTIONS & CLASSES FROM CUSTOM MODULE <<<")
print("=" * 65)

# 2. Simple Interest Calculation
principal = 100000  # 100,000 Currency Units
rate = 7.5          # 7.5% per annum
time_years = 3      # 3 years

si_result = calculate_simple_interest(principal, rate, time_years)
print(f"\n• Principal Amount: ₹{principal:,}")
print(f"• Interest Rate   : {rate}%")
print(f"• Time Period     : {time_years} Years")
print(f"• Total Interest  : ₹{si_result['Simple_Interest']:,}")
print(f"• Final Payback   : ₹{si_result['Total_Amount']:,}")

# 3. Helper Class methods
test_numbers = [17, 24, 29, 36, 47]
print("\n--- Checking Numbers with NumberHelper Class ---")
for n in test_numbers:
    is_p = NumberHelper.is_prime(n)
    is_e = NumberHelper.is_even(n)

    status_prime = "Prime" if is_p else "Not Prime"
    status_even = "Even" if is_e else "Odd"
    print(f"• Number {n:>2} -> {status_prime:<12} | {status_even}")

print("\n" + "=" * 65)
print(">>> PART 3: MODULE INSPECTION & INTROSPECTION <<<")
print("=" * 65)

print(f"• Module File Location : {calc.__file__}")
print(f"• Current File __name__: {__name__}")
print(f"• Imported Module Name : {calc.__name__}")

# dir() function: Lists all available attributes and methods in the module
print("\n• Available attributes in 'my_calculator':")
available_items = [item for item in dir(calc) if not item.startswith("__")]
print(f"  {available_items}")

print("\n" + "=" * 65)
print(">>> MODULE 02 COMPLETED SUCCESSFULLY! <<<")
print("=" * 65)
