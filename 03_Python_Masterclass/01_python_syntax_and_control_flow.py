"""
=============================================================================
TOPIC: PYTHON SYNTAX, VARIABLES, DATA TYPES & CONTROL FLOW
=============================================================================
Author: Python Mastery Course
Level: Beginner to Intermediate (Foundation for Data Analytics)

Conceptual Overview:
--------------------
1. What is Python?
   - Python is a high-level, interpreted, dynamically-typed programming language.
   - It emphasizes readable, clean syntax, making it the premier choice for 
     Data Analytics, Machine Learning, and Automation.

2. Dynamic Typing:
   - In Python, variables do not require explicit type declarations.
   - The Python interpreter infers the data type dynamically at runtime based
     on the value assigned.

3. Control Flow:
   - Programs make intelligent decisions using conditional statements (if-elif-else).
   - Loops (for, while) automate repetitive calculations across datasets.

4. Core Topics Covered in this Guide:
   - Part 1: Variables, Dynamic Typing & Primitive Data Types
   - Part 2: Explicit Type Casting & Modern String Formatting (f-strings)
   - Part 3: Python Operators (Arithmetic, Comparison, Logical, Membership)
   - Part 4: Conditional Statements (if-elif-else) & Business Decision Logic
   - Part 5: For Loops, range(), Enumeration & Nested Iteration
   - Part 6: While Loops & Loop Control Statements (break, continue, pass)
   - Part 7: Real-world Practice: Student Evaluation & KPI Assessment Engine
=============================================================================
"""

# =============================================================================
# PART 1: VARIABLES, DYNAMIC TYPING & PRIMITIVE DATA TYPES
# =============================================================================
import sys

# Ensure UTF-8 output encoding across all Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("=" * 65)
print(">>> PART 1: VARIABLES & PRIMITIVE DATA TYPES <<<")
print("=" * 65)

# Python supports four fundamental primitive types:
student_name = "Sahil Shaikh"       # str (String / Text)
student_age = 22                    # int (Integer / Whole number)
course_gpa = 3.85                   # float (Floating point / Decimal)
is_enrolled = True                  # bool (Boolean / True or False)

print(f"• Student Name : {student_name} | Type: {type(student_name).__name__}")
print(f"• Student Age  : {student_age} | Type: {type(student_age).__name__}")
print(f"• Course GPA   : {course_gpa} | Type: {type(course_gpa).__name__}")
print(f"• Enrollment   : {is_enrolled} | Type: {type(is_enrolled).__name__}")

# Dynamic reassignment demonstration
salary_metric = 45000               # Initially an integer
print(f"\n• Initial Metric Value: {salary_metric} (Type: {type(salary_metric).__name__})")
salary_metric = "Exceeds Target"    # Reassigned to a string dynamically
print(f"• Updated Metric Value: '{salary_metric}' (Type: {type(salary_metric).__name__})")


# =============================================================================
# PART 2: TYPE CASTING & STRING FORMATTING (F-STRINGS)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 2: TYPE CASTING & F-STRINGS <<<")
print("=" * 65)

import sys

# Ensure UTF-8 output encoding across all Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# 1. Type Casting (Converting between types)
raw_sales_input = "1500"            # Data imported from CSV often starts as text
tax_percentage = "0.18"

# Converting string to numeric for calculations
sales_amount = float(raw_sales_input)
tax_rate = float(tax_percentage)
total_tax = sales_amount * tax_rate
grand_total = sales_amount + total_tax

print(f"• Raw Input (String): '{raw_sales_input}'")
print(f"• Converted Numeric Total Sales: Rs. {sales_amount:,.2f}")
print(f"• Computed Tax (18%): Rs. {total_tax:,.2f}")
print(f"• Grand Total Payable: Rs. {grand_total:,.2f}")

# 2. Boolean Type Casting Truthiness
# In Python: 0, None, "", [], {}, () are False. Everything else is True.
print("\n• Boolean Evaluation (Truthiness):")
print(f"  bool(0)       -> {bool(0)}")
print(f"  bool('')      -> {bool('')}")
print(f"  bool('Data')  -> {bool('Data')}")
print(f"  bool(100)     -> {bool(100)}")


# =============================================================================
# PART 3: OPERATORS (ARITHMETIC, COMPARISON, LOGICAL, MEMBERSHIP)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 3: OPERATORS (ARITHMETIC & LOGICAL) <<<")
print("=" * 65)

a = 25
b = 4

# 1. Arithmetic Operators
print("• Arithmetic Operations:")
print(f"  Addition ({a} + {b})       = {a + b}")
print(f"  Subtraction ({a} - {b})    = {a - b}")
print(f"  Multiplication ({a} * {b}) = {a * b}")
print(f"  Division ({a} / {b})       = {a / b}")
print(f"  Floor Division ({a} // {b})= {a // b} (Removes decimal part)")
print(f"  Modulus / Remainder ({a} % {b}) = {a % b}")
print(f"  Exponentiation ({a} ** {b})= {a ** b} (25 raised to power 4)")

# 2. Comparison & Logical Operators
sales_rep_score = 88
attendance_rate = 94

is_top_performer = (sales_rep_score >= 85) and (attendance_rate >= 90)
needs_training = (sales_rep_score < 70) or (attendance_rate < 75)

print("\n• Logical Evaluation:")
print(f"  Is Top Performer (Score >= 85 AND Attendance >= 90): {is_top_performer}")
print(f"  Needs Training (Score < 70 OR Attendance < 75): {needs_training}")

# 3. Membership Operators ('in' and 'not in')
allowed_roles = ["Admin", "Data Analyst", "Data Engineer", "BI Consultant"]
user_role = "Data Analyst"

print(f"\n• Membership Check:")
print(f"  Is '{user_role}' in allowed roles? -> {user_role in allowed_roles}")
print(f"  Is 'Guest' not in allowed roles?    -> {'Guest' not in allowed_roles}")


# =============================================================================
# PART 4: CONDITIONAL STATEMENTS (IF - ELIF - ELSE)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 4: CONDITIONAL DECISION LOGIC <<<")
print("=" * 65)

# Business scenario: E-commerce Customer Discount Tier Assignment
purchase_amount = 8500

if purchase_amount >= 10000:
    tier = "Platinum"
    discount_percent = 20
elif purchase_amount >= 5000:
    tier = "Gold"
    discount_percent = 12
elif purchase_amount >= 2000:
    tier = "Silver"
    discount_percent = 5
else:
    tier = "Standard"
    discount_percent = 0

discount_value = (purchase_amount * discount_percent) / 100
final_bill = purchase_amount - discount_value

print(f"• Purchase Amount   : Rs. {purchase_amount:,.2f}")
print(f"• Customer Tier     : {tier}")
print(f"• Applied Discount  : {discount_percent}% (Savings: Rs. {discount_value:,.2f})")
print(f"• Final Invoice Pay : Rs. {final_bill:,.2f}")


# =============================================================================
# PART 5: FOR LOOPS, RANGE & ENUMERATION
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 5: FOR LOOPS, RANGE & ENUMERATION <<<")
print("=" * 65)

# 1. Standard range() iteration: range(start, stop, step)
print("• Counting by 5s using range(10, 31, 5):")
for num in range(10, 31, 5):
    print(f"  Step Value: {num}")

# 2. Iterating over an analytics dataset with enumerate()
daily_revenue = [12000, 15400, 18900, 14200, 22500, 28000, 31000]
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("\n• Weekly Revenue Tracking:")
for index, (day, rev) in enumerate(zip(days_of_week, daily_revenue), start=1):
    print(f"  Day {index} ({day}): Rs. {rev:,.2f}")


# =============================================================================
# PART 6: WHILE LOOPS & CONTROL STATEMENTS (BREAK, CONTINUE, PASS)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 6: WHILE LOOPS & CONTROL STATEMENTS <<<")
print("=" * 65)

# 1. While Loop with Termination Condition
account_balance = 10000
monthly_subscription = 1800
month = 1

print("• Simulating Subscription Deductions (While Loop):")
while account_balance >= monthly_subscription:
    account_balance -= monthly_subscription
    print(f"  Month {month}: Debited Rs. {monthly_subscription}, Remaining Balance: Rs. {account_balance}")
    month += 1
print(f"  Subscription stopped: Insufficient balance (Rs. {account_balance})")

# 2. Using 'continue' to skip items and 'break' to stop early
raw_data_stream = [250, 410, -999, 320, "CORRUPT", 540, 9999, 610]
cleaned_metrics = []

print("\n• Data Stream Cleaning with break & continue:")
for entry in raw_data_stream:
    if entry == "CORRUPT" or entry == -999:
        print(f"  [SKIPPED] Bad entry found: {entry} -> continuing to next")
        continue  # Skip this iteration
    if entry == 9999:
        print(f"  [HALTED] Emergency stop signal: {entry} -> breaking loop")
        break     # Terminate loop entirely
    cleaned_metrics.append(entry)

print(f"• Successfully Processed Clean Stream: {cleaned_metrics}")


# =============================================================================
# PART 7: MINI-PROJECT: AUTOMATED KPI & PERFORMANCE AUDIT
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 7: MINI-PROJECT: EMPLOYEE PERFORMANCE EVALUATION <<<")
print("=" * 65)

employees = [
    {"name": "Aarav Sharma", "deals_closed": 18, "csat": 95},
    {"name": "Neha Verma",   "deals_closed": 8,  "csat": 78},
    {"name": "Rohan Gupta",  "deals_closed": 14, "csat": 88},
    {"name": "Priya Nair",   "deals_closed": 22, "csat": 98},
]

print(f"{'Employee Name':<16} | {'Deals':<6} | {'CSAT %':<6} | {'Bonus Rating':<15} | {'Action':<15}")
print("-" * 68)

for emp in employees:
    deals = emp["deals_closed"]
    csat = emp["csat"]
    
    if deals >= 20 and csat >= 90:
        rating = "Outstanding"
        action = "Promotion + 25% Bonus"
    elif deals >= 12 and csat >= 85:
        rating = "Exceeds Target"
        action = "15% Bonus"
    elif deals >= 10:
        rating = "Meets Target"
        action = "Standard Bonus"
    else:
        rating = "Needs Support"
        action = "Mentorship Plan"

    print(f"{emp['name']:<16} | {deals:<6} | {csat:<6}% | {rating:<15} | {action:<15}")

print("=" * 65)
print(">>> TOPIC 01 COMPLETE: SYNTAX & CONTROL FLOW MASTERED <<<")
print("=" * 65)
