"""
=============================================================================
INDUSTRY CAPSTONE: AUTOMATED PYTHON ETL & DATA WAREHOUSING PIPELINE
=============================================================================
Project: AuraKart Omni-Channel Customer Retention & Financial Analytics
Author: Data Analytics Masterclass
Deliverable: Cleaned Data Warehouse + Power BI Integration CSVs
=============================================================================
"""

import sys
import os
import sqlite3
import pandas as pd
import numpy as np

# Ensure UTF-8 output encoding across all Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 1000)

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "aurakart_analytics.db")

print("=" * 65)
print(">>> CAPSTONE ETL: INGESTION, SANITIZATION & METRIC MODELING <<<")
print("=" * 65)

# -------------------------------------------------------------
# STEP 1: GENERATING REALISTIC RAW ENTERPRISE DATASET
# -------------------------------------------------------------
np.random.seed(42)
n_orders = 600

customer_pool = [
    (101, "Aarav Sharma",   "Mumbai",    "Tier-1", "Organic Search"),
    (102, "Neha Verma",     "Delhi",     "Tier-1", "Instagram Ads"),
    (103, "Rohan Gupta",    "Bangalore", "Tier-1", "Google Ads"),
    (104, "Priya Nair",     "Pune",      "Tier-2", "Referral"),
    (105, "Vikram Rathore", "Mumbai",    "Tier-1", "Direct App"),
    (106, "Sneha Rao",      "Hyderabad", "Tier-2", "Instagram Ads"),
    (107, "Karan Johar",    "Delhi",     "Tier-1", "Google Ads"),
    (108, "Divya Sen",      "Kolkata",   "Tier-2", "Organic Search"),
    (109, "Amit Patel",     "Ahmedabad", "Tier-2", "Referral"),
    (110, "Pooja Hegde",    "Bangalore", "Tier-1", "Direct App")
]

products_catalog = [
    (501, "Smart Fitness Watch", "Electronics",  4500, 2400),
    (502, "Noise Cancelling Buds", "Electronics", 3200, 1600),
    (503, "Organic Green Tea Pack", "Grocery",    650,  320),
    (504, "Cold-Pressed Almond Oil", "Grocery",   850,  480),
    (505, "Ergonomic Memory Pillow", "Home",      2200, 1100),
    (506, "Ceramic Cookware Set", "Home",         5800, 3600),
    (507, "Cotton Athleisure Hoodie", "Apparel",  1800,  850),
    (508, "Running Training Shoes", "Apparel",    3500, 1900)
]

# Build DataFrames
df_cust = pd.DataFrame(customer_pool, columns=["CustomerID", "CustomerName", "City", "MarketTier", "AcquisitionChannel"])
df_prod = pd.DataFrame(products_catalog, columns=["ProductID", "ProductName", "Category", "SellingPrice", "UnitCost"])

order_dates = pd.date_range(start="2026-01-01", end="2026-06-30", periods=n_orders)

raw_orders = []
for i in range(n_orders):
    cust = customer_pool[np.random.randint(len(customer_pool))]
    prod = products_catalog[np.random.randint(len(products_catalog))]
    qty = np.random.randint(1, 6)
    
    # Introduce deliberate realistic anomalies (5% chance of corrupt data)
    noise = np.random.rand()
    if noise < 0.03:
        discount = -0.10  # Anomaly: Negative discount
    elif noise < 0.06:
        discount = 0.50   # Deep discount
    else:
        discount = np.random.choice([0.0, 0.05, 0.10, 0.15])
        
    payment = np.random.choice(["UPI", "Credit Card", "Debit Card", "Net Banking", "Cash on Delivery"], p=[0.45, 0.25, 0.15, 0.10, 0.05])
    
    raw_orders.append({
        "OrderID": f"ORD-{10000 + i}",
        "OrderDate": order_dates[i].strftime("%Y-%m-%d"),
        "CustomerID": cust[0],
        "ProductID": prod[0],
        "Quantity": qty,
        "DiscountApplied": discount,
        "PaymentMethod": payment,
        "DeliveryStatus": np.random.choice(["Delivered", "Delivered", "Delivered", "Cancelled", "Returned"], p=[0.82, 0.06, 0.04, 0.05, 0.03])
    })

df_raw_orders = pd.DataFrame(raw_orders)
print(f"• Generated {len(df_raw_orders)} Raw Transaction Records across {len(df_cust)} Customers and {len(df_prod)} Products.")


# -------------------------------------------------------------
# STEP 2: DATA CLEANING & FINANCIAL METRIC MODELING
# -------------------------------------------------------------
print("\n• Sanitizing Dirty Records:")
# 1. Filter out illegal negative discounts
invalid_discounts = len(df_raw_orders[df_raw_orders["DiscountApplied"] < 0])
df_clean_orders = df_raw_orders[df_raw_orders["DiscountApplied"] >= 0].copy()
print(f"  Dropped {invalid_discounts} corrupted rows containing negative discounts.")

# 2. Merge pricing metadata to compute line item financials
df_clean_orders = df_clean_orders.merge(df_prod[["ProductID", "SellingPrice", "UnitCost"]], on="ProductID", how="left")

# 3. Calculate Financial Metrics
df_clean_orders["GrossSales"] = df_clean_orders["Quantity"] * df_clean_orders["SellingPrice"]
df_clean_orders["DiscountAmount"] = np.round(df_clean_orders["GrossSales"] * df_clean_orders["DiscountApplied"], 2)
df_clean_orders["NetRevenue"] = np.round(df_clean_orders["GrossSales"] - df_clean_orders["DiscountAmount"], 2)
df_clean_orders["TotalCOGS"] = df_clean_orders["Quantity"] * df_clean_orders["UnitCost"]  # Cost of Goods Sold
df_clean_orders["GrossProfit"] = np.round(df_clean_orders["NetRevenue"] - df_clean_orders["TotalCOGS"], 2)
df_clean_orders["ProfitMarginPct"] = np.round((df_clean_orders["GrossProfit"] / df_clean_orders["NetRevenue"]) * 100, 2)

# 4. Standardize Date and extract calendar dimensions
df_clean_orders["OrderDate"] = pd.to_datetime(df_clean_orders["OrderDate"])
df_clean_orders["YearMonth"] = df_clean_orders["OrderDate"].dt.strftime("%Y-%m")
df_clean_orders["MonthName"] = df_clean_orders["OrderDate"].dt.month_name()
df_clean_orders["Quarter"] = df_clean_orders["OrderDate"].dt.to_period("Q").astype(str)

print("\n• Sample Sanitized Financial Transactions:")
print(df_clean_orders[["OrderID", "OrderDate", "Quantity", "GrossSales", "NetRevenue", "GrossProfit", "ProfitMarginPct"]].head(5))


# -------------------------------------------------------------
# STEP 3: EXPORTING TO SQL DATABASE WAREHOUSE & POWER BI CSVS
# -------------------------------------------------------------
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)

# Ingest DataFrames as Relational SQL Tables
df_cust.to_sql("dim_customers", conn, if_exists="replace", index=False)
df_prod.to_sql("dim_products", conn, if_exists="replace", index=False)
df_clean_orders.drop(columns=["SellingPrice", "UnitCost"]).to_sql("fact_orders", conn, if_exists="replace", index=False)
conn.commit()
conn.close()

print(f"\n• SQLite Enterprise Warehouse Created: '{DB_PATH}'")
print("  - Table 'dim_customers' (10 rows)")
print("  - Table 'dim_products' (8 rows)")
print(f"  - Table 'fact_orders' ({len(df_clean_orders)} clean rows)")

# Export clean CSVs for Power BI Desktop ingestion
csv_dir = os.path.join(BASE_DIR, "power_bi_export")
os.makedirs(csv_dir, exist_ok=True)

df_cust.to_csv(os.path.join(csv_dir, "Dim_Customers.csv"), index=False)
df_prod.to_csv(os.path.join(csv_dir, "Dim_Products.csv"), index=False)
df_clean_orders.drop(columns=["SellingPrice", "UnitCost"]).to_csv(os.path.join(csv_dir, "Fact_Orders.csv"), index=False)

print(f"• Exported Clean Power BI CSVs to: '{csv_dir}'")
print(f"  Total Net Revenue Processed: Rs. {df_clean_orders['NetRevenue'].sum():,.2f}")
print(f"  Total Gross Profit Produced: Rs. {df_clean_orders['GrossProfit'].sum():,.2f}")
print(f"  Overall Average Margin    : {((df_clean_orders['GrossProfit'].sum() / df_clean_orders['NetRevenue'].sum())*100):.2f}%")

print("=" * 65)
print(">>> CAPSTONE ETL STAGE COMPLETE: READY FOR SQL & POWER BI <<<")
print("=" * 65)
