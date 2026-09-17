"""
=============================================================================
EXCEL PRACTICE WORKBOOK GENERATOR (FOR STUDENTS & INSTRUCTORS)
=============================================================================
Generates ready-to-use hands-on Excel practice spreadsheets with:
  1. 'Raw_Dirty_Data'     -> For Sorting, Filtering, and Data Validation tasks
  2. 'Formulas_Practice'  -> For XLOOKUP, VLOOKUP, INDEX-MATCH, IF & SUMIFS
  3. 'Dashboard_Dataset'  -> 500 clean rows for Pivot Tables, Slicers & Charts
  4. 'Solved_Reference'   -> Self-check answer key with exact formulas
=============================================================================
"""

import sys
import os
import pandas as pd
import numpy as np

# Ensure UTF-8 output encoding across all Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "sales_analytics_master_practice.xlsx")

print("=" * 65)
print(">>> GENERATING EXCEL MASTERCLASS PRACTICE WORKBOOK <<<")
print("=" * 65)

# -------------------------------------------------------------
# Sheet 1: Raw Dirty Data
# -------------------------------------------------------------
dirty_records = {
    "Order_ID": [f"ORD-{i:04d}" for i in range(101, 126)],
    "Customer_Name": [
        "Aarav Sharma", "neha verma", "Rohan Gupta", "Priya Nair", "karan johar",
        "Sneha Rao", "Aarav Sharma", "Vikram Rathore", "Divya Sen", "Amit Patel",
        "Pooja Hegde", "Rahul Roy", "Suresh Raina", "Anjali Mehta", "Rohit Verma",
        "Deepak Chahar", "Kavita Rao", "Manoj Tiwari", "Sunita Sharma", "Harsh Goel",
        "Pooja Hegde", "Gaurav Sen", "Meena Kumari", "Rajesh Khanna", "Aarav Sharma"
    ],
    "Region": [
        "North", "north", "West", "South", "East",
        "West", "North", "WEST", "East", "South",
        "North", "West", "South", "East", "North",
        "North", "West", "South", "East", "North",
        "North", "South", "West", "East", "North"
    ],
    "Order_Amount": [
        15000, 22000, 8500, 45000, 12000,
        64000, 15000, 31000, 9200, 18500,
        52000, 75000, 11000, 34000, 28000,
        14000, 42000, 19000, 88000, 23000,
        52000, 17500, 39000, 61000, 15000
    ],
    "Payment_Status": [
        "Completed", "Completed", "Pending", "Completed", "Failed",
        "Completed", "Completed", "Completed", "Pending", "Completed",
        "Completed", "Completed", "Pending", "Completed", "Completed",
        "Completed", "Failed", "Completed", "Completed", "Pending",
        "Completed", "Completed", "Completed", "Completed", "Completed"
    ]
}
df_dirty = pd.DataFrame(dirty_records)

# -------------------------------------------------------------
# Sheet 2: Formulas & Lookups Practice
# -------------------------------------------------------------
# Master Employee Salary Table (Lookup source)
lookup_catalog = {
    "Emp_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Employee_Name": ["Rahul Roy", "Pooja Hegde", "Amit Patel", "Sneha Rao", "Karan Johar", "Vikram Rathore", "Divya Sen", "Aarav Sharma"],
    "Department": ["IT", "HR", "IT", "Finance", "Marketing", "IT", "Finance", "Data Analytics"],
    "Base_Salary": [65000, 52000, 95000, 80000, 72000, 68000, 84000, 88000],
    "Experience_Yrs": [3, 5, 11, 7, 15, 4, 9, 6]
}
df_lookup = pd.DataFrame(lookup_catalog)

# -------------------------------------------------------------
# Sheet 3: Dashboard Transactions Dataset (500 Rows)
# -------------------------------------------------------------
np.random.seed(42)
n_rows = 500

regions = ["North", "South", "East", "West"]
categories = ["Electronics", "Home & Furniture", "Office Supplies", "Apparel"]
reps = ["Aarav", "Pooja", "Vikram", "Sneha", "Rohan", "Neha"]
products_map = {
    "Electronics": [("Laptop Pro 15", 75000, 55000), ("Wireless Headphone", 4500, 2800), ("4K Monitor 27", 26000, 19000)],
    "Home & Furniture": [("Ergonomic Office Chair", 12500, 8500), ("Standing Desk", 22000, 16000), ("LED Desk Lamp", 1800, 950)],
    "Office Supplies": [("Gel Pens Pack 20", 350, 180), ("Spiral Notebook A4", 220, 110), ("Paper Shredder", 5500, 3800)],
    "Apparel": [("Corporate Blazer", 6500, 4200), ("Formal Cotton Shirt", 1800, 1100), ("Leather Laptop Bag", 3800, 2400)]
}

dates = pd.date_range(start="2026-01-01", end="2026-06-30", periods=n_rows)

dashboard_rows = []
for i in range(n_rows):
    region = np.random.choice(regions)
    rep = np.random.choice(reps)
    cat = np.random.choice(categories)
    prod_info = products_map[cat][np.random.randint(len(products_map[cat]))]
    prod_name, unit_price, unit_cost = prod_info
    qty = np.random.randint(1, 10)
    
    revenue = qty * unit_price
    total_cost = qty * unit_cost
    profit = revenue - total_cost
    
    dashboard_rows.append({
        "Transaction_ID": f"TXN-{1000 + i}",
        "Date": dates[i].strftime("%Y-%m-%d"),
        "Region": region,
        "Sales_Rep": rep,
        "Category": cat,
        "Product": prod_name,
        "Quantity": qty,
        "Unit_Price": unit_price,
        "Unit_Cost": unit_cost,
        "Total_Revenue": revenue,
        "Total_Cost": total_cost,
        "Gross_Profit": profit
    })

df_dashboard = pd.DataFrame(dashboard_rows)

# -------------------------------------------------------------
# Sheet 4: Solved Reference Guide
# -------------------------------------------------------------
reference_guide = {
    "Practice Task": [
        "Lookup Salary for Emp_ID 104 using XLOOKUP",
        "Lookup Department for Emp_ID 103 using INDEX-MATCH",
        "Calculate Total Revenue for 'Electronics' in 'West' region",
        "Count completed orders with amount > 25,000",
        "Determine Bonus Tier based on Experience (>8 yrs = 20%, >4 yrs = 10%, else 5%)"
    ],
    "Exact Excel Formula Syntax": [
        '=XLOOKUP(104, Formulas_Practice!$A$2:$A$9, Formulas_Practice!$D$2:$D$9, "Not Found")',
        '=INDEX(Formulas_Practice!$C$2:$C$9, MATCH(103, Formulas_Practice!$A$2:$A$9, 0))',
        '=SUMIFS(Dashboard_Data!$J$2:$J$501, Dashboard_Data!$E$2:$E$501, "Electronics", Dashboard_Data!$C$2:$C$501, "West")',
        '=COUNTIFS(Raw_Dirty_Data!$D$2:$D$26, ">25000", Raw_Dirty_Data!$E$2:$E$26, "Completed")',
        '=IFS(E2>8, "20% Bonus", E2>4, "10% Bonus", TRUE, "5% Bonus")'
    ],
    "Expected Output / Business Result": [
        "Rs. 80,000",
        "IT",
        f"Rs. {df_dashboard[(df_dashboard['Category']=='Electronics') & (df_dashboard['Region']=='West')]['Total_Revenue'].sum():,}",
        f"{len(df_dirty[(df_dirty['Order_Amount'] > 25000) & (df_dirty['Payment_Status'] == 'Completed')])} Orders",
        "Calculated dynamically per employee row"
    ]
}
df_reference = pd.DataFrame(reference_guide)

# -------------------------------------------------------------
# Writing to Multi-Sheet Excel File
# -------------------------------------------------------------
with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
    df_dirty.to_excel(writer, sheet_name="Raw_Dirty_Data", index=False)
    df_lookup.to_excel(writer, sheet_name="Formulas_Practice", index=False)
    df_dashboard.to_excel(writer, sheet_name="Dashboard_Data", index=False)
    df_reference.to_excel(writer, sheet_name="Solved_Reference", index=False)

print(f"• Successfully created: '{OUTPUT_FILE}'")
print("  - Sheet 1: 'Raw_Dirty_Data' (Sorting, Filtering, Drop-down validation)")
print("  - Sheet 2: 'Formulas_Practice' (XLOOKUP, VLOOKUP, INDEX-MATCH)")
print("  - Sheet 3: 'Dashboard_Data' (500 rows for Pivot Tables & Slicers)")
print("  - Sheet 4: 'Solved_Reference' (Answer Key with exact formula syntax)")
print("=" * 65)
print(">>> EXCEL WORKBOOK READY FOR STUDENT PRACTICE <<<")
print("=" * 65)
