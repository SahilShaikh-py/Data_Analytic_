# 📕 Module 4: DAX Mastery Guide (Data Analysis Expressions)

### 🎯 Objective:
Master the architectural difference between Calculated Columns and Measures, understand DAX Evaluation Contexts (Row Context, Filter Context, and Context Transition), construct a dedicated `_All_Measures` centralized repository table, and build 25+ production-grade DAX measures against our 1,000-row enterprise dataset. Every pattern is explained with precise syntax, formatting requirements, and business logic.

---

## 📂 Reference Data Context for this Module:
- **Fact Table:** `sales_data_1000` (`SalesAmount`, `CostAmount`, `Quantity`, `UnitPrice`, `Discount`, `Profit`, `OrderDate`)
- **Calendar Dimension:** `Dim_Calendar` (`Date`, `Year`, `MonthName`, `MonthNumber`)
- **Dimensions:** `customer_dim` (`CustomerID`, `CustomerName`, `Region`), `product_dim` (`ProductID`, `ProductName`, `Category`)

---

## 📌 Topic 4.1: Calculated Column vs. Measure (The Critical Architectural Difference)

A core foundational concept and the **#1 most frequently asked Power BI interview question**:

| Feature | Calculated Column | Measure (⭐ Recommended Best Practice) |
| :--- | :--- | :--- |
| **Storage Location** | Evaluated during data refresh and persisted as physical data in system **RAM (Disk storage)**. | Never physically stored! Dynamically computed **on-the-fly by the CPU** when requested by a visual. |
| **Evaluation Context** | **Row Context** (Iterates and evaluates strictly row-by-row across the table). | **Filter Context** (Recalculates dynamically based on active slicers, cross-filters, and visual axes). |
| **Model Footprint** | Inflates file size and consumes memory proportional to table row volume. | Zero persistent storage overhead; highly scalable and fast. |
| **Optimal Use Cases** | When categorical values must serve as **Slicers**, **Filter boundaries**, or **Matrix row/column headers** (e.g., Age Groups, Customer Tiers). | When calculating business KPIs, dynamic ratios, percentages, and summaries (e.g., Total Revenue, Margin %, YoY Growth %). |

---

### 🛠️ Operation 1: How to Create a Calculated Column

#### Business Scenario:
Compute per-row gross transaction value: `GrossRevenue = Quantity * UnitPrice` as a physical row attribute in `sales_data_1000`.

- **Step 1:** In the left sidebar, click **Table View** (Data grid icon).
- **Step 2:** In the right **Data Pane**, expand `sales_data_1000`.
- **Step 3:** Click the contextual **Table Tools Tab** in the top ribbon.
- **Step 4:** Within the **Calculations** group, click **New Column**.
- **Step 5:** Enter the following expression in the Formula Bar:
  ```dax
  GrossRevenue = sales_data_1000[Quantity] * sales_data_1000[UnitPrice]
  ```
- **Step 6:** Press `Enter`.
- **Step 7:** A new physical column is appended at the far right of the table, evaluated across every individual row.

---

### 🛠️ Operation 2: How to Create a Measure

#### Business Scenario:
Formulate an aggregated dynamic business KPI: `Total Sales = SUM(sales_data_1000[SalesAmount])`.

- **Step 1:** Navigate to the **Home Tab** (or **Modeling Tab**) in the ribbon.
- **Step 2:** Click **New Measure** in the **Calculations** group.
- **Step 3:** Enter the DAX expression in the Formula Bar:
  ```dax
  Total Sales = SUM(sales_data_1000[SalesAmount])
  ```
- **Step 4:** Press `Enter`.
- **Step 5 (Format Measure):**
  - The **Measure Tools Tab** will appear in the ribbon.
  - In the **Formatting** group, select Currency (`$`) and set decimal places to `2`.
- **Step 6:** The `Total Sales` measure is added to the Data Pane with a distinct calculator icon.

---

## 📌 Topic 4.2: Best Practice - Creating a Centralized `_All_Measures` Table

Rather than dispersing measures haphazardly across various Fact and Dimension tables, professional BI architecture dictates isolating all DAX measures in a dedicated repository table.

### 🛠️ Step-by-Step Setup:
- **Step 1:** Click the **Home Tab** in the ribbon.
- **Step 2:** Click the **Enter Data** button in the **Data** group.
- **Step 3:** In the Create Table dialog:
  - Replace `Table1` in the Table name input with **`_All_Measures`** *(The leading underscore `_` forces alphabetical sorting to the very top of the Data Pane)*.
  - Leave the grid columns blank.
- **Step 4:** Click **Load**.
- **Step 5 (Relocate Measures to the Central Table):**
  - In the Data Pane, click any existing measure (e.g., `Total Sales`).
  - Open the **Measure Tools Tab** in the ribbon.
  - In the **Home table** dropdown, change `sales_data_1000` to **`_All_Measures`**.
- **Step 6 (Delete Default Column):**
  - Right-click the dummy placeholder `Column1` in `_All_Measures` and select **Delete from model**.
- **Step 7 (Result):** `_All_Measures` automatically assumes a **Calculator Table Icon** and pins permanently to the top of the Data Pane.

---

## 📌 Topic 4.3: Understanding Contexts in DAX (The Three Evaluation Pillars)

1. **Row Context (Row-by-Row Iteration):**
   - Active when DAX iterates through an individual row of a table.
   - Automatically present in Calculated Columns and iterative "X-functions" (`SUMX`, `AVERAGEX`).
2. **Filter Context (Dynamic Visual Query Context):**
   - Composed of all active slicer selections, visual coordinate coordinates (e.g., chart axis categories), and page-level filter cards.
   - The subset of rows that survives these combined filters represents the active Filter Context against which Measures evaluate.
3. **Context Transition (The Core Engine):**
   - Occurs when a Row Context is converted into an equivalent Filter Context by wrapping an expression in **`CALCULATE()`**.

---

## 📌 Topic 4.4: 25+ Production DAX Measures (Categorized Reference)

> [!TIP]
> **Standard Measure Creation Workflow:**
> For every measure below:
> 1. Right-click `_All_Measures` in the Data Pane ➡️ click **New Measure**.
> 2. Paste the DAX code into the Formula Bar and press `Enter`.
> 3. Use the **Measure Tools Tab** to assign formatting (Currency, Whole Number, or Percentage).

---

### 🔹 Category 1: Standard Aggregations & Safe Arithmetic

#### Measure 1: Total Revenue
```dax
Total Revenue = SUM(sales_data_1000[SalesAmount])
```
*Formatting: Currency ($), 2 Decimals.*

#### Measure 2: Total Cost
```dax
Total Cost = SUM(sales_data_1000[CostAmount])
```
*Formatting: Currency ($), 2 Decimals.*

#### Measure 3: Total Profit
```dax
Total Profit = SUM(sales_data_1000[Profit])
```
*Formatting: Currency ($), 2 Decimals.*

#### Measure 4: Total Orders (Count Rows)
```dax
Total Orders = COUNTROWS(sales_data_1000)
```
*Formatting: Whole Number (123).*

#### Measure 5: Unique Customers Count
```dax
Unique Customers = DISTINCTCOUNT(sales_data_1000[CustomerID])
```
*Formatting: Whole Number (123).*

#### Measure 6: Profit Margin % (Safe Division via DIVIDE)
> *Avoid `[Total Profit] / [Total Revenue]`! If revenue equals zero, standard division throws `#DIV/0` errors. Always encapsulate division in `DIVIDE()`.*
```dax
Profit Margin % = 
DIVIDE([Total Profit], [Total Revenue], 0)
```
*Formatting: Percentage (%), 2 Decimals.*

#### Measure 7: Average Order Value (AOV)
```dax
Average Order Value = 
DIVIDE([Total Revenue], [Total Orders], 0)
```
*Formatting: Currency ($), 2 Decimals.*

---

### 🔹 Category 2: Iterator / X-Functions (Row-by-Row Iteration)

Iterator functions iterate over each individual row of a table, execute an expression, and aggregate the results:

#### Measure 8: Row-by-Row Total Cost via SUMX
```dax
Total Cost SUMX = 
SUMX(
    sales_data_1000,
    sales_data_1000[Quantity] * sales_data_1000[CostAmount]
)
```

#### Measure 9: Average Daily Sales via AVERAGEX
```dax
Avg Daily Sales = 
AVERAGEX(
    VALUES(Dim_Calendar[Date]),
    [Total Revenue]
)
```

#### Measure 10: Dynamic Customer Ranking via RANKX
```dax
Customer Rank = 
RANKX(
    ALL(customer_dim[CustomerName]),
    [Total Revenue],
    ,
    DESC,
    Dense
)
```

---

### 🔹 Category 3: The King of DAX: `CALCULATE()` & Filter Modifiers

`CALCULATE()` modifies or overrides the existing Filter Context of an evaluation:

#### Measure 11: APAC Region Sales (Explicit Filter Context)
```dax
APAC Sales = 
CALCULATE(
    [Total Revenue],
    customer_dim[Region] = "APAC"
)
```

#### Measure 12: High-Value Order Sales
```dax
High Value Sales = 
CALCULATE(
    [Total Revenue],
    sales_data_1000[SalesAmount] >= 2000
)
```

#### Measure 13: Grand Total Sales (Ignoring Regional Slicers via ALL)
```dax
All Geography Sales = 
CALCULATE(
    [Total Revenue],
    ALL(customer_dim[Region])
)
```

#### Measure 14: % Contribution to Total Regional Sales
```dax
% Region Contribution = 
DIVIDE(
    [Total Revenue],
    CALCULATE([Total Revenue], ALL(customer_dim[Region])),
    0
)
```
*Formatting: Percentage (%), 2 Decimals.*

#### Measure 15: Sales Excluding Category Filter via ALLEXCEPT
```dax
Sales Keep Only Category Filter = 
CALCULATE(
    [Total Revenue],
    ALLEXCEPT(product_dim, product_dim[Category])
)
```

---

### 🔹 Category 4: Cross-Table Navigation (`RELATED` & `RELATEDTABLE`)

#### Measure 16: Calculated Column in Fact Table Fetching Category
- *Navigation: Table View > sales_data_1000 > New Column*
```dax
Product Category Lookup = RELATED(product_dim[Category])
```

#### Measure 17: Order Count per Customer in Customer Dimension Table
- *Navigation: Table View > customer_dim > New Column*
```dax
Customer Total Orders Count = COUNTROWS(RELATEDTABLE(sales_data_1000))
```

---

### 🔹 Category 5: Time Intelligence DAX (Temporal & Cumulative Metrics)

> [!IMPORTANT]
> Time Intelligence functions require an official contiguous `Dim_Calendar` table marked as a Date Table to calculate correctly.

#### Measure 18: Year-to-Date Sales (YTD)
```dax
YTD Sales = 
TOTALYTD(
    [Total Revenue],
    Dim_Calendar[Date]
)
```

#### Measure 19: Quarter-to-Date Sales (QTD)
```dax
QTD Sales = 
TOTALQTD(
    [Total Revenue],
    Dim_Calendar[Date]
)
```

#### Measure 20: Prior Year Sales (Same Period Last Year)
```dax
PY Sales = 
CALCULATE(
    [Total Revenue],
    SAMEPERIODLASTYEAR(Dim_Calendar[Date])
)
```

#### Measure 21: Year-over-Year (YoY) Growth Amount
```dax
YoY Sales Growth Amount = [Total Revenue] - [PY Sales]
```

#### Measure 22: Year-over-Year (YoY) Growth %
```dax
YoY Sales Growth % = 
DIVIDE(
    [YoY Sales Growth Amount],
    [PY Sales],
    0
)
```
*Formatting: Percentage (%), 2 Decimals.*

#### Measure 23: Sales Shifted 30 Days Back (DATEADD)
```dax
Sales Last 30 Days = 
CALCULATE(
    [Total Revenue],
    DATEADD(Dim_Calendar[Date], -30, DAY)
)
```

---

### 🔹 Category 6: Conditional Branching & Dynamic UI DAX

#### Measure 24: Operational Status Badge via SWITCH
```dax
Performance Status = 
SWITCH(
    TRUE(),
    [Profit Margin %] >= 0.25, "🟢 Exceptional",
    [Profit Margin %] >= 0.10, "🟡 Moderate",
    "🔴 At Risk"
)
```

#### Measure 25: Dynamic Visual Header Controlled by Slicers
```dax
Dynamic Dashboard Title = 
VAR SelectedReg = SELECTEDVALUE(customer_dim[Region], "All Global Regions")
RETURN
"Sales & Profitability Analysis - " & SelectedReg
```

---

## 📌 Topic 4.5: DAX Best Practices & Performance Tuning

### 1. Leverage Variables (`VAR ... RETURN`):
Variables enhance code readability and dramatically improve performance by caching intermediate calculation results in memory rather than recalculating them repeatedly:

```dax
Optimized Profit Margin = 
VAR CurrentProfit = [Total Profit]
VAR CurrentRevenue = [Total Revenue]
RETURN
    DIVIDE(CurrentProfit, CurrentRevenue, 0)
```

### 2. Organizing Measures into Display Folders:
- Navigate to **Model View** on the left sidebar.
- In the Data Pane, expand `_All_Measures`.
- Select `[Total Revenue]`, `[Total Cost]`, and `[Total Profit]` using `Ctrl+Click`.
- In the Properties pane, enter `01_Core_Financials` in the **Display Folder** input.
- The selected measures will now be cleanly grouped into an expandable subfolder.

---

## 📌 Topic 4.6: Hands-On DAX Practice Checklist (Student Lab Challenge)

- [ ] **Task 1:** Create the centralized `_All_Measures` table and confirm its calculator icon status.
- [ ] **Task 2:** Author `[Total Revenue]`, `[Total Cost]`, and `[Total Profit]` measures.
- [ ] **Task 3:** Create `[Profit Margin %]` using `DIVIDE()` and format as a two-decimal Percentage.
- [ ] **Task 4:** Create `% Region Contribution` using `CALCULATE()` with `ALL()`.
- [ ] **Task 5:** Author `[PY Sales]` using `SAMEPERIODLASTYEAR()`.
- [ ] **Task 6:** Calculate `[YoY Sales Growth %]` and plot on a Line Chart visual.
- [ ] **Task 7:** Formulate `[Performance Status]` using `SWITCH(TRUE(), ...)`.
- [ ] **Task 8:** Add `Dynamic Dashboard Title` to a Card visual and verify dynamic updates when clicking a Region slicer.
