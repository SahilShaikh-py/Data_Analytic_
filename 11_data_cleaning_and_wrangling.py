"""
=============================================================================
TOPIC: DATA CLEANING & WRANGLING MASTERCLASS (PANDAS PIPELINE)
=============================================================================
Author: Python Mastery Course
Level: Intermediate to Advanced (Essential for Industry Data Analysts)

Conceptual Overview:
--------------------
1. Why Data Cleaning Matters:
   - "Garbage in, Garbage out": Machine learning models and executive dashboards 
     are only as good as the underlying data quality.
   - Real-world corporate data is notorious for missing values, duplicate entries, 
     inconsistent data types, and non-standardized timestamps.

2. Core Operations in this Masterclass:
   - Profiling Data Quality (Null value counts, duplicate detection)
   - Strategic Imputation (Mean, Median, Mode, Forward Fill)
   - Deduplication & Primary Key Integrity
   - Type Casting & Coercion (`pd.to_numeric`, `astype`)
   - Text Normalization & String Sanitization (strip, replace, regex)
   - DateTime Parsing & Calendar Feature Engineering

3. Topics Covered in this Guide:
   - Part 1: Initial Data Profiling & Health Assessment
   - Part 2: Handling Missing Values (Imputation vs Deletion)
   - Part 3: Duplicate Detection & Removal
   - Part 4: Data Type Correction & Error Coercion
   - Part 5: Text Sanitization & String Standardization
   - Part 6: DateTime Parsing & Feature Engineering
   - Part 7: Real-world Practice: Full End-to-End Raw Ingestion Cleaning Pipeline
=============================================================================
"""

import sys
import pandas as pd
import numpy as np

# Ensure UTF-8 output encoding across all Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Display settings for clean terminal output
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 1000)

# =============================================================================
# PART 1: INITIAL DATA PROFILING & HEALTH ASSESSMENT
# =============================================================================
print("=" * 65)
print(">>> PART 1: RAW DATA INGESTION & QUALITY PROFILING <<<")
print("=" * 65)

# Simulating messy e-commerce customer transaction records
raw_data = {
    "Transaction_ID": ["TXN-101", "TXN-102", "TXN-103", "TXN-104", "TXN-105", "TXN-101", "TXN-106", "TXN-107"],
    "Customer_Name": ["  Aarav Sharma ", "neha VERMA", "Rohan Gupta", np.nan, "Priya Nair", "  Aarav Sharma ", "Karan Johar", "Sneha Rao"],
    "Age": ["28", "34", "invalid", "29", np.nan, "28", "45", "31"],
    "Order_Amount": ["Rs. 15,000", "22500", "8,900", "N/A", "45000", "Rs. 15,000", "12000", "64000"],
    "Payment_Method": ["Credit Card", "UPI", "UPI", "Net Banking", np.nan, "Credit Card", "Debit Card", "UPI"],
    "Purchase_Date": ["2026/01/15", "15-01-2026", "2026.01.18", "2026-01-20", "22-01-2026", "2026/01/15", "2026-01-25", "2026-02-01"]
}

df = pd.DataFrame(raw_data)
print("• Raw Dirty DataFrame:")
print(df)

print("\n• Data Quality Health Check:")
print(f"  Shape (Rows, Columns): {df.shape}")
print(f"  Missing Values per Column:\n{df.isna().sum()}")
print(f"  Duplicate Rows Detected: {df.duplicated().sum()}")


# =============================================================================
# PART 2: DUPLICATE DETECTION & REMOVAL
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 2: DETECTING & DROPPING DUPLICATES <<<")
print("=" * 65)

# Check duplicate records based on primary identifier 'Transaction_ID'
duplicates_found = df[df.duplicated(subset=["Transaction_ID"], keep=False)]
print("• Duplicate Transactions Found in Batch:")
print(duplicates_found[["Transaction_ID", "Customer_Name", "Order_Amount"]])

# Drop duplicate rows, keeping the first valid occurrence
df_clean = df.drop_duplicates(subset=["Transaction_ID"], keep="first").copy()
print(f"\n• Rows count after deduplication: {len(df_clean)} (Removed {len(df) - len(df_clean)} duplicate rows)")


# =============================================================================
# PART 3: TEXT SANITIZATION & STRING NORMALIZATION
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 3: STRING SANITIZATION & TITLE CASING <<<")
print("=" * 65)

# 1. Fill missing customer name with 'Valued Customer'
df_clean["Customer_Name"] = df_clean["Customer_Name"].fillna("Valued Customer")

# 2. Strip leading/trailing whitespaces and convert to Title Case (e.g. 'neha VERMA' -> 'Neha Verma')
df_clean["Customer_Name"] = df_clean["Customer_Name"].str.strip().str.title()

# 3. Clean Order_Amount column: Remove 'Rs.', commas, spaces, and replace 'N/A' with NaN
df_clean["Order_Amount"] = (
    df_clean["Order_Amount"]
    .astype(str)
    .str.replace("Rs.", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
    .replace("N/A", np.nan)
)

print("• Cleaned Customer Names & Sanitized Order Amounts:")
print(df_clean[["Transaction_ID", "Customer_Name", "Order_Amount"]])


# =============================================================================
# PART 4: DATA TYPE CORRECTION & NUMERIC COERCION
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 4: NUMERIC CONVERSION & COERCION <<<")
print("=" * 65)

# Convert 'Age' to numeric. 'invalid' will safely become NaN using errors='coerce'
df_clean["Age"] = pd.to_numeric(df_clean["Age"], errors="coerce")

# Convert 'Order_Amount' to float
df_clean["Order_Amount"] = pd.to_numeric(df_clean["Order_Amount"], errors="coerce")

print("• Column Data Types after Coercion:")
print(df_clean.dtypes)
print("\n• Null Count after Coercion:")
print(df_clean[["Age", "Order_Amount"]].isna().sum())


# =============================================================================
# PART 5: STRATEGIC MISSING VALUE IMPUTATION
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 5: STRATEGIC MISSING VALUE IMPUTATION <<<")
print("=" * 65)

# Strategy 1: Impute numerical 'Age' with Median (Median is robust against outliers)
median_age = df_clean["Age"].median()
df_clean["Age"] = df_clean["Age"].fillna(median_age).astype(int)
print(f"• Imputed Missing Age with Median Value: {median_age:.0f} years")

# Strategy 2: Impute 'Order_Amount' with Mean order value
mean_amount = df_clean["Order_Amount"].mean()
df_clean["Order_Amount"] = df_clean["Order_Amount"].fillna(mean_amount).round(2)
print(f"• Imputed Missing Order Amount with Mean: Rs. {mean_amount:,.2f}")

# Strategy 3: Impute categorical 'Payment_Method' with Mode (Most frequent value)
mode_payment = df_clean["Payment_Method"].mode()[0]
df_clean["Payment_Method"] = df_clean["Payment_Method"].fillna(mode_payment)
print(f"• Imputed Missing Payment Method with Mode: '{mode_payment}'")


# =============================================================================
# PART 6: DATETIME PARSING & CALENDAR FEATURE ENGINEERING
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 6: DATETIME STANDARDIZATION & FEATURE EXTRACTION <<<")
print("=" * 65)

# Convert varied date formats ("2026/01/15", "15-01-2026", "2026.01.18") into standardized ISO Timestamp
df_clean["Purchase_Date"] = pd.to_datetime(df_clean["Purchase_Date"], format="mixed")

# Feature Engineering: Extracting calendar dimensions for BI reporting
df_clean["Year"] = df_clean["Purchase_Date"].dt.year
df_clean["Month_Name"] = df_clean["Purchase_Date"].dt.month_name()
df_clean["Day_Name"] = df_clean["Purchase_Date"].dt.day_name()
df_clean["Quarter"] = df_clean["Purchase_Date"].dt.to_period("Q").astype(str)
df_clean["Is_Weekend"] = df_clean["Purchase_Date"].dt.dayofweek >= 5

print("• Engineered Date Attributes:")
print(df_clean[["Transaction_ID", "Purchase_Date", "Month_Name", "Day_Name", "Quarter", "Is_Weekend"]])


# =============================================================================
# PART 7: FINAL WRANGLED DATASET & SUMMARY METRICS
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 7: FINAL CLEANED ANALYTICAL DATASET <<<")
print("=" * 65)

# Reset index for clean sequential ordering
df_clean.reset_index(drop=True, inplace=True)

print(df_clean[["Transaction_ID", "Customer_Name", "Age", "Order_Amount", "Payment_Method", "Day_Name"]])

print("\n• Verification of Zero Missing Values:")
print(f"  Remaining Null Values: {df_clean.isna().sum().sum()}")
print(f"  Total Cleaned Revenue: Rs. {df_clean['Order_Amount'].sum():,.2f}")
print(f"  Average Basket Size  : Rs. {df_clean['Order_Amount'].mean():,.2f}")

print("=" * 65)
print(">>> TOPIC 11 COMPLETE: DATA CLEANING & WRANGLING MASTERED <<<")
print("=" * 65)
