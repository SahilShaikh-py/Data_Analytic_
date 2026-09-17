"""
=============================================================================
TOPIC: PYTHON COLLECTIONS & DATA STRUCTURES (LISTS, TUPLES, SETS, DICTS)
=============================================================================
Author: Python Mastery Course
Level: Beginner to Intermediate (Data Analytics Core)

Conceptual Overview:
--------------------
1. What are Collections?
   - Collections are compound data types used to store groups of related items 
     in a single variable.
   - They form the fundamental building blocks of all Data Analytics, ETL 
     pipelines, and Machine Learning algorithms.

2. Comparison of the 4 Built-in Data Structures:
   ┌─────────────┬───────────┬────────────┬──────────────────┬─────────────────┐
   │ Collection  │ Ordered?  │ Mutable?   │ Allows Duplicate?│ Syntax          │
   ├─────────────┼───────────┼────────────┼──────────────────┼─────────────────┤
   │ List        │ Yes       │ Yes        │ Yes              │ [item1, item2]  │
   │ Tuple       │ Yes       │ No (Locked)│ Yes              │ (item1, item2)  │
   │ Set         │ No        │ Yes        │ No (Unique Only) │ {item1, item2}  │
   │ Dictionary  │ Yes (3.7+)│ Keys unique│ Values duplicate │ {key: value}    │
   └─────────────┴───────────┴────────────┴──────────────────┴─────────────────┘

3. Topics Covered in this Guide:
   - Part 1: Python Lists & In-Place Manipulations
   - Part 2: Python Tuples & Data Integrity Unpacking
   - Part 3: Python Sets & Venn Diagram Relational Math
   - Part 4: Dictionaries (Key-Value Lookups & Nested Records)
   - Part 5: List, Dict & Set Comprehensions (Pythonic Data Transformation)
   - Part 6: Built-in Collection Aggregators (sum, min, max, sorted, all, any)
   - Part 7: Real-world Practice: E-Commerce Basket & Customer Profiling Engine
=============================================================================
"""

import sys

# Ensure UTF-8 output encoding across all Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# =============================================================================
# PART 1: PYTHON LISTS & MUTABLE OPERATIONS
# =============================================================================
print("=" * 65)
print(">>> PART 1: PYTHON LISTS & MUTABLE OPERATIONS <<<")
print("=" * 65)

# 1. Creating a list of monthly sales targets
monthly_sales = [45000, 52000, 61000, 58000, 72000]
print(f"• Initial Sales List: {monthly_sales}")

# 2. Slicing & Indexing
print(f"  First Month Sales (index 0)   : Rs. {monthly_sales[0]:,}")
print(f"  Last Month Sales (index -1)   : Rs. {monthly_sales[-1]:,}")
print(f"  Q1 Sales (slice 0:3)          : {monthly_sales[0:3]}")

# 3. In-place List Modifications
monthly_sales.append(81000)               # Append single item to end
monthly_sales.insert(1, 49000)             # Insert at index 1
monthly_sales.extend([89000, 95000])       # Add multiple items from another list

print(f"\n• List after append/insert/extend:")
print(f"  {monthly_sales}")

# 4. Removing items
popped_val = monthly_sales.pop()           # Removes and returns last item
monthly_sales.remove(49000)                # Removes first occurrence of specific value
print(f"• After popping '{popped_val}' and removing '49000':")
print(f"  {monthly_sales}")

# 5. Sorting & Reversing
monthly_sales.sort(reverse=True)           # Sorts descending in-place
print(f"• Sorted Descending (Highest to Lowest): {monthly_sales}")


# =============================================================================
# PART 2: PYTHON TUPLES & DATA INTEGRITY UNPACKING
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 2: PYTHON TUPLES & IMMUTABILITY <<<")
print("=" * 65)

# Tuples are immutable: Once created, elements cannot be altered or appended.
# Perfect for database coordinates, geographic locations, and fixed metadata.
warehouse_location = ("Warehouse-North", 28.6139, 77.2090, "Active")

# Tuple Unpacking: Assigning elements directly to descriptive variables
wh_id, latitude, longitude, status = warehouse_location

print(f"• Warehouse Record Tuple: {warehouse_location}")
print(f"  ID        : {wh_id}")
print(f"  GPS Coords: ({latitude}, {longitude})")
print(f"  Status    : {status}")

# Tuple immutability demonstration
try:
    warehouse_location[3] = "Inactive"  # Will trigger TypeError
except TypeError as error:
    print(f"\n• Immutability Proof: Cannot modify tuple -> {error}")


# =============================================================================
# PART 3: PYTHON SETS & RELATIONAL SET OPERATIONS
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 3: PYTHON SETS (UNIQUE VALUES & VENN OPERATIONS) <<<")
print("=" * 65)

# Sets automatically eliminate duplicate entries
raw_customer_emails = [
    "user1@gmail.com", "sales@corp.in", "user1@gmail.com", 
    "ceo@startup.io", "sales@corp.in", "student@ysm.com"
]
unique_emails = set(raw_customer_emails)

print(f"• Raw Email Count   : {len(raw_customer_emails)} (Contains duplicates)")
print(f"• Unique Email Count: {len(unique_emails)} -> {unique_emails}")

# Relational Set Mathematics (Venn Diagram operations)
jan_buyers = {"Aarav", "Neha", "Rohan", "Priya", "Vikram"}
feb_buyers = {"Priya", "Vikram", "Sneha", "Karan", "Aarav"}

print("\n• Customer Cohort Comparison:")
print(f"  January Buyers: {jan_buyers}")
print(f"  February Buyers: {feb_buyers}")

# Union: Total unique customers across both months
total_customers = jan_buyers.union(feb_buyers)
print(f"  Union (Total Unique Customers)     : {total_customers}")

# Intersection: Returning / Repeat customers who bought in BOTH months
repeat_customers = jan_buyers.intersection(feb_buyers)
print(f"  Intersection (Repeat Buyers in Both): {repeat_customers}")

# Difference: Churned customers (Bought in Jan but NOT in Feb)
churned_jan_customers = jan_buyers.difference(feb_buyers)
print(f"  Difference (Jan only, Churned)     : {churned_jan_customers}")

# Symmetric Difference: Customers who bought in EXACTLY ONE of the months
single_month_buyers = jan_buyers.symmetric_difference(feb_buyers)
print(f"  Symmetric Difference (Non-Repeat)  : {single_month_buyers}")


# =============================================================================
# PART 4: PYTHON DICTIONARIES & NESTED ANALYTICS RECORDS
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 4: PYTHON DICTIONARIES (KEY-VALUE PAIRS) <<<")
print("=" * 65)

# Dictionary representing an enterprise sales account
client_account = {
    "account_id": "ACC-9042",
    "company_name": "Apex Logistics Pvt Ltd",
    "industry": "Supply Chain",
    "contract_value": 350000,
    "is_active": True,
    "contact_persons": ["Rajesh Sharma", "Sunita Rao"]
}

print(f"• Account Overview:")
print(f"  Company Name   : {client_account['company_name']}")
print(f"  Contract Value : Rs. {client_account['contract_value']:,}")

# Safe retrieval using .get() (Prevents KeyError if key does not exist)
renewal_date = client_account.get("renewal_date", "Pending Schedule")
print(f"  Renewal Date   : {renewal_date} (Retrieved via .get() with default)")

# Updating and adding key-value pairs
client_account["contract_value"] += 50000  # Upsell expansion
client_account["lead_analyst"] = "Sahil Shaikh"

print("\n• Updated Account Details:")
for key, value in client_account.items():
    print(f"  {key:<18}: {value}")


# =============================================================================
# PART 5: COMPREHENSIONS (LIST, DICTIONARY & SET)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 5: COMPREHENSIONS (DATA TRANSFORMATIONS) <<<")
print("=" * 65)

# 1. List Comprehension: Filtering and transforming transactions
transactions = [120, 850, 4200, 95, 12000, 310, 6500]

# Keep only high-value orders (>= 1000) and convert to USD (Assuming 1 USD = 80 INR)
high_value_usd = [round(amt / 80, 2) for amt in transactions if amt >= 1000]
print(f"• Raw Transactions (INR)      : {transactions}")
print(f"• High Value Orders (>= Rs 1000 in USD): {high_value_usd}")

# 2. Dictionary Comprehension: Converting product pricing table
product_prices_inr = {"Laptop": 65000, "Monitor": 18000, "Mouse": 1200, "Keyboard": 2500}
discounted_prices = {product: round(price * 0.90, 2) for product, price in product_prices_inr.items()}

print("\n• Original vs 10% Discounted Catalog (Dict Comprehension):")
for item, disc_price in discounted_prices.items():
    print(f"  {item:<10} -> Original: Rs. {product_prices_inr[item]:,} | Discounted: Rs. {disc_price:,}")

# 3. Set Comprehension: Extracting unique departments
employee_records = [
    {"name": "Amit", "dept": "IT"},
    {"name": "Sneha", "dept": "Finance"},
    {"name": "Vikram", "dept": "IT"},
    {"name": "Pooja", "dept": "HR"},
    {"name": "Divya", "dept": "Finance"}
]
all_departments = {emp["dept"] for emp in employee_records}
print(f"\n• Unique Departments (Set Comprehension): {all_departments}")


# =============================================================================
# PART 6: BUILT-IN COLLECTION AGGREGATORS & UTILITIES
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 6: COLLECTION STATISTICAL UTILITIES <<<")
print("=" * 65)

daily_store_visits = [420, 580, 710, 630, 890, 940, 780]

print(f"• Daily Visits Array : {daily_store_visits}")
print(f"  Total Weekly Footfall: {sum(daily_store_visits):,} visitors")
print(f"  Lowest Single Day    : {min(daily_store_visits)} visitors")
print(f"  Peak Footfall Day    : {max(daily_store_visits)} visitors")
print(f"  Average Daily Visits : {sum(daily_store_visits) / len(daily_store_visits):.1f} visitors")

# all() and any() boolean verifications
compliance_passed = [True, True, True, True]
print(f"\n• Are all security checks passed? all(checks) -> {all(compliance_passed)}")

fraud_flags = [False, False, True, False]
print(f"• Is any transaction suspicious? any(flags)   -> {any(fraud_flags)}")


# =============================================================================
# PART 7: MINI-PROJECT: BASKET ANALYSIS & REPEAT PURCHASE ENGINE
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 7: MINI-PROJECT: E-COMMERCE CART & COHORT ANALYSIS <<<")
print("=" * 65)

orders = [
    {"order_id": 101, "customer": "Aarav", "items": ["Laptop", "Mouse"], "total": 66200},
    {"order_id": 102, "customer": "Neha",  "items": ["Monitor", "HDMI Cable"], "total": 19500},
    {"order_id": 103, "customer": "Aarav", "items": ["Keyboard", "Mousepad"], "total": 3500},
    {"order_id": 104, "customer": "Rohan", "items": ["Laptop", "Cooling Pad"], "total": 68000},
    {"order_id": 105, "customer": "Neha",  "items": ["Desk Lamp"], "total": 1800}
]

# 1. Total revenue
total_revenue = sum(o["total"] for o in orders)

# 2. Customer spend aggregator
customer_spend = {}
for o in orders:
    cust = o["customer"]
    customer_spend[cust] = customer_spend.get(cust, 0) + o["total"]

# 3. Unique items sold across all orders
all_items_sold = {item for o in orders for item in o["items"]}

print(f"• Grand E-Commerce Revenue : Rs. {total_revenue:,}")
print(f"• Unique Items Catalog Sold: {sorted(list(all_items_sold))}")
print("\n• Customer Lifetime Value (CLV):")
for cust, spend in sorted(customer_spend.items(), key=lambda x: x[1], reverse=True):
    print(f"  Customer: {cust:<8} | Total Spend: Rs. {spend:,}")

print("=" * 65)
print(">>> TOPIC 02 COMPLETE: COLLECTIONS & DATA STRUCTURES MASTERED <<<")
print("=" * 65)
