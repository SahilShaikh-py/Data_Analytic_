"""
=============================================================================
TOPIC: PYTHON + SQL RELATIONAL DATABASE PIPELINE (SQLITE & PANDAS)
=============================================================================
Author: Python Mastery Course
Level: Intermediate to Advanced (Data Engineering & Business Intelligence)

Conceptual Overview:
--------------------
1. Why Python + SQL Integration?
   - SQL is the gold standard for querying and extracting structured enterprise data.
   - Python + Pandas provides advanced manipulation, statistics, and automation.
   - In production workflows, analysts query millions of rows from a database (SQL), 
     perform feature engineering in Pandas, and load cleaned results back to the database.

2. SQLite in Python:
   - Python comes bundled with the built-in `sqlite3` library (zero installation).
   - It implements a complete, standards-compliant ACID relational database engine 
     that supports all standard ANSI SQL syntax (SELECT, WHERE, GROUP BY, JOIN, HAVING).

3. Topics Covered in this Guide:
   - Part 1: SQLite Database Connection & Cursor Architecture
   - Part 2: Creating Relational Tables with Primary & Foreign Keys (DDL)
   - Part 3: Inserting Records via Python & Ingesting DataFrames (`df.to_sql`)
   - Part 4: Direct SQL Querying into Pandas DataFrames (`pd.read_sql_query`)
   - Part 5: Multi-Table Relational Joins in SQL (Customers, Orders, Products)
   - Part 6: Database-Level Aggregations & Metric Calculation (GROUP BY, HAVING)
   - Part 7: Real-world Practice: Automated End-to-End SQL Analytical Pipeline
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

# Display settings for clean tabular terminal formatting
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 1000)

DB_FILE = "enterprise_analytics.db"

# Remove old database file if exists to ensure clean execution
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

# =============================================================================
# PART 1: CONNECTING TO DATABASE & CURSOR INITIALIZATION
# =============================================================================
print("=" * 65)
print(">>> PART 1: SQLITE CONNECTION & CURSOR <<<")
print("=" * 65)

# Connect to database (Creates the file if it does not exist)
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

print(f"• Successfully connected to SQLite database: '{DB_FILE}'")
print(f"• SQLite Version: {sqlite3.sqlite_version}")


# =============================================================================
# PART 2: DDL SCHEMA CREATION (TABLES WITH PRIMARY & FOREIGN KEYS)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 2: CREATING RELATIONAL TABLES (DDL) <<<")
print("=" * 65)

# Enable foreign key constraint support in SQLite
cursor.execute("PRAGMA foreign_keys = ON;")

# Table 1: Customers
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    city TEXT NOT NULL,
    tier TEXT DEFAULT 'Standard'
);
""")

# Table 2: Products
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    unit_price REAL NOT NULL
);
""")

# Table 3: Orders (Foreign Keys referencing Customers and Products)
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
""")

conn.commit()
print("• Relational Database Schema Created Successfully:")
print("  - Table 'customers' (customer_id PK, name, city, tier)")
print("  - Table 'products' (product_id PK, name, category, unit_price)")
print("  - Table 'orders' (order_id PK, customer_id FK, product_id FK, quantity, date)")


# =============================================================================
# PART 3: DATA INGESTION (SQL INSERTS & PANDAS DF.TO_SQL)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 3: DATA POPULATION & DF.TO_SQL INGESTION <<<")
print("=" * 65)

# 1. Populating Customers table using executemany
customers_data = [
    (1, "Aarav Sharma", "Mumbai", "Platinum"),
    (2, "Neha Verma", "Delhi", "Gold"),
    (3, "Rohan Gupta", "Bangalore", "Silver"),
    (4, "Priya Nair", "Pune", "Platinum"),
    (5, "Vikram Rathore", "Mumbai", "Standard")
]
cursor.executemany("INSERT INTO customers VALUES (?, ?, ?, ?);", customers_data)

# 2. Populating Products table via Pandas DataFrame .to_sql()
products_df = pd.DataFrame([
    {"product_id": 101, "product_name": "Pro Wireless Mouse", "category": "Accessories", "unit_price": 2500.0},
    {"product_id": 102, "product_name": "Mechanical Keyboard", "category": "Accessories", "unit_price": 5500.0},
    {"product_id": 103, "product_name": "4K Ultra Monitor", "category": "Hardware", "unit_price": 32000.0},
    {"product_id": 104, "product_name": "Workstation Laptop", "category": "Computers", "unit_price": 85000.0}
])
products_df.to_sql("products", conn, if_exists="append", index=False)

# 3. Populating Orders table
orders_data = [
    (1, 104, 1, "2026-01-10"),  # Aarav bought Laptop
    (1, 101, 2, "2026-01-12"),  # Aarav bought 2 Mice
    (2, 103, 1, "2026-01-15"),  # Neha bought Monitor
    (3, 102, 1, "2026-01-18"),  # Rohan bought Keyboard
    (4, 104, 2, "2026-01-20"),  # Priya bought 2 Laptops
    (4, 102, 1, "2026-01-22"),  # Priya bought Keyboard
    (2, 101, 1, "2026-01-25"),  # Neha bought Mouse
]
cursor.executemany("INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES (?, ?, ?, ?);", orders_data)
conn.commit()

print(f"• Successfully populated tables: 5 Customers, 4 Products, 7 Orders.")


# =============================================================================
# PART 4: DIRECT SQL QUERYING WITH PANDAS (PD.READ_SQL_QUERY)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 4: QUERYING SQL DIRECTLY INTO PANDAS <<<")
print("=" * 65)

# Querying all platinum customers sorted by city
sql_platinum = """
SELECT customer_id, customer_name, city, tier
FROM customers
WHERE tier = 'Platinum'
ORDER BY customer_name ASC;
"""

df_platinum = pd.read_sql_query(sql_platinum, conn)
print("• Platinum Customers (pd.read_sql_query):")
print(df_platinum)


# =============================================================================
# PART 5: MULTI-TABLE RELATIONAL JOINS IN SQL
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 5: MULTI-TABLE SQL JOINS <<<")
print("=" * 65)

# Combining customers, orders, and products via INNER JOIN
sql_joined_orders = """
SELECT 
    o.order_id,
    o.order_date,
    c.customer_name,
    c.city,
    c.tier AS customer_tier,
    p.product_name,
    p.category,
    p.unit_price,
    o.quantity,
    (o.quantity * p.unit_price) AS total_order_value
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id
ORDER BY o.order_date ASC;
"""

df_master_orders = pd.read_sql_query(sql_joined_orders, conn)
print("• Consolidated Orders View Across 3 Joined Tables:")
print(df_master_orders[["order_id", "order_date", "customer_name", "product_name", "quantity", "total_order_value"]])


# =============================================================================
# PART 6: DATABASE-LEVEL AGGREGATIONS & METRICS (GROUP BY & HAVING)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 6: SQL AGGREGATIONS (GROUP BY & HAVING) <<<")
print("=" * 65)

# SQL Query calculating revenue and total orders per customer, filtering customers with revenue > Rs. 50,000
sql_customer_revenue = """
SELECT 
    c.customer_name,
    c.tier,
    c.city,
    COUNT(o.order_id) AS total_orders_placed,
    SUM(o.quantity * p.unit_price) AS total_lifetime_spend,
    AVG(o.quantity * p.unit_price) AS avg_order_value
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN products p ON o.product_id = p.product_id
GROUP BY c.customer_id, c.customer_name, c.tier, c.city
HAVING total_lifetime_spend > 50000
ORDER BY total_lifetime_spend DESC;
"""

df_high_value_clients = pd.read_sql_query(sql_customer_revenue, conn)
print("• High-Value Customers with Spend > Rs. 50,000 (GROUP BY + HAVING):")
print(df_high_value_clients)


# =============================================================================
# PART 7: AUTOMATED ANALYTICAL REPORT GENERATION
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 7: EXECUTING EXECUTIVE REVENUE REPORT <<<")
print("=" * 65)

# Revenue summary by category
sql_category_summary = """
SELECT 
    p.category,
    COUNT(o.order_id) AS total_units_sold,
    SUM(o.quantity * p.unit_price) AS category_revenue,
    ROUND((SUM(o.quantity * p.unit_price) * 100.0 / (
        SELECT SUM(o2.quantity * p2.unit_price) 
        FROM orders o2 
        INNER JOIN products p2 ON o2.product_id = p2.product_id
    )), 2) AS revenue_contribution_pct
FROM orders o
INNER JOIN products p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY category_revenue DESC;
"""

df_cat_summary = pd.read_sql_query(sql_category_summary, conn)
print("• Product Category Contribution Report:")
print(df_cat_summary)

# Close database connection cleanly
conn.close()
print("\n• Database connection closed safely.")

# Clean up database file after run
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
print(f"• Temporary database '{DB_FILE}' removed.")

print("=" * 65)
print(">>> TOPIC 15 COMPLETE: PYTHON + SQL PIPELINE MASTERED <<<")
print("=" * 65)
