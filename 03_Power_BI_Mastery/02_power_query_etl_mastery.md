# 📗 Module 2: Power Query ETL Mastery (Complete Step-by-Step Data Cleaning & Transformation)

### 🎯 Objective:
Master the end-to-end Extract, Transform, and Load (ETL) pipeline using Power Query. Clean, reshape, merge, and structure dirty, unstructured source datasets (CSV, Excel, Database) into an enterprise-ready, 100% optimized dimensional model. Every technique is presented with explicit UI navigation, button sequences, parameter inputs, and business rationale.

---

## 📂 Reference Datasets Path for this Module:
All hands-on labs in this module reference these files:
- **Fact Table:** `d:\YSM Info Solution\Data Analytics &Cyber Security\python\Power BI\data\sales_data_1000.csv`
- **Yearly Sales (Append Queries):**
  - `d:\YSM Info Solution\Data Analytics &Cyber Security\python\Power BI\data\Sales_2022.csv`
  - `d:\YSM Info Solution\Data Analytics &Cyber Security\python\Power BI\data\Sales_2023.csv`
  - `d:\YSM Info Solution\Data Analytics &Cyber Security\python\Power BI\data\Sales_2024.csv`
- **Customer Dimension:** `d:\YSM Info Solution\Data Analytics &Cyber Security\python\Power BI\data\customer_dim.csv`
- **Product Dimension:** `d:\YSM Info Solution\Data Analytics &Cyber Security\python\Power BI\data\product_dim.csv`
- **Unpivot Exercise Data:** `d:\YSM Info Solution\Data Analytics &Cyber Security\python\Power BI\data\unpivot_exercise_data.csv`

---

## 📌 Topic 2.1: Power Query Editor Interface & Architecture

### 1. Conceptual Framework
In enterprise data ingestion, up to 80% of raw source data arrives incomplete, improperly typed, or structurally non-relational. **Power Query Editor** serves as Power BI's dedicated visual and formula-driven ETL engine, allowing analysts to sanitize, reshape, and optimize data streams before committing records to the reporting engine.

### 2. Launching Power Query Editor:
- **Step 1:** Open Power BI Desktop.
- **Step 2:** Navigate to the **Home Tab** in the top ribbon.
- **Step 3:** Within the **Queries** group, click the **Transform Data** icon.
- **Step 4:** A dedicated auxiliary application window will open titled **Power Query Editor**.

```
+---------------------------------------------------------------------------------------------------------+
|  TOP RIBBON TABS: [Home] [Transform] [Add Column] [View] [Tools] [Help]                                 |
+-------------------+-------------------------------------------------------------+-----------------------+
| QUERIES PANE      | FORMULA BAR: = Table.TransformColumnTypes(#"Promoted Headers")| APPLIED STEPS PANE:   |
| (Left Sidebar):   +-------------------------------------------------------------+ (Right Sidebar):      |
|                   | [ABC] OrderID | [Calendar] OrderDate | [1.2] SalesAmount    | * Source              |
| > sales_data_1000 | ORD-0001      | 2024-02-13           | 625.63               | * Promoted Headers    |
| > customer_dim    | ORD-0002      | 2023-01-29           | 5464.45              | * Changed Type        |
| > product_dim     | ORD-0003      | 2023-11-18           | 786.12               | [ ❌ to delete step ]  |
+-------------------+-------------------------------------------------------------+-----------------------+
| Status Bar: 17 Columns, 1000 Rows | Data Profiling Status: Column profiling based on top 1000 rows      |
+---------------------------------------------------------------------------------------------------------+
```

### 3. Five Core Components of the Interface:

#### Component 1: Top Ribbon Tabs
- **Home Tab:** Primary data cleaning operations (Data sources, row filtering, column splitting, merging, appending, and Close & Apply).
- **Transform Tab:** In-place modifications (Modifies data within the existing selected column without generating a new column).
- **Add Column Tab:** Feature engineering (Generates a new output column based on calculations while preserving source columns).
- **View Tab:** Data health diagnostics (Data Profiling toggles: Column Quality, Column Distribution, Column Profile, and Formula Bar visibility).

#### Component 2: Queries Pane (Left Sidebar)
- Enumerates all ingested queries/tables (e.g., `sales_data_1000`, `customer_dim`).
- Right-clicking enables options to **Rename**, **Delete**, **Duplicate**, or create an isolated downstream **Reference** query.

#### Component 3: Formula Bar (Top Center)
- Displays the live **M-Code (Power Query Formula Language)** expression driving the active transformation step.
- To display if hidden: Navigate to **View Tab** > **Layout Group** > check the **Formula Bar** checkbox.

#### Component 4: Data Canvas (Center Grid)
- Tabular preview grid displaying active data transformations.
- Each column header includes an interactive **Data Type Icon** (`ABC`, `123`, Calendar icon) for one-click casting.
- Right-clicking any column header exposes context-specific transformation shortcuts.

#### Component 5: Applied Steps Pane (Right Sidebar - Core Rule)
- **Power Query does not maintain traditional `Ctrl + Z` undo histories.**
- Every user transformation creates an immutable, sequential step in the **Applied Steps** list.
- **Undoing a Step:** Click the red **`❌` (Delete)** icon next to the target step.
- **Editing Step Parameters:** Click the **Gear / Settings Icon (⚙️)** adjacent to the step name.
- **Renaming Steps:** Right-click the step -> select **Rename** (e.g., `Changed Type to Currency`).

---

## 📌 Topic 2.2: Data Profiling (Auditing Data Quality)

### 1. Purpose and Importance:
Before implementing ETL transformations, analysts must audit column null percentages, syntax corruption, error frequencies, and cardinality distributions. This audit workflow is known as **Data Profiling**.

### 2. Step-by-Step Profiling Configuration:
- **Step 1:** In Power Query Editor, click the **View Tab** in the top ribbon.
- **Step 2:** Locate the **Data Preview** group.
- **Step 3:** Enable the first checkbox: **Column Quality**.
  - *Effect:* A tri-color quality metric appears beneath every column header:
    - 🟩 **Green (Valid %):** Successfully parsed records.
    - 🟥 **Red (Error %):** Syntax or data conversion exceptions.
    - ⬜ **Grey (Empty %):** Missing or explicit NULL values.
- **Step 4:** Enable the second checkbox: **Column Distribution**.
  - *Effect:* Renders a frequency histogram illustrating unique and distinct value counts.
- **Step 5:** Enable the third checkbox: **Column Profile**.
  - *Effect:* Opens a bottom pane rendering detailed descriptive statistics (Min, Max, Mean, Standard Deviation, Null Counts, and Value Distributions).
- **Step 6 (Crucial Setting - Full Dataset Profiling):**
  - By default, profiling assesses only the initial 1,000 rows.
  - Locate the bottom status bar indicator: `Column profiling based on top 1000 rows`.
  - Click the text and select **Column profiling based on entire data set**.
  - Power BI will now execute profiling across 100% of rows.

### 3. Direct Actions From Quality Indicators:
- Hover your cursor directly over the **Quality Bar** (Green/Grey bar) under any header.
- A summary card appears (e.g., `Valid: 95%, Empty: 5%`).
- Click the **Three Dots (`...`)** menu to trigger immediate remediation actions such as **Remove Empty** or **Replace Values**.

---

## 📌 Topic 2.3: Data Type Casting & Cleaning Operations

### 🛠️ Operation 1: Explicit Data Type Casting

#### Technical Necessity:
If numerical columns such as `SalesAmount` default to Text (`ABC`), aggregate functions like Sum, Average, and DAX calculations will fail. Enforcing explicit typing is the foundational ETL step.

#### Step-by-Step UI Actions:
- **Step 1:** Click the header of the target column (e.g., `OrderDate`).
- **Step 2:** Click the data type glyph on the left of the header label (`ABC` or `123`).
- **Step 3:** Select the appropriate data type from the dropdown:
  - Temporal fields (`OrderDate`, `ShipDate`) ➡️ **Date**.
  - Integer counts (`Quantity`) ➡️ **Whole Number (123)**.
  - Financial amounts (`UnitPrice`, `Discount`, `SalesAmount`, `CostAmount`, `Profit`) ➡️ **Decimal Number (1.2)** or **Fixed Decimal Number ($)**.
  - Identifier keys (`OrderID`, `CustomerID`, `ProductID`, `PostalCode`) ➡️ **Text (ABC)** (Identifiers must not be stored as aggregatable numbers).
- **Step 4:** In the confirmation dialog (*"Change Column Type: Replace current step or Add new step?"*), select **Add new step** for audit transparency.
- **Step 5:** The step `Changed Type` is logged sequentially in the **Applied Steps** pane.

---

### 🛠️ Operation 2: Handling Missing / Null / Blank Values

#### Business Scenario:
In `sales_data_1000.csv`, non-returned merchandise in the `ReturnStatus` column displays literal `null`. We must replace `null` with the explicit status label **"Not Returned"**.

#### Step-by-Step UI Actions:
- **Step 1:** Select the `ReturnStatus` column header.
- **Step 2:** Right-click the header (or navigate to **Transform Tab** > **Any Column Group** > **Replace Values**).
- **Step 3:** Select **Replace Values...**.
- **Step 4:** In the modal dialog:
  - **Value To Find:** Enter `null` (lowercase).
  - **Replace With:** Enter `Not Returned`.
- **Step 5:** Click **OK**.
- **Step 6:** Inspect the grid: All `null` cells now reflect the sanitized string "Not Returned".

#### Fill Down / Fill Up (Resolving Merged Cell Artifacts):
- When data migrated from Excel contains sectional headers with blank child rows:
  - **Step 1:** Select the affected column.
  - **Step 2:** In the ribbon, click the **Transform Tab**.
  - **Step 3:** Within the **Any Column** group, open the **Fill** dropdown.
  - **Step 4:** Select **Down** to propagate values downward into blank rows.

---

### 🛠️ Operation 3: Deduplication and Error Elimination

#### Business Scenario:
Eliminate duplicate transaction entries in the Fact table and enforce primary key uniqueness across dimension lookup tables.

#### Step-by-Step UI Actions (Enforcing Key Uniqueness):
- **Step 1:** Select the entity key column (e.g., `OrderID` or `CustomerID`).
- **Step 2:** Right-click the column header.
- **Step 3:** Click **Remove Duplicates**.
  - *(Ribbon alternative: Home Tab > Reduce Rows Group > Remove Rows > Remove Duplicates)*.
- **Step 4:** Power Query retains the first instance and purges subsequent duplicate records.

#### Purging Corrupt / Error Records:
- **Step 1:** Highlight the column displaying red error indicators.
- **Step 2:** Navigate to **Home Tab** in the ribbon.
- **Step 3:** Open the **Remove Rows** dropdown in the **Reduce Rows** group.
- **Step 4:** Click **Remove Errors**.

---

### 🛠️ Operation 4: Header Promotion

#### Business Scenario:
When importing CSV/Excel files, attribute names (e.g., `OrderID`, `SalesAmount`) occasionally land in Data Row 1, while default headers show generic names like `Column1`, `Column2`.

#### Step-by-Step UI Actions:
- **Step 1:** Navigate to the **Home Tab** in the ribbon.
- **Step 2:** Locate the **Use First Row as Headers** command within the **Transform** group.
- **Step 3:** Click the button.
- **Step 4:** Row 1 is promoted to primary column headers.
  - *(To revert: Click the adjacent arrow and select **Use Headers as First Row**)*.

---

### 🛠️ Operation 5: Removing Redundant Columns (Schema Optimization)

#### Best Practice Rule: Remove Columns vs. Remove Other Columns
- **Remove Columns:** Deletes explicitly selected columns. (Fragile: New columns added at the source will be unintentionally ingested into memory).
- **Remove Other Columns (Recommended):** Retains strictly selected columns and drops everything else, ensuring deterministic schema boundaries.

#### Step-by-Step UI Actions:
- **Step 1:** Hold down the `Ctrl` key on your keyboard.
- **Step 2:** Click each required column header: `OrderID`, `OrderDate`, `CustomerID`, `ProductID`, `SalesAmount`, `Profit`.
- **Step 3:** Right-click on any selected header.
- **Step 4:** Select **Remove Other Columns**.
- **Step 5:** All unselected columns are permanently excluded, minimizing memory overhead.

---

## 📌 Topic 2.4: Text, Number & Date Transformations

> [!IMPORTANT]
> **Architectural Distinction: Transform Tab vs. Add Column Tab:**
> - **Transform Tab:** Overwrites and replaces values in-place within the selected column.
> - **Add Column Tab:** Leaves the source column untouched and computes a **New Output Column**.

---

### 1. Text Transformation (Splitting & Formatting)

#### Practical Scenario A: Parsing Username and Domain from Email
Parse `CustomerEmail` (e.g., `arman.khan@example.com`) into separate user identifier and domain columns.

- **Step 1:** Select the `CustomerEmail` column header.
- **Step 2:** Go to **Home Tab** (or **Transform Tab**).
- **Step 3:** Click the **Split Column** dropdown in the **Transform** group.
- **Step 4:** Select **By Delimiter**.
- **Step 5:** In the configuration window:
  - **Select or enter delimiter:** Choose Custom and input `@`.
  - **Split at:** Select **Each occurrence of the delimiter** (or Left-most delimiter).
- **Step 6:** Click **OK**.
- **Step 7:** The column splits into `CustomerEmail.1` (username) and `CustomerEmail.2` (domain).
- **Step 8:** Double-click each header to rename them to `Username` and `EmailDomain`.

#### Practical Scenario B: String Sanitization (Stripping Whitespace & Casing)
Source customer names often contain trailing or irregular whitespace (e.g., `"  Arman Khan   "`).

- **Step 1:** Select the target column (e.g., `CustomerName`).
- **Step 2:** Click the **Transform Tab** in the ribbon.
- **Step 3:** Open the **Format** dropdown within the **Text Column** group.
- **Step 4:** Select **Trim** to eliminate leading and trailing whitespace.
- **Step 5:** Re-open **Format** and select **Clean** to strip non-printable ASCII control characters.
- **Step 6:** For title casing, select **Capitalize Each Word** (e.g., `arman khan` ➡️ `Arman Khan`).

---

### 2. Date & Time Transformation (Calendar Feature Engineering)

#### Practical Scenario:
Derive Year, Month Name, and Day of Week from `OrderDate` (e.g., `2024-02-13`) without writing complex formula strings.

#### Step-by-Step UI Actions (Add Column Tab):
- **Step 1:** Select the `OrderDate` column header.
- **Step 2:** Click the **Add Column Tab** in the ribbon (preserves original timestamps).
- **Step 3:** Within the **From Date & Time** group, click the **Date** dropdown.
- **Step 4 (Extract Year):**
  - Select: **Year** ➡️ **Year**.
  - *Result:* Creates a new column containing four-digit year values (e.g., `2024`).
- **Step 5 (Extract Month Name):**
  - Select `OrderDate` again.
  - Ribbon > **Add Column Tab** > **Date** > **Month** ➡️ **Name of Month**.
  - *Result:* Creates an attribute column populated with string month labels (e.g., `February`).
- **Step 6 (Extract Day of Week):**
  - Select `OrderDate` again.
  - Ribbon > **Add Column Tab** > **Date** > **Day** ➡️ **Name of Day**.
  - *Result:* Outputs textual day names (e.g., `Tuesday`).

---

### 3. Number Transformation (Rounding & Math Operations)

#### Step-by-Step UI Actions:
- **Step 1:** Select a numeric column (e.g., `Profit` or `SalesAmount`).
- **Step 2:** Click the **Transform Tab** in the ribbon.
- **Step 3:** Within the **Number Column** group:
  - Open **Rounding** ➡️ select **Round...** ➡️ input decimal precision `2` ➡️ click **OK**.
  - Open **Standard** to perform arithmetic operations (Add, Multiply, Divide, Percentage) directly in the ETL layer without DAX overhead.

---

## 📌 Topic 2.5: Pivot vs. Unpivot Columns (Critical Technical Interview Topic)

### 1. Conceptual Framework: Wide vs. Tall Datasets

| Parameter | Wide Format (Sub-optimal for BI ❌) | Tall / Normalized Format (Standard BI Best Practice ✅) |
| :--- | :--- | :--- |
| **Structure** | Separate metrics span horizontal columns (e.g., `Jan_Sales`, `Feb_Sales`, `Mar_Sales`). | Standardized into two key columns: an Attribute/Date dimension and a numerical Measure value. |
| **Limitations** | Precludes dynamic temporal slicing, breaks standard Time-Intelligence DAX, and hardcodes schema columns. | Enables seamless multi-level slicers, cross-filtering, dynamic aggregations, and standard Time-Intelligence. |
| **Remediation** | Execute **Unpivot Columns** to normalize horizontal attributes into vertical rows. | Serves as the bedrock schema for performant VertiPaq tabular modeling. |

#### Structural Visual Comparison:
```   
[ BEFORE UNPIVOT (Wide Table) ]
ProductID | ProductName | Jan_Sales | Feb_Sales | Mar_Sales
PRD-101   | Laptop      | 5000      | 6200      | 4800

                 ⬇️ [ UNPIVOT OTHER COLUMNS OPERATION ] ⬇️

[ AFTER UNPIVOT (Tall Table) ]
ProductID | ProductName | Month     | Sales
PRD-101   | Laptop      | Jan_Sales | 5000
PRD-101   | Laptop      | Feb_Sales | 6200
PRD-101   | Laptop      | Mar_Sales | 4800
```

---

### 🛠️ Step-by-Step Hands-on Lab on `unpivot_exercise_data.csv`:

- **Step 1 (Ingest Source File):**
  - In the ribbon, click **Home Tab**.
  - In the **New Query** group, click **New Source** > **Text/CSV**.
  - Select: `d:\YSM Info Solution\Data Analytics &Cyber Security\python\Power BI\data\unpivot_exercise_data.csv`.
  - In the preview dialog, click **OK**.
- **Step 2 (Analyze Schema):**
  - Observe that the first 4 columns are static categorical keys (`ProductID`, `ProductName`, `Category`, `Region`).
  - The remaining 12 columns represent unnormalized month intervals: `Jan_Sales`, `Feb_Sales`, ..., `Dec_Sales`.
- **Step 3 (Select Static Anchor Columns):**
  - Press and hold `Ctrl`.
  - Sequentially select the 4 static columns:
    - Click `ProductID`
    - Click `ProductName`
    - Click `Category`
    - Click `Region`
- **Step 4 (Execute Unpivot):**
  - Right-click on any of the selected 4 headers.
  - Select **Unpivot Other Columns**.
  - *(Ribbon Path: Transform Tab > Any Column Group > Unpivot Columns dropdown > Unpivot Other Columns)*.
- **Step 5 (Evaluate Normalized Output):**
  - The 12 horizontal month columns collapse instantly.
  - Two normalized columns appear:
    - **Attribute:** Contains row entries (`Jan_Sales`, `Feb_Sales`, etc.).
    - **Value:** Contains corresponding transactional amounts.
- **Step 6 (Renaming & Typing):**
  - Double-click `Attribute` and rename to **`Month`**.
  - Double-click `Value` and rename to **`MonthlySales`**.
  - Click the type glyph on `MonthlySales` and assign **Decimal Number**.

---

## 📌 Topic 2.6: Merge Queries (Joins) vs. Append Queries (Unions)

### 1. Architectural Distinction:
- **Merge Queries (Horizontal Joins):** Merges two tables horizontally based on common matching keys (equivalent to SQL JOIN or Excel VLOOKUP).
- **Append Queries (Vertical Unions):** Stacks records vertically across two or more tables (equivalent to SQL UNION ALL). Requires identical schema headers for seamless unioning.

---

### 🛠️ Practical 1: Merge Queries (VLOOKUP Replacement in Power Query)

#### Business Scenario:
The `sales_data_1000` table contains only foreign key `ProductID` (`PRD-101`). We must join `product_dim` to bring `ProductName` and `Category` into the fact stream.

#### Step-by-Step UI Actions:
- **Step 1:** Select the `sales_data_1000` query in the left **Queries Pane**.
- **Step 2:** In the ribbon, click the **Home Tab**.
- **Step 3:** In the **Combine** group, open the **Merge Queries** dropdown:
  - Select **Merge Queries** (choose *Merge Queries as New* if creating an isolated combined table).
- **Step 4:** In the Merge dialog:
  - In the upper table preview (`sales_data_1000`), click the **`ProductID`** column to highlight it.
  - In the secondary dropdown, select the dimension table: **`product_dim`**.
  - In the lower preview grid, click the **`ProductID`** column to establish the relational key link.
- **Step 5 (Select Join Kind):**
  - From the **Join Kind** dropdown, select **Left Outer (all from first, matching from second)**.
- **Step 6 (Verify Match Diagnostic):**
  - Check the bottom diagnostic readout:
    `The selection matches 1000 of 1000 rows from the first table.`
- **Step 7:** Click **OK**.
- **Step 8 (Expand Nested Tables):**
  - A nested table column named `product_dim` appears at the right edge of the grid.
  - Click the **Expand Icon (`⮂`)** on the right side of the column header.
- **Step 9:** In the expansion dialog:
  - Uncheck **(Select All Columns)**.
  - Check only the needed attributes: ✅ **`ProductName`** and ✅ **`Category`**.
  - Uncheck **"Use original column name as prefix"** to prevent prefixes like `product_dim.ProductName`.
- **Step 10:** Click **OK**.
- **Step 11:** Verify the result: Product names and categories are now merged into the sales dataset.

---

### 2. Join Types Reference Matrix:

| Join Type | Execution Mechanics | Business Use Case |
| :--- | :--- | :--- |
| **Left Outer** | Retains 100% of rows from Left table + matching records from Right table. | Preserves all sales records regardless of whether master catalog lookup exists. |
| **Right Outer** | Retains 100% of rows from Right table + matching records from Left table. | Audits entire product catalog including items with zero historical sales. |
| **Full Outer** | Retains all records across both tables, filling mismatches with nulls. | Reconciliations and comprehensive inventory-versus-sales audits. |
| **Inner Join** | Retains strictly rows that match across both tables. | Filters out orphan transactions where master dimensions are missing. |
| **Left Anti** | Isolates records present in Left table but absent from Right table. | **Data Quality Audit:** Identifies transactions referencing invalid product keys. |
| **Right Anti** | Isolates records present in Right table but absent from Left table. | Pinpoints dead inventory: Products sitting in warehouse that never sold. |

---

### 🛠️ Practical 2: Append Queries (Vertical Record Stacking)

#### Business Scenario:
The business maintains historical annual transaction logs across three files: `Sales_2022.csv`, `Sales_2023.csv`, and `Sales_2024.csv`. Consolidate these into a unified master fact table.

#### Step-by-Step UI Actions:
- **Step 1:** In the ribbon, navigate to **Home Tab**.
- **Step 2:** In the **Combine** group, open the **Append Queries** dropdown.
- **Step 3:** Select **Append Queries as New** to preserve individual annual staging queries.
- **Step 4:** In the modal dialog:
  - For two tables: Choose **Two tables**.
  - For three or more files: Select **Three or more tables**.
- **Step 5:** Highlight the source tables in the left box and click **Add >>** to move them into the append staging container.
- **Step 6:** Click **OK**.
- **Step 7:** Rename the resulting query `Append1` to **`All_Sales_Master`**.
- **Step 8:** Verify column schema alignment and data types across the merged records.

---

## 📌 Topic 2.7: Conditional Columns & Custom Columns

### 🛠️ Operation 1: Conditional Columns (Rule-Based Branching)

#### Business Scenario:
Segment transactions based on `SalesAmount` thresholds:
- If `SalesAmount` >= 2000 ➡️ **"High Value"**
- If `SalesAmount` >= 500 ➡️ **"Medium Value"**
- Otherwise ➡️ **"Low Value"**

#### Step-by-Step UI Actions:
- **Step 1:** Navigate to **Add Column Tab** in the ribbon.
- **Step 2:** Click **Conditional Column** within the **General** group.
- **Step 3:** In the configuration dialog:
  - **New column name:** Set to `SalesCategory`.
  - **First Clause (If):**
    - *Column Name:* Select `SalesAmount`.
    - *Operator:* Select `is greater than or equal to`.
    - *Value:* Input `2000`.
    - *Output:* Input `High Value`.
  - **Second Clause (Else If):**
    - Click **Add Clause**.
    - *Column Name:* `SalesAmount`
    - *Operator:* `is greater than or equal to`
    - *Value:* Input `500`.
    - *Output:* Input `Medium Value`.
  - **Default Clause (Else):**
    - *Else:* Input `Low Value`.
- **Step 4:** Click **OK**.
- **Step 5:** Cast the newly created column to **Text (ABC)**.

---

### 🛠️ Operation 2: Custom Columns (M-Formula Expressions)

#### 🔹 Scenario A: Direct Calculation (Net Margin)
Calculate per-transaction **Net Margin**:
- **Formula:** `[SalesAmount] - [CostAmount]`
- **Data Type:** `Decimal Number (1.2)` (Permits downstream aggregations).

---

#### 🔹 Scenario B: Compound Conditional Strings (Margin + Status)
Construct an informational status string displaying margin difference and business profitability state:

```
Sample Output:
- "Profit: +450.50"
- "Loss: -120.00"
- "Break-Even: 0"
```

#### Step-by-Step UI Actions:
- **Step 1:** Open the **Add Column Tab** in the ribbon.
- **Step 2:** Click **Custom Column** in the **General** group.
- **Step 3:** In the dialog:
  - **New column name:** Input `MarginDetails`.
  - **Custom column formula (`=`):** Enter the M expression:
    ```powerquery
    if ([SalesAmount] - [CostAmount]) > 0 then 
        "Profit: +" & Text.From([SalesAmount] - [CostAmount])
    else if ([SalesAmount] - [CostAmount]) < 0 then 
        "Loss: " & Text.From([SalesAmount] - [CostAmount])
    else 
        "Break-Even: 0"
    ```
    
    *(Structured syntax utilizing `let ... in`):*
    ```powerquery
    let
        diff = [SalesAmount] - [CostAmount]
    in
        if diff > 0 then "Profit: +" & Text.From(diff)
        else if diff < 0 then "Loss: " & Text.From(diff)
        else "Break-Even: 0"
    ```

- **Step 4 (Syntax Check):** Verify the diagnostic indicator reads: `No syntax errors have been detected.`
- **Step 5:** Click **OK**.
- **Step 6:** Assign the data type to **Text (ABC)**.

> [!WARNING]
> **Power Query M-Language Syntax Rules:**
> 1. M is strictly **case-sensitive**. Keywords `if`, `then`, and `else` must be lowercase. Using uppercase `IF` triggers syntax compilation errors.
> 2. Concatenating numerical expressions with strings using the `&` operator requires explicit type casting via `Text.From()`.

---

### 🛠️ Operation 3: Column From Examples (AI-Driven Pattern Inference)

#### Business Scenario:
Synthesize formatted customer addresses from existing fields without authoring string manipulation expressions.

#### Step-by-Step UI Actions:
- **Step 1:** In the ribbon, click **Add Column Tab**.
- **Step 2:** Click **Column From Examples** within the **General** group (choose *From Selection* or *From All Columns*).
- **Step 3:** A new temporary column appears at the far right.
- **Step 4:** In Row 1, manually type the intended pattern (e.g., `City, State`).
- **Step 5:** Press `Enter`. Power Query infers the underlying transformation logic and populates all remaining rows.
- **Step 6:** Review the generated expression in the formula bar and click **OK**.

---

## 📌 Topic 2.8: Group By (ETL Aggregations) & Advanced Editor (M Anatomy)

### 🛠️ Operation 1: Group By (Pre-aggregating Data)

#### Business Scenario:
Roll up granular line-item records into pre-aggregated **Regional Total Sales** and **Transaction Counts**.

#### Step-by-Step UI Actions:
- **Step 1:** Open the **Transform Tab** (or **Home Tab**) in the ribbon.
- **Step 2:** Click **Group By** in the **Transform** group.
- **Step 3:** In the dialog:
  - Select the **Advanced** radio button.
  - Set grouping field: Select **`Region`**.
  - **Aggregation 1 (Total Revenue):**
    - *New column name:* `TotalRegionalSales`
    - *Operation:* `Sum`
    - *Column:* `SalesAmount`
  - Click **Add aggregation**.
  - **Aggregation 2 (Volume):**
    - *New column name:* `TransactionCount`
    - *Operation:* `Count Rows`
- **Step 4:** Click **OK**.
- **Step 5:** The dataset rolls up into distinct regions with aggregated metrics.

---

### 🛠️ Operation 2: Advanced Editor (M Script Structure)

#### Understanding M-Code:
Every visual button interaction in Power Query compiles into declarative code written in **M (Mashup Language)**.

#### Inspecting M-Code:
- **Step 1:** Go to the **Home Tab** (or **View Tab**).
- **Step 2:** Click **Advanced Editor** in the **Query** group.
- **Step 3:** Review the procedural step definition:

```powerquery
let
    // Step 1: Connect to source file
    Source = Csv.Document(File.Contents("d:\YSM Info Solution\Data Analytics &Cyber Security\python\Power BI\data\sales_data_1000.csv"), [Delimiter=",", Columns=17, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    
    // Step 2: Promote Row 1 to header
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    
    // Step 3: Enforce strict schema types
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"OrderID", type text}, {"OrderDate", type date}, {"SalesAmount", type number}}),
    
    // Step 4: Handle missing values
    #"Replaced Value" = Table.ReplaceValue(#"Changed Type",null,"Not Returned",Replacer.ReplaceValue,{"ReturnStatus"})
in
    // Final output committed to memory
    #"Replaced Value"
```

#### Structural Mechanics of M:
1. **`let` Block:** Defines sequential immutable transformations. Each line concludes with a comma (`,`), except the final evaluation step.
2. **`in` Block:** Specifies which evaluated transformation variable serves as the return value of the query.

---

## 📌 Topic 2.9: Query Architecture & Committing Changes

### 1. Enable Load vs. Include in Report Refresh (Memory Architecture Trick ⭐):

#### Business Scenario:
When staging tables are merged into an integrated master fact table, loading intermediate staging queries into the Power BI memory model wastes system RAM.

#### Step-by-Step UI Actions:
- **Step 1:** In the left **Queries Pane**, locate the intermediate staging query.
- **Step 2:** Right-click the query name.
- **Step 3:** Click **Enable Load** to uncheck it.
- **Step 4:** In the confirmation dialog (*"Disabling load may cause data loss in report visuals"*), select **Continue**.
- **Step 5:** The query title italicizes. The query remains active in the ETL pipeline for transformation dependencies but is excluded from RAM consumption in the report model.

---

### 2. Organizing Queries into Groups (Folders):
- **Step 1:** Right-click any blank area within the left **Queries Pane**.
- **Step 2:** Select **New Group...**.
- **Step 3:** Enter descriptive names: `01_Staging_Data`, `02_Dimensions`, or `03_Facts`.
- **Step 4:** Drag and drop queries into respective folders for clear governance.

---

### 3. Committing Transformations to Power BI Desktop:

Upon completing all cleaning and transformation steps:
- **Step 1:** Click the **Home Tab** in the ribbon.
- **Step 2:** Locate the **Close & Apply** split-button on the far left.
- **Step 3:** Select from the action modes:
  - **Close & Apply:** Saves transformation steps, closes Power Query Editor, and populates the data model.
  - **Apply:** Persists transformations to the model while keeping the Power Query workspace open.
  - **Close:** Closes the editor without committing pending transformations.
- **Step 4:** Observe the synchronization modal:
  `sales_data_1000: 1000 rows loaded.`
- **Step 5:** In the right **Data Pane**, all cleaned tables and attributes are now available for visual authoring.

---

## 📌 Topic 2.10: Hands-On Practice Checklist (Student Lab Challenge)

Complete these 10 sequential lab tasks to validate mastery of Power Query ETL:

- [ ] **Task 1:** Connect `sales_data_1000.csv` to Power BI Desktop and select **Transform Data**.
- [ ] **Task 2:** Under the View tab, enable **Column Quality** and **Column Profile** (configured across entire dataset).
- [ ] **Task 3:** Cast `OrderDate` and `ShipDate` to **Date**, and `SalesAmount` to **Decimal Number**.
- [ ] **Task 4:** Replace all `null` entries in `ReturnStatus` with the literal string **"Not Returned"**.
- [ ] **Task 5:** From `OrderDate`, extract **Month Name** into a new column via the Add Column tab.
- [ ] **Task 6:** Import `unpivot_exercise_data.csv` and execute **Unpivot Other Columns** to produce a tall monthly sales schema.
- [ ] **Task 7:** Perform a **Merge Queries** operation between `sales_data_1000` and `product_dim` (Left Outer Join on `ProductID`) and expand `ProductName`.
- [ ] **Task 8:** Add a **Conditional Column**: If `SalesAmount >= 1000` ➡️ "High", Else ➡️ "Standard".
- [ ] **Task 9:** Add a **Custom Column**: `NetProfit = [SalesAmount] - [CostAmount]`.
- [ ] **Task 10:** Click **Close & Apply** to commit the cleaned data into the report model.
