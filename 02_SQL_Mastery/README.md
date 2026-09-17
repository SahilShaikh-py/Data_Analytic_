# 🗄️ SQL & Relational Database Mastery (MySQL & SQLite)

SQL (Structured Query Language) is the most critical technical skill for Data Analysts, BI Engineers, and Data Scientists. Nearly 90% of business transaction data in global corporations is stored in Relational Database Management Systems (RDBMS).

---

## 📌 Relational Database Fundamentals

An RDBMS organizes information into structured 2-dimensional **Tables** (Relations) connected by mathematical relationships.

```
┌───────────────────────────┐         ┌───────────────────────────────┐
│     CUSTOMERS TABLE       │         │         ORDERS TABLE          │
├───────────────────────────┤         ├───────────────────────────────┤
│ [PK] customer_id (101)    │◀───┐    │ [PK] order_id (5001)          │
│      customer_name        │    └───┼─[FK] customer_id (101)         │
│      city                 │         │ [FK] product_id (205)  ───┐   │
│      tier                 │         │      quantity             │   │
└───────────────────────────┘         │      order_date           │   │
                                      └───────────────────────────┼───┘
                                                                  │
                                      ┌───────────────────────────┼───┐
                                      │        PRODUCTS TABLE     │   │
                                      ├───────────────────────────┼───┤
                                      │ [PK] product_id (205) ◀───┘   │
                                      │      product_name             │
                                      │      category                 │
                                      │      unit_price               │
                                      └───────────────────────────────┘
```

- **Primary Key (PK):** A column (or set of columns) that uniquely identifies every record in a table. It cannot contain `NULL` values. *(e.g., `customer_id`)*.
- **Foreign Key (FK):** A column that creates a link between two tables by referencing the Primary Key of another table. *(e.g., `customer_id` inside the `orders` table)*.

---

## 📌 Query Execution Order (How the Database Thinks)

Writing SQL is different from programming languages. SQL is **declarative** (you specify *what* data you want, not *how* to loop through memory).

The database executes query clauses in this exact order:

```
1. FROM / JOIN   ──▶ Identifies target tables and merges them
2. WHERE         ──▶ Filters raw individual rows
3. GROUP BY      ──▶ Aggregates filtered rows into summary buckets
4. HAVING        ──▶ Filters the grouped aggregated metrics
5. SELECT        ──▶ Selects requested columns and applies expressions
6. DISTINCT      ──▶ Removes duplicate rows from the output
7. ORDER BY      ──▶ Sorts final output rows (ASC / DESC)
8. LIMIT / TOP   ──▶ Caps total row count returned
```

---

## 📁 SQL Mastery Files & Exercises in this Directory

| File Name | Purpose & Key Topics Covered |
| :--- | :--- |
| **`01_sql_basics_and_filtering.sql`** | Table Creation, `SELECT`, Aliasing, `WHERE` operators (`=, >, <, BETWEEN, IN`), Wildcard pattern matching (`LIKE '%term%'`), `ORDER BY`, `LIMIT`. |
| **`02_sql_grouping_and_aggregations.sql`**| Aggregate functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`), category slicing via `GROUP BY`, conditional group filtering using `HAVING` (vs `WHERE`). |
| **`03_sql_joins_and_subqueries.sql`** | Multi-table relational joins (`INNER JOIN`, `LEFT JOIN`), cross-table metric analysis, nested subqueries in `WHERE`, `FROM`, and `SELECT`. |
| **`sql_interactive_runner.py`** | **1-Click Interactive Runner!** Runs all queries instantly in local SQLite, displaying formatted terminal tables matching [`ExcepPandas.py`](file:///d:/YSM%20Info%20Solution/Data%20Analytics%20&Cyber%20Security/python/ExcepPandas.py). |

---

## 🚀 How to Run the SQL Queries

You do **not** need to install MySQL Server to practice! Run the self-contained Python runner:

```bash
python 02_SQL_Mastery/sql_interactive_runner.py
```
This automatically initializes the database, populates mock tables, executes the queries, and prints output tables in clean formatted ASCII tables.
