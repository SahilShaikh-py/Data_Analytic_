# 🎯 Top 50 Data Analytics Interview Questions & Answers (Master Reference)

A curated compilation of the most frequently asked technical, theoretical, and scenario-based interview questions asked by hiring managers at product and service companies.

---

## 📊 SECTION 1: MICROSOFT EXCEL (Q1 – Q10)

#### Q1: What is the main difference between XLOOKUP and legacy VLOOKUP?
- **Answer:** VLOOKUP requires hardcoded column indices, cannot look to the left, and defaults to approximate matching (which causes bugs). `XLOOKUP` defaults to exact match, looks in any direction (left, right, up, down), supports built-in fallback values (`[if_not_found]`), and dynamically adjusts when columns are inserted or deleted.

#### Q2: How does the INDEX-MATCH combination work under the hood?
- **Answer:** `MATCH(lookup_val, lookup_array, 0)` returns the relative row position number. `INDEX(array, row_num)` uses that position number to retrieve the target cell value. Unlike VLOOKUP, it is immune to column shifts and consumes less memory.

#### Q3: What is the difference between COUNT, COUNTA, and COUNTBLANK?
- **Answer:**
  - `COUNT`: Counts only cells containing numeric values.
  - `COUNTA`: Counts all non-empty cells (numbers, text, booleans, errors).
  - `COUNTBLANK`: Counts only empty cells.

#### Q4: When would you use SUMIFS instead of SUMIF?
- **Answer:** `SUMIF` only supports a single criteria condition. `SUMIFS` allows multiple simultaneous criteria (e.g., Region = "North" AND Category = "Electronics" AND Amount > 10000). In `SUMIFS`, the `sum_range` is always the first argument.

#### Q5: What is an Excel Table (`CTRL + T`) and why should you use it with Pivot Tables?
- **Answer:** An official Excel Table treats a range as a structured relational dataset. It provides automatic formula propagation, banded formatting, and structured column referencing. Most importantly, when new rows are appended to the table, linked Pivot Tables automatically include the new rows upon refreshing.

#### Q6: How do you connect one Slicer to multiple Pivot Tables?
- **Answer:** Right-click the Slicer ➡️ Select **Report Connections** (or **PivotTable Connections**) ➡️ Check the boxes for all Pivot Tables on the dashboard.

#### Q7: What is Conditional Formatting and how do you highlight an entire row?
- **Answer:** Conditional formatting applies visual styles dynamically based on cell values. To format an entire row, write a custom formula locking the evaluated column with a dollar sign: `=$E2="High Priority"`.

#### Q8: What does the `#N/A` error mean in Excel and how do you handle it?
- **Answer:** `#N/A` indicates that a lookup formula failed to find a match. It can be handled cleanly using `=IFNA(formula, "Custom Fallback")` or via XLOOKUP's built-in 4th argument.

#### Q9: What is Data Validation and why is it critical for data entry?
- **Answer:** Data Validation restricts user inputs to valid predefined rules (e.g., drop-down lists, numeric ranges, date limits), preventing typos and bad formatting at the source.

#### Q10: What is the difference between an Absolute Reference (`$A$1`) and a Relative Reference (`A1`)?
- **Answer:** A relative reference changes automatically when copied to adjacent cells. An absolute reference (`$A$1`) locks both column and row so the targeted cell remains constant when copied.

---

## 🗄️ SECTION 2: SQL & RELATIONAL DATABASES (Q11 – Q25)

#### Q11: What is the logical query execution order in SQL?
- **Answer:** `FROM & JOIN` ➡️ `WHERE` ➡️ `GROUP BY` ➡️ `HAVING` ➡️ `SELECT` ➡️ `DISTINCT` ➡️ `ORDER BY` ➡️ `LIMIT / TOP`.

#### Q12: What is the critical difference between `WHERE` and `HAVING`?
- **Answer:** `WHERE` filters individual rows **before** aggregation and cannot evaluate aggregate functions like `SUM()` or `COUNT()`. `HAVING` filters aggregated groups **after** the `GROUP BY` clause has executed.

#### Q13: Explain the difference between `INNER JOIN` and `LEFT JOIN`.
- **Answer:**
  - `INNER JOIN`: Returns only records that have matching keys in **both** tables.
  - `LEFT JOIN`: Returns **all** records from the left table, plus matched records from the right table. Unmatched right table columns are populated with `NULL`.

#### Q14: How do you find records in Table A that do not exist in Table B?
- **Answer:** Using a `LEFT JOIN` with a `WHERE ... IS NULL` filter:
  ```sql
  SELECT a.* FROM table_a a 
  LEFT JOIN table_b b ON a.id = b.id 
  WHERE b.id IS NULL;
  ```

#### Q15: What is the difference between `COUNT(*)`, `COUNT(column)`, and `COUNT(DISTINCT column)`?
- **Answer:**
  - `COUNT(*)`: Counts all rows, including rows with NULL values.
  - `COUNT(column)`: Counts only rows where the specified column is NOT NULL.
  - `COUNT(DISTINCT column)`: Counts the number of unique non-null values.

#### Q16: Explain Window Functions: `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()`.
- **Answer:** In a tie (e.g. values 100, 100, 90):
  - `ROW_NUMBER()` assigns unique sequential integers: `1, 2, 3`.
  - `RANK()` assigns identical ranks with gaps: `1, 1, 3`.
  - `DENSE_RANK()` assigns identical ranks without gaps: `1, 1, 2`.

#### Q17: What is a Common Table Expression (CTE) and why is it preferred over nested subqueries?
- **Answer:** A CTE (`WITH cte_name AS (...)`) defines a temporary named result set. It improves readability, modularity, and can be referenced multiple times within the same query.

#### Q18: What is the difference between `UNION` and `UNION ALL`?
- **Answer:** `UNION` combines result sets and runs an internal deduplication step (slower). `UNION ALL` combines results keeping all duplicates (much faster).

#### Q19: What is a Primary Key vs a Foreign Key?
- **Answer:** A Primary Key uniquely identifies each row in a table and cannot be NULL. A Foreign Key is a column that refers to the Primary Key of another table, establishing a parent-child relationship.

#### Q20: What is database Indexing and what are its trade-offs?
- **Answer:** An index is a B-tree data structure that drastically accelerates `SELECT` queries and `WHERE` filtering. The trade-off is slower `INSERT`, `UPDATE`, and `DELETE` operations and additional disk storage.

#### Q21: How do you calculate Month-over-Month (MoM) revenue growth in SQL?
- **Answer:** Using the `LAG()` window function:
  ```sql
  SELECT 
      month, revenue,
      ROUND((revenue - LAG(revenue, 1) OVER (ORDER BY month)) * 100.0 / LAG(revenue, 1) OVER (ORDER BY month), 2) AS mom_growth_pct
  FROM monthly_sales;
  ```

#### Q22: What is the difference between `DELETE`, `TRUNCATE`, and `DROP`?
- **Answer:**
  - `DELETE`: DML command that removes specific rows (can use WHERE; rollback possible).
  - `TRUNCATE`: DDL command that removes all rows quickly without logging individual row deletions.
  - `DROP`: DDL command that permanently destroys the entire table structure and data from disk.

#### Q23: What does `COALESCE()` do?
- **Answer:** `COALESCE(val1, val2, ...)` returns the first non-null expression from its arguments list. Frequently used to replace nulls with `0` or default text.

#### Q24: What is the difference between a Correlated Subquery and a Non-Correlated Subquery?
- **Answer:** A non-correlated subquery executes independently once and passes its result to the outer query. A correlated subquery depends on values from the outer query row-by-row and executes repeatedly for every row.

#### Q25: How do you find the 2nd highest salary in an employee table without using LIMIT/TOP?
- **Answer:**
  ```sql
  SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees);
  ```

---

## 🐍 SECTION 3: PYTHON & DATA SCIENCE (Q26 – Q35)

#### Q26: What is the difference between a Python List and a NumPy Array?
- **Answer:** Python Lists hold heterogeneous objects via pointer references (slower, high memory overhead). NumPy arrays are homogeneous, stored in contiguous memory blocks, and support vectorized SIMD operations (50x-100x faster for math).

#### Q27: What is the difference between `.loc[]` and `.iloc[]` in Pandas?
- **Answer:**
  - `.loc[]`: Label-based indexing (uses actual row labels and column names).
  - `.iloc[]`: Integer-position-based indexing (uses zero-based integer index numbers `0, 1, 2...`).

#### Q28: How do you handle missing (NaN) values in Pandas?
- **Answer:**
  - Detect: `df.isna().sum()`
  - Drop: `df.dropna(subset=['critical_col'])`
  - Impute: `df['age'] = df['age'].fillna(df['age'].median())` or Forward Fill `df.ffill()`.

#### Q29: What is the difference between `df['col'] = df['col'].astype(float)` and `pd.to_numeric()`?
- **Answer:** `astype(float)` crashes if it encounters invalid non-numeric strings (like `"N/A"` or `"invalid"`). `pd.to_numeric(df['col'], errors='coerce')` safely converts bad strings into `NaN` without throwing an exception.

#### Q30: What is the difference between `apply()`, `map()`, and vectorized operations?
- **Answer:** Vectorized operations (`df['a'] + df['b']`) are compiled C-speed and should always be preferred. `map()` is used on Series for mapping values via dictionary or function. `apply()` runs Python-level iteration row-by-row or column-by-column (slowest, use as last resort).

#### Q31: How do you detect outliers statistically in Python?
- **Answer:** Using the Interquartile Range (IQR) Rule:
  ```python
  Q1 = df['col'].quantile(0.25)
  Q3 = df['col'].quantile(0.75)
  IQR = Q3 - Q1
  outliers = df[(df['col'] < Q1 - 1.5 * IQR) | (df['col'] > Q3 + 1.5 * IQR)]
  ```

#### Q32: What is the difference between a Shallow Copy and a Deep Copy in Pandas?
- **Answer:** A shallow copy (`df2 = df` or slice) creates a view pointing to the same memory block (modifying `df2` alters `df`). A deep copy (`df2 = df.copy()`) allocates an independent memory duplicate.

#### Q33: How do you merge two DataFrames on different column names in Pandas?
- **Answer:**
  ```python
  pd.merge(df_orders, df_users, left_on='user_id', right_on='customer_id', how='left')
  ```

#### Q34: What is a Lambda function and where is it used in Data Science?
- **Answer:** A lambda is an anonymous, single-expression inline function (`lambda x: x * 1.18`). Heavily used in data transformations inside `.apply()` and sorting keys.

#### Q35: How do you read and write SQL tables directly using Pandas?
- **Answer:**
  - Read: `df = pd.read_sql_query("SELECT * FROM table", connection)`
  - Write: `df.to_sql("target_table", connection, if_exists="append", index=False)`

---

## 📈 SECTION 4: MICROSOFT POWER BI & DAX (Q36 – Q45)

#### Q36: What is the difference between a Calculated Column and a Measure in DAX?
- **Answer:**
  - **Calculated Column:** Evaluated at data refresh, row-by-row, stored in RAM, increases file size.
  - **Measure:** Evaluated dynamically at query time based on report filter context, consumes zero storage RAM until rendered.

#### Q37: What is the VertiPaq Engine in Power BI?
- **Answer:** The in-memory, columnar database engine powering Power BI. It achieves massive compression (10x) and fast performance by storing data in columns rather than rows.

#### Q38: What is the difference between Star Schema and Snowflake Schema?
- **Answer:**
  - **Star Schema:** Fact table in the center directly connected to single-level Dimension tables. (Recommended for Power BI due to fast relationship traversal).
  - **Snowflake Schema:** Dimension tables are normalized into sub-dimensions (more complex, slower relationship filtering).

#### Q39: What does the `CALCULATE()` function do in DAX?
- **Answer:** `CALCULATE()` evaluates a DAX expression while modifying or overriding the current filter context. It is the most powerful function in DAX.
  *(e.g., `CALCULATE([Total Sales], DimProduct[Category] = "Electronics")`)*.

#### Q40: What is the difference between Row Context and Filter Context?
- **Answer:**
  - **Row Context:** "Which row am I looking at right now?" (Exclusively present in calculated columns or iterating X-functions like `SUMX`).
  - **Filter Context:** "What filters are active from slicers, visual interactions, and page filters?"

#### Q41: Explain the purpose of `ALL()` and `ALLEXCEPT()`.
- **Answer:** `ALL(Table[Column])` strips away any active filters from that column, enabling benchmark denominator calculations like `% of Total Sales`. `ALLEXCEPT()` removes all filters except specified columns.

#### Q42: What is the difference between `SUM` and `SUMX`?
- **Answer:** `SUM` aggregates a single physical column. `SUMX(Table, Expression)` is an iterator that computes an expression row-by-row (e.g. `Price * Quantity`) and then sums the results.

#### Q43: What is Row-Level Security (RLS) in Power BI?
- **Answer:** RLS restricts data access for specific users based on their login roles. *(e.g., Regional Manager North can only view North regional sales)*.

#### Q44: What is the difference between Import Mode and DirectQuery Mode?
- **Answer:**
  - **Import Mode:** Ingests data into Power BI RAM (fastest, supports all DAX, max 1GB file limit for Pro).
  - **DirectQuery:** Leaves data in the underlying SQL database and sends real-time queries on every visual interaction (slower, supports near-real-time data).

#### Q45: How do you calculate Year-to-Date (YTD) Sales in DAX?
- **Answer:**
  ```dax
  Sales YTD = TOTALYTD([Total Sales], DimDate[Date])
  ```

---

## 💼 SECTION 5: SCENARIO-BASED & BUSINESS PROBLEM SOLVING (Q46 – Q50)

#### Q46: If an executive tells you "Sales dropped 15% this month, find out why," what is your framework?
- **Answer:**
  1. **Data Integrity Check:** Verify pipeline completeness (Did data ingestion lag? Are records missing?).
  2. **Decomposition:** Break down Sales = *Traffic (Visitors) × Conversion Rate × Average Order Value (AOV)*.
  3. **Segment Slicing:** Slice by Geography, Product Category, Customer Cohort, and Device Type.
  4. **External Drivers:** Check seasonality, marketing campaign pauses, stock-outs, or competitor discounting.

#### Q47: How do you handle stakeholders who request 50 columns on a single dashboard page?
- **Answer:** Explain cognitive overload and dashboard responsiveness. Recommend an **Executive-to-Operational drill-down structure**: Keep 4 key KPI cards and top 3 charts on the summary page, with drill-through navigation or exportable detail tabs for operational line-items.

#### Q48: How do you validate that your SQL query results are 100% accurate before reporting?
- **Answer:** Cross-check row counts, verify against source transactional totals, ensure Primary Key uniqueness in joined tables, check for inadvertent Cartesian products (`CROSS JOIN` duplicates), and validate edge case nulls.

#### Q49: What is the difference between Mean, Median, and Mode in a skewed salary distribution?
- **Answer:** If a few executives earn Rs. 50 Lakhs while staff earn Rs. 5 Lakhs, the **Mean** is pulled upward artificially. The **Median** (50th percentile) represents the true central tendency of the majority of employees.

#### Q50: How do you explain a complex Machine Learning or statistical metric (like IQR or Correlation) to a non-technical manager?
- **Answer:** Use analogies. For example, explain IQR as: *"Imagine taking the middle 50% of our typical customers; any transaction that falls well outside this normal zone is an extreme exception that warrants individual inspection."*
