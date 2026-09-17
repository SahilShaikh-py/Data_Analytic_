"""
=============================================================================
TOPIC 01: PYTHON MODULES (BUILT-IN & STANDARD LIBRARY)
=============================================================================
Author: Python Mastery Course
Level: Beginner to Intermediate

Conceptual Overview:
--------------------
1. What is a Module?
   - A module is a single Python file (.py file) containing pre-written code 
     (Functions, Variables, Classes).
   - Example: Just as a toolbox contains various tools, Python modules are 
     collections of ready-to-use functions.

2. Benefits of Using Modules (Advantages):
   - Code Reusability: Write code once and import it across multiple files.
   - Code Organization: Group related functions into separate, well-structured files.
   - Cleaner Code: Keeps the main program concise, organized, and readable.

3. Four Ways to Import Modules in Python:
   - Method 1: `import module_name` -> Call every function as `module_name.function()`.
   - Method 2: `from module_name import function_name` -> Call the function directly by name.
   - Method 3: `import module_name as alias` -> Assign a convenient shorthand name (e.g., `import math as m`).
   - Method 4: `from module_name import *` -> Imports all functions directly into the current namespace (Not recommended in production/large projects).
=============================================================================
"""

print("=" * 65)
print(">>> PART 1: FOUR WAYS TO IMPORT MODULES <<<")
print("=" * 65)

# -------------------------------------------------------------
# 1. Standard Import (import module_name)
# -------------------------------------------------------------
import math

print("\n--- 1. Standard Import Example ---")
# The sqrt function from the math module calculates the square root of a number
result_sqrt = math.sqrt(64)
print(f"math.sqrt(64) = {result_sqrt}")  # Output: 8.0
print(f"Value of math.pi * result_sqrt = {math.pi * result_sqrt}")    # Output: 3.141592653589793

# -------------------------------------------------------------
# 2. Specific Function Import (from module import ...)
# -------------------------------------------------------------
from math import pow, floor, ceil

print("\n--- 2. Specific Function Import Example ---")
# Use pow() directly without prefixing math.pow()
power_result = pow(2, 5) # 2 raised to the power of 5 (2^5 = 32)
print(f"pow(2, 5) = {power_result}")

# floor: Rounds down to the nearest lower integer (4.9 -> 4)
# ceil: Rounds up to the nearest higher integer (4.1 -> 5)
print(f"floor(4.9) = {floor(4.9)}")
print(f"ceil(4.1) = {ceil(4.1)}")

# -------------------------------------------------------------
# 3. Aliasing (Giving an Alias: import module as alias)
# -------------------------------------------------------------
import datetime as dt

print("\n--- 3. Aliasing Example (using the 'as' keyword) ---")
# Retrieve current date and time using dt.datetime
current_date = dt.datetime.now()
print(f"Current Date & Time: {current_date}")
print(f"Year: {current_date.year}, Month: {current_date.month}, Day: {current_date.day}")
# strftime: Formats date and time into a custom human-readable string
formatted_date = current_date.strftime("%d-%B-%Y (%A) %I:%M %p")
print(f"Formatted Date: {formatted_date}")

# -------------------------------------------------------------
# 4. RANDOM MODULE (Used in Gaming, OTP Generation, and Data Shuffling)
# -------------------------------------------------------------
import random

print("\n" + "=" * 65)
print(">>> PART 2: RANDOM MODULE EXAMPLES <<<")
print("=" * 65)

# randint(a, b): Returns a random integer between 'a' and 'b' inclusive
otp = random.randint(1000, 9999)
print(f"• 4-Digit Generated OTP: {otp}")

# choice(list): Randomly picks a single element from a sequence
students = ["Rahul", "Priya", "Amit", "Sneha", "Vikas"]
lucky_winner = random.choice(students)
print(f"• Random Lucky Winner: {lucky_winner}")

# shuffle(list): Randomizes the order of elements in place
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(cards)
print(f"• Shuffled Cards: {cards}")

# sample(list, k): Selects 'k' unique random items from a sequence
sample_students = random.sample(students, 2)
print(f"• Selected 2 Students for Project: {sample_students}")

# -------------------------------------------------------------
# 5. OS & SYS MODULE (Operating System and Python Runtime Interaction)
# -------------------------------------------------------------
import os
import sys

print("\n" + "=" * 65)
print(">>> PART 3: OS & SYS MODULES <<<")
print("=" * 65)

# os.getcwd(): Returns the Current Working Directory path
cwd = os.getcwd()
print(f"• Current Working Directory (CWD): {cwd}")

# os.path.exists(): Checks whether a file or directory exists
is_file_exist = os.path.exists("01_modules_builtin_and_standard.py")
print(f"• Does this file exist?: {is_file_exist}")

# sys.version: Provides details of the installed Python version
print(f"• Python Version: {sys.version.split()[0]}")

# sys.platform: Identifies the running Operating System platform (win32 / linux / darwin)
print(f"• Running OS Platform: {sys.platform}")

# -------------------------------------------------------------
# 6. JSON MODULE (Data Interchange Format - APIs & Web Services)
# -------------------------------------------------------------
import json

print("\n" + "=" * 65)
print(">>> PART 4: JSON MODULE (Serialization & Deserialization) <<<")
print("=" * 65)

# Python Dictionary
student_data = {
    "id": 101,
    "name": "Aakash Sharma",
    "course": "Data Analytics",
    "is_enrolled": True,
    "skills": ["Python", "SQL", "Pandas"]
}

# json.dumps(): Converts a Python dictionary into a JSON formatted string (Serialization)
json_string = json.dumps(student_data, indent=4)
print("• Python Dict converted to JSON String:")
print(json_string)

# json.loads(): Parses a JSON string back into a Python dictionary (Deserialization)
parsed_dict = json.loads(json_string)
print(f"\n• Parsed Student Name from JSON: {parsed_dict['name']}")
print(f"• Student's 1st Skill: {parsed_dict['skills'][0]}")

print("\n" + "=" * 65)
print(">>> MODULE 01 COMPLETED SUCCESSFULLY! <<<")
print("=" * 65)
