"""
=============================================================================
TOPIC: PYTHON FUNCTIONS, *ARGS, **KWARGS, LAMBDA & FUNCTIONAL UTILITIES
=============================================================================
Author: Python Mastery Course
Level: Beginner to Intermediate (Data Analytics & Automation)

Conceptual Overview:
--------------------
1. What is a Function?
   - A function is an organized, reusable block of code designed to perform 
     a single, specific task.
   - Analogy: Think of a microwave. You supply input (raw food / timer), it 
     processes the logic inside, and produces an output (cooked meal) without 
     you needing to rewire the heating element every time.

2. Variable-Length Arguments:
   - `*args`: Collects an arbitrary number of positional arguments as a Tuple.
   - `**kwargs`: Collects arbitrary keyword arguments as a Dictionary.

3. Lambda Functions:
   - Small, anonymous, single-line functions created on the fly.
   - Syntax: `lambda arguments: expression`
   - Heavily utilized inside Pandas `.apply()`, `map()`, and custom sort keys.

4. Topics Covered in this Guide:
   - Part 1: Function Anatomy, Return Values & Docstrings
   - Part 2: Default Arguments & Defensive Parameter Design
   - Part 3: Flexible Inputs using *args and **kwargs
   - Part 4: Variable Scope (LEGB Rule & Global Keyword)
   - Part 5: Lambda (Anonymous) Functions in Action
   - Part 6: Higher-Order Functions (map, filter, zip, sorted)
   - Part 7: Real-world Practice: Corporate Payroll & Bonus Calculation Engine
=============================================================================
"""

import sys

# Ensure UTF-8 output encoding across all Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# =============================================================================
# PART 1: FUNCTION ANATOMY, RETURN VALUES & DOCSTRINGS
# =============================================================================
print("=" * 65)
print(">>> PART 1: FUNCTION ANATOMY & RETURN VALUES <<<")
print("=" * 65)

def calculate_roi(investment: float, returns: float) -> float:
    """
    Calculates Return on Investment (ROI) percentage.
    Formula: ((Returns - Investment) / Investment) * 100
    """
    net_profit = returns - investment
    roi_percent = (net_profit / investment) * 100
    return roi_percent

initial_capital = 50000
final_return = 72500
growth = calculate_roi(initial_capital, final_return)

print(f"• Initial Investment: Rs. {initial_capital:,}")
print(f"• Final Value       : Rs. {final_return:,}")
print(f"• Calculated ROI    : {growth:.2f}%")
print(f"• Function Docstring: {calculate_roi.__doc__.strip()}")


# =============================================================================
# PART 2: DEFAULT ARGUMENTS & DEFENSIVE PARAMETER DESIGN
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 2: DEFAULT ARGUMENTS & KEYWORD CALLS <<<")
print("=" * 65)

def generate_invoice(customer_name: str, base_amount: float, tax_rate: float = 0.18, discount: float = 0.0) -> dict:
    """Computes final payable bill with default GST tax rate of 18%."""
    discount_amount = base_amount * discount
    taxable_amount = base_amount - discount_amount
    tax_amount = taxable_amount * tax_rate
    final_total = taxable_amount + tax_amount

    return {
        "customer": customer_name,
        "base": base_amount,
        "discount_applied": discount_amount,
        "tax": tax_amount,
        "grand_total": final_total
    }

# 1. Calling with default tax (18%) and no discount
inv1 = generate_invoice("YSM Info Solution", 100000)
print(f"• Invoice 1 (Standard 18% Tax):")
print(f"  Customer: {inv1['customer']} | Tax: Rs. {inv1['tax']:,.2f} | Total: Rs. {inv1['grand_total']:,.2f}")

# 2. Calling with custom 10% discount and 12% concession tax rate (Keyword Arguments)
inv2 = generate_invoice("TechCorp Ltd", base_amount=250000, tax_rate=0.12, discount=0.10)
print(f"• Invoice 2 (Custom Discount & Concession Tax):")
print(f"  Customer: {inv2['customer']} | Discount: Rs. {inv2['discount_applied']:,.2f} | Total: Rs. {inv2['grand_total']:,.2f}")


# =============================================================================
# PART 3: FLEXIBLE INPUTS (*ARGS AND **KWARGS)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 3: FLEXIBLE PARAMETERS (*args & **kwargs) <<<")
print("=" * 65)

# *args captures any number of positional arguments into a Tuple
def compute_sales_metrics(*sales_figures):
    """Aggregates an unknown number of weekly/monthly sales numbers."""
    total_sales = sum(sales_figures)
    avg_sales = total_sales / len(sales_figures) if sales_figures else 0
    return total_sales, avg_sales

total, avg = compute_sales_metrics(12000, 18500, 24000, 31000, 19500)
print(f"• *args Sales Metric:")
print(f"  Total Sales: Rs. {total:,} | Average per Store: Rs. {avg:,.2f}")

# **kwargs captures any number of named keyword arguments into a Dictionary
def build_employee_profile(emp_id: int, name: str, **metadata):
    """Creates a dynamic employee record storing flexible company attributes."""
    profile = {"Emp_ID": emp_id, "Name": name}
    profile.update(metadata)
    return profile

emp1 = build_employee_profile(
    101, "Aarav Sharma", 
    department="Data Analytics", 
    city="Pune", 
    experience_years=4, 
    certification="Power BI Certified"
)

print(f"\n• **kwargs Dynamic Employee Profile:")
for k, v in emp1.items():
    print(f"  {k:<18}: {v}")


# =============================================================================
# PART 4: VARIABLE SCOPE (LEGB RULE & GLOBAL KEYWORD)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 4: VARIABLE SCOPE (LEGB RULE) <<<")
print("=" * 65)

# Global Scope Variable
current_fiscal_year = "2026-27"
total_audited_transactions = 0

def audit_batch(batch_size: int):
    # Modifying a global variable inside a local scope requires 'global' keyword
    global total_audited_transactions
    local_batch_status = f"Batch of {batch_size} processed for FY {current_fiscal_year}"
    total_audited_transactions += batch_size
    return local_batch_status

print(f"• Before Batch: Total Audited = {total_audited_transactions}")
msg = audit_batch(500)
print(f"  Audit Status: {msg}")
print(f"• After Batch : Total Audited = {total_audited_transactions}")


# =============================================================================
# PART 5: LAMBDA FUNCTIONS (ANONYMOUS SINGLE-LINE LOGIC)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 5: LAMBDA FUNCTIONS <<<")
print("=" * 65)

# Standard function vs Lambda comparison
# Normal:
# def calculate_gst(amount): return amount * 0.18
# Lambda:
calculate_gst = lambda amount: amount * 0.18
apply_markup = lambda cost, margin: cost * (1 + margin)

test_cost = 4500
print(f"• Base Cost               : Rs. {test_cost:,}")
print(f"• GST (18% via Lambda)    : Rs. {calculate_gst(test_cost):,.2f}")
print(f"• 25% Markup (via Lambda) : Rs. {apply_markup(test_cost, 0.25):,.2f}")


# =============================================================================
# PART 6: HIGHER-ORDER FUNCTIONAL UTILITIES (MAP, FILTER, ZIP, SORTED)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 6: MAP, FILTER, ZIP & SORTED <<<")
print("=" * 65)

salaries_inr = [35000, 52000, 78000, 95000, 42000, 110000]

# 1. map(): Apply a function to every item in an iterable
# Give a 10% appraisal hike across all employees
hiked_salaries = list(map(lambda s: round(s * 1.10, 2), salaries_inr))
print(f"• Original Salaries : {salaries_inr}")
print(f"• 10% Hiked Salaries: {hiked_salaries}")

# 2. filter(): Retain only items satisfying a condition
# Filter employees earning more than Rs. 60,000
senior_salaries = list(filter(lambda s: s > 60000, salaries_inr))
print(f"• Filtered Senior Salaries (> 60k): {senior_salaries}")

# 3. zip(): Pair corresponding elements from parallel lists
departments = ["HR", "IT", "Data Analytics", "Finance", "Sales", "Executive"]
team_directory = list(zip(departments, salaries_inr))
print(f"\n• Paired Directory (zip):")
for dept, sal in team_directory:
    print(f"  {dept:<16} -> Rs. {sal:,}")

# 4. sorted() with custom lambda key: Sort by salary ascending / descending
sorted_by_salary = sorted(team_directory, key=lambda x: x[1], reverse=True)
print(f"\n• Sorted by Highest Compensation:")
for dept, sal in sorted_by_salary:
    print(f"  {dept:<16} : Rs. {sal:,}")


# =============================================================================
# PART 7: MINI-PROJECT: CORPORATE PAYROLL & DEDUCTION PIPELINE
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 7: MINI-PROJECT: COMPLETE PAYROLL ENGINE <<<")
print("=" * 65)

staff_members = [
    {"name": "Rahul Roy",    "base_salary": 65000, "performance_score": 92},
    {"name": "Pooja Hegde",  "base_salary": 52000, "performance_score": 79},
    {"name": "Amit Patel",   "base_salary": 95000, "performance_score": 96},
    {"name": "Sneha Rao",    "base_salary": 80000, "performance_score": 88}
]

def calculate_net_pay(emp: dict) -> dict:
    base = emp["base_salary"]
    score = emp["performance_score"]

    # Bonus rule: 15% if score >= 90, 8% if score >= 80, else 0%
    bonus_rate = 0.15 if score >= 90 else (0.08 if score >= 80 else 0.0)
    bonus = base * bonus_rate

    # Standard Deductions: Provident Fund (PF: 12% of base), Professional Tax (PT: Rs. 200)
    pf_deduction = base * 0.12
    pt_deduction = 200

    gross_salary = base + bonus
    net_salary = gross_salary - (pf_deduction + pt_deduction)

    return {
        "Name": emp["name"],
        "Base": base,
        "Bonus": bonus,
        "PF": pf_deduction,
        "Net_Pay": net_salary
    }

payroll_register = list(map(calculate_net_pay, staff_members))

print(f"{'Employee Name':<14} | {'Base Salary':<11} | {'Bonus':<9} | {'PF Deduct':<10} | {'Net Pay':<11}")
print("-" * 65)
for p in payroll_register:
    print(f"{p['Name']:<14} | Rs. {p['Base']:<8,}| Rs. {p['Bonus']:<6,}| Rs. {p['PF']:<7,}| Rs. {p['Net_Pay']:<8,}")

total_payroll = sum(p["Net_Pay"] for p in payroll_register)
print("-" * 65)
print(f"• Total Company Monthly Payroll Disbursement: Rs. {total_payroll:,.2f}")

print("=" * 65)
print(">>> TOPIC 03 COMPLETE: FUNCTIONS, LAMBDA & PIPELINES MASTERED <<<")
print("=" * 65)
