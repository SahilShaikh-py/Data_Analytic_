"""
=============================================================================
TOPIC: PYTHON EXCEPTION HANDLING & FILE I/O (ROBUST DATA PIPELINES)
=============================================================================
Author: Python Mastery Course
Level: Intermediate (Production Data Engineering & Analytics)

Conceptual Overview:
--------------------
1. What is an Exception?
   - An exception is an error that occurs during program execution.
   - Without exception handling, an unhandled error crashes the entire pipeline.
   - With `try-except`, we gracefully catch errors, log warnings, and continue 
     processing remaining clean records.

2. Structure of Try-Except-Else-Finally:
   - `try`: Code that might raise an exception.
   - `except`: Code that executes if an exception occurs.
   - `else`: Code that executes ONLY if no exception occurred in `try`.
   - `finally`: Code that ALWAYS executes (cleanup, closing database/file connections).

3. File Handling with Context Managers (`with open(...)`):
   - Automatically closes the file stream even if an unexpected exception occurs.
   - Supports reading and writing Plain Text, CSV, and JSON data formats.

4. Topics Covered in this Guide:
   - Part 1: Try, Except, Else, Finally Blocks
   - Part 2: Catching Specific vs Multiple Exceptions
   - Part 3: Raising Custom User-Defined Exceptions
   - Part 4: Reading and Writing Plain Text Log Files
   - Part 5: Parsing & Generating Structured CSV Data with `csv` module
   - Part 6: Ingesting & Exporting Nested JSON Payloads with `json` module
   - Part 7: Real-world Practice: Automated ETL Ingestion & Error Audit Log
=============================================================================
"""

import sys
import os
import csv
import json

# Ensure UTF-8 output encoding across all Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# =============================================================================
# PART 1: TRY, EXCEPT, ELSE & FINALLY BLOCKS
# =============================================================================
print("=" * 65)
print(">>> PART 1: TRY, EXCEPT, ELSE & FINALLY <<<")
print("=" * 65)

def calculate_conversion_rate(clicks: int, conversions: int) -> float:
    try:
        rate = (conversions / clicks) * 100
    except ZeroDivisionError as err:
        print(f"  [Handled Error] Cannot divide by zero clicks: {err}")
        return 0.0
    else:
        print(f"  [Success] Conversion calculated without errors.")
        return rate
    finally:
        print(f"  [Cleanup] Calculation cycle completed.")

print("• Test 1: Normal Campaign Calculation:")
res1 = calculate_conversion_rate(1000, 45)
print(f"  Result: {res1:.2f}%\n")

print("• Test 2: Zero Clicks Campaign (Edge Case):")
res2 = calculate_conversion_rate(0, 0)
print(f"  Result: {res2:.2f}%")


# =============================================================================
# PART 2: CATCHING MULTIPLE SPECIFIC EXCEPTIONS
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 2: SPECIFIC EXCEPTION HIERARCHY <<<")
print("=" * 65)

dirty_input_records = [
    {"user_id": 101, "age": "28", "salary": "75000"},
    {"user_id": 102, "age": "N/A", "salary": "52000"},       # Invalid integer (ValueError)
    {"user_id": 103, "salary": "85000"},                      # Missing age key (KeyError)
    {"user_id": 104, "age": "32", "salary": "120000"}
]

clean_records = []

for record in dirty_input_records:
    try:
        uid = record["user_id"]
        age = int(record["age"])
        salary = float(record["salary"])
        clean_records.append({"user_id": uid, "age": age, "salary": salary})
    except KeyError as key_err:
        print(f"• Missing Field in Record {record.get('user_id', 'Unknown')}: Missing key '{key_err.args[0]}'")
    except ValueError as val_err:
        print(f"• Type Conversion Failure in Record {record.get('user_id', 'Unknown')}: {val_err}")

print(f"\n• Successfully Sanitized Records: {clean_records}")


# =============================================================================
# PART 3: CUSTOM USER-DEFINED EXCEPTIONS
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 3: CUSTOM BUSINESS EXCEPTIONS <<<")
print("=" * 65)

class NegativeRevenueError(Exception):
    """Raised when incoming sales transactions contain an invalid negative amount."""
    def __init__(self, amount, transaction_id):
        self.amount = amount
        self.transaction_id = transaction_id
        super().__init__(f"Transaction '{transaction_id}' rejected: Negative revenue amount Rs. {amount} is illegal.")

def process_transaction(txn_id: str, amount: float):
    if amount < 0:
        raise NegativeRevenueError(amount, txn_id)
    print(f"• Transaction '{txn_id}' of Rs. {amount:,.2f} recorded successfully.")

# Testing normal and anomalous transactions
try:
    process_transaction("TXN-901", 15400)
    process_transaction("TXN-902", -3500)
except NegativeRevenueError as custom_err:
    print(f"• Caught Custom Exception: {custom_err}")


# =============================================================================
# PART 4: READING & WRITING TEXT LOG FILES
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 4: TEXT FILE I/O WITH CONTEXT MANAGER <<<")
print("=" * 65)

log_filename = "audit_pipeline.log"

# Writing log entries to a text file
with open(log_filename, mode="w", encoding="utf-8") as file:
    file.write("[INFO] 2026-09-18 09:00:00 - Data Pipeline Started\n")
    file.write("[INFO] 2026-09-18 09:01:15 - Ingested 1500 sales records\n")
    file.write("[WARNING] 2026-09-18 09:01:30 - 3 records dropped due to null keys\n")
    file.write("[SUCCESS] 2026-09-18 09:02:00 - Pipeline Completed\n")

print(f"• Created Text Log File: '{log_filename}'")

# Reading back the log file lines
print("• Reading Log File Lines:")
with open(log_filename, mode="r", encoding="utf-8") as file:
    for line in file:
        print(f"  -> {line.strip()}")


# =============================================================================
# PART 5: STRUCTURED CSV FILE READING & WRITING
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 5: CSV GENERATION & PARSING (CSV MODULE) <<<")
print("=" * 65)

csv_filename = "sample_products.csv"
product_data = [
    ["Product_ID", "Product_Name", "Category", "Price", "Stock_Units"],
    [101, "Dell UltraSharp 27 Monitor", "Hardware", 28500, 45],
    [102, "Logitech MX Master 3S", "Accessories", 8900, 120],
    [103, "Keychron K2 Mechanical Keyboard", "Accessories", 7500, 60],
    [104, "Apple MacBook Pro M3", "Computers", 169000, 15]
]

# Writing CSV using csv.writer
with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(product_data)
print(f"• Generated CSV: '{csv_filename}'")

# Reading CSV using csv.DictReader (Parses directly into dictionary rows)
print("\n• Parsing CSV Rows with csv.DictReader:")
with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(f"  Product: {row['Product_Name']:<32} | Price: Rs. {float(row['Price']):<10,.2f} | Stock: {row['Stock_Units']}")


# =============================================================================
# PART 6: JSON INGESTION & EXPORT (API PAYLOADS)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 6: JSON PARSING & EXPORT (JSON MODULE) <<<")
print("=" * 65)

analytics_report_dict = {
    "report_title": "Monthly Marketing Performance",
    "generated_at": "2026-09-18",
    "metrics": {
        "total_ad_spend_inr": 125000,
        "leads_generated": 840,
        "cost_per_lead": round(125000 / 840, 2),
        "channels": ["Google Ads", "LinkedIn", "Meta"]
    }
}

json_filename = "campaign_metrics.json"

# Serializing python dictionary to JSON file
with open(json_filename, mode="w", encoding="utf-8") as json_file:
    json.dump(analytics_report_dict, json_file, indent=4)
print(f"• Exported JSON Report to '{json_filename}'")

# Deserializing JSON file back into Python dictionary
with open(json_filename, mode="r", encoding="utf-8") as json_file:
    loaded_data = json.load(json_file)

print(f"\n• Read Back JSON Data:")
print(f"  Title          : {loaded_data['report_title']}")
print(f"  Total Spend    : Rs. {loaded_data['metrics']['total_ad_spend_inr']:,}")
print(f"  Cost Per Lead  : Rs. {loaded_data['metrics']['cost_per_lead']}")
print(f"  Active Channels: {', '.join(loaded_data['metrics']['channels'])}")


# =============================================================================
# PART 7: MINI-PROJECT: ROBUST ETL INGESTION WITH CORRUPT ROW QUARANTINE
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 7: MINI-PROJECT: RESILIENT ETL PIPELINE <<<")
print("=" * 65)

raw_incoming_batch = [
    {"row_id": 1, "customer": "Aarav", "items_count": 3, "amount": 15000},
    {"row_id": 2, "customer": "Neha",  "items_count": 0, "amount": 0},      # Zero items error
    {"row_id": 3, "customer": "Rohan", "items_count": "two", "amount": 8000},# Corrupt int string
    {"row_id": 4, "customer": "Priya", "items_count": 5, "amount": 32000},
]

valid_orders = []
quarantine_log = []

for order in raw_incoming_batch:
    try:
        count = int(order["items_count"])
        if count <= 0:
            raise ValueError("Item count must be strictly greater than zero.")
        
        avg_item_price = order["amount"] / count
        valid_orders.append({
            "order_id": order["row_id"],
            "customer": order["customer"],
            "total": order["amount"],
            "avg_unit_price": avg_item_price
        })
    except (ValueError, TypeError) as err:
        quarantine_log.append({"row_id": order["row_id"], "reason": str(err)})

print("• Valid Orders Processed:")
for v in valid_orders:
    print(f"  Order {v['order_id']} ({v['customer']}): Total Rs. {v['total']:,} (Avg Rs. {v['avg_unit_price']:,.2f} per unit)")

print("\n• Quarantined Corrupted Rows (Saved for Review):")
for q in quarantine_log:
    print(f"  [QUARANTINED] Row {q['row_id']} rejected -> Reason: {q['reason']}")

# Clean up generated temporary demo files
for temp_file in [log_filename, csv_filename, json_filename]:
    if os.path.exists(temp_file):
        os.remove(temp_file)

print("\n• Temporary audit files cleaned up successfully.")
print("=" * 65)
print(">>> TOPIC 08 COMPLETE: EXCEPTIONS & FILE I/O MASTERED <<<")
print("=" * 65)
