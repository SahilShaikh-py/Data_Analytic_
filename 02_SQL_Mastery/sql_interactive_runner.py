"""
=============================================================================
TOPIC: SQL RELATIONAL DATABASE INTERACTIVE RUNNER (MySQL / SQLite COMPATIBLE)
=============================================================================
Author: Python Mastery Course
Level: Beginner to Advanced (100% ANSI SQL Compatible)

Conceptual Overview:
--------------------
Why use this Runner?
1. Students can run all SQL queries instantly without configuring MySQL Server.
2. Demonstrates standard ANSI SQL queries (SELECT, WHERE, GROUP BY, HAVING, 
   INNER/LEFT JOIN, and Nested Subqueries).
3. Produces cleanly formatted terminal ASCII tables using Pandas display options.
=============================================================================
"""

import sys
import sqlite3
import pandas as pd

# Ensure UTF-8 output encoding across all Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)

# Connect to in-memory database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# =============================================================================
# SETUP: DATABASE SCHEMA & MOCK DATA POPULATION
# =============================================================================
cursor.executescript("""
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT NOT NULL,
    department TEXT NOT NULL,
    city TEXT NOT NULL,
    age INTEGER,
    salary REAL NOT NULL,
    bonus REAL,
    is_active INTEGER DEFAULT 1
);

INSERT INTO employees VALUES
(101, 'Aarav Sharma',   'IT',             'Mumbai',    28, 68000, 5000, 1),
(102, 'Neha Verma',     'Finance',        'Delhi',     34, 82000, 8000, 1),
(103, 'Rohan Gupta',    'IT',             'Bangalore', 31, 74000, NULL, 1),
(104, 'Priya Nair',     'HR',             'Pune',      29, 54000, 3000, 1),
(105, 'Vikram Rathore', 'IT',             'Mumbai',    42, 98000, 12000, 1),
(106, 'Sneha Rao',      'Finance',        'Bangalore', 30, 86000, 7500, 1),
(107, 'Karan Johar',    'Marketing',      'Mumbai',    38, 71000, NULL, 0),
(108, 'Divya Sen',      'Data Analytics', 'Pune',      26, 65000, 4000, 1);

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    city TEXT NOT NULL,
    tier TEXT DEFAULT 'Standard'
);

INSERT INTO customers VALUES
(1, 'Aarav Enterprises', 'Mumbai',    'Platinum'),
(2, 'Apex Logistics',    'Delhi',     'Gold'),
(3, 'Zenith Retail',     'Bangalore', 'Silver'),
(4, 'Nova Tech Labs',    'Pune',      'Platinum'),
(5, 'Omega Global',      'Mumbai',    'Standard'); -- Zero orders customer

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    unit_price REAL NOT NULL
);

INSERT INTO products VALUES
(201, 'Wireless Keyboard', 'Accessories', 2500),
(202, 'Ergonomic Mouse',   'Accessories', 1800),
(203, '4K UHD Monitor',    'Hardware',    28000),
(204, 'Dev Laptop M3',     'Computers',   95000);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    order_date TEXT NOT NULL
);

INSERT INTO orders VALUES
(1001, 1, 204, 2, '2026-01-10'),
(1002, 1, 201, 5, '2026-01-12'),
(1003, 2, 203, 1, '2026-01-15'),
(1004, 3, 202, 3, '2026-01-18'),
(1005, 4, 204, 1, '2026-01-20'),
(1006, 4, 201, 2, '2026-01-22'),
(1007, 2, 202, 4, '2026-01-25');
""")
conn.commit()

def run_query(title: str, query: str):
    print("\n" + "-" * 65)
    print(f"QUERY: {title}")
    print("-" * 65)
    df = pd.read_sql_query(query, conn)
    print(df)
    return df

# =============================================================================
# PART 1: BASIC SELECT & FILTERING (WHERE, LIKE, ORDER BY)
# =============================================================================
print("=" * 65)
print(">>> PART 1: SELECT & FILTERING (WHERE, LIKE, ORDER BY) <<<")
print("=" * 65)

run_query(
    "1. Filter IT Employees Earning >= 70,000 Sorted by Salary Descending",
    """
    SELECT emp_name, department, city, salary
    FROM employees
    WHERE department = 'IT' AND salary >= 70000
    ORDER BY salary DESC;
    """
)

run_query(
    "2. Pattern Matching with LIKE (Names starting with 'A' or 'P')",
    """
    SELECT emp_id, emp_name, department, salary
    FROM employees
    WHERE emp_name LIKE 'A%' OR emp_name LIKE 'P%';
    """
)


# =============================================================================
# PART 2: AGGREGATIONS & GROUP BY WITH HAVING
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 2: AGGREGATIONS & GROUP BY WITH HAVING <<<")
print("=" * 65)

run_query(
    "3. Department-wise Headcount & Average Compensation",
    """
    SELECT 
        department,
        COUNT(*) AS total_staff,
        ROUND(AVG(salary), 2) AS average_salary,
        SUM(salary) AS department_budget
    FROM employees
    GROUP BY department
    ORDER BY department_budget DESC;
    """
)

run_query(
    "4. Departments with at least 2 staff members & avg salary > 70,000 (HAVING)",
    """
    SELECT 
        department,
        COUNT(*) AS total_staff,
        ROUND(AVG(salary), 2) AS average_salary
    FROM employees
    GROUP BY department
    HAVING COUNT(*) >= 2 AND AVG(salary) > 70000;
    """
)


# =============================================================================
# PART 3: RELATIONAL JOINS (INNER JOIN & LEFT JOIN)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 3: RELATIONAL JOINS <<<")
print("=" * 65)

run_query(
    "5. INNER JOIN: Full Order Details Across Customers and Products",
    """
    SELECT 
        o.order_id,
        c.customer_name,
        p.product_name,
        o.quantity,
        p.unit_price,
        (o.quantity * p.unit_price) AS total_line_value
    FROM orders o
    INNER JOIN customers c ON o.customer_id = c.customer_id
    INNER JOIN products p ON o.product_id = p.product_id
    ORDER BY o.order_id ASC;
    """
)

run_query(
    "6. LEFT JOIN: All Customers Including Inactive (Zero Orders) Accounts",
    """
    SELECT 
        c.customer_name,
        c.city,
        c.tier,
        COUNT(o.order_id) AS orders_placed,
        COALESCE(SUM(o.quantity * p.unit_price), 0) AS total_spent
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
    LEFT JOIN products p ON o.product_id = p.product_id
    GROUP BY c.customer_id, c.customer_name, c.city, c.tier
    ORDER BY total_spent DESC;
    """
)


# =============================================================================
# PART 4: NESTED SUBQUERIES
# =============================================================================
print("\n" + "=" * 65)
print(">>> PART 4: NESTED SUBQUERIES <<<")
print("=" * 65)

run_query(
    "7. Employees Earning More Than the Company-Wide Average Salary",
    """
    SELECT emp_name, department, salary
    FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees)
    ORDER BY salary DESC;
    """
)

run_query(
    "8. Customers Who Purchased from the 'Computers' Category (Subquery IN)",
    """
    SELECT customer_id, customer_name, city
    FROM customers
    WHERE customer_id IN (
        SELECT o.customer_id
        FROM orders o
        INNER JOIN products p ON o.product_id = p.product_id
        WHERE p.category = 'Computers'
    );
    """
)

conn.close()
print("\n" + "=" * 65)
print(">>> ALL SQL MODULE QUERIES EXECUTED SUCCESSFULLY <<<")
print("=" * 65)
