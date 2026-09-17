# 📙 Module 3: Data Modeling & Relationships (The Backbone of Power BI)

### 🎯 Objective:
Architect a robust relational data model adhering to the **Star Schema** enterprise design standard. Configure Cardinality and Cross-Filter directions, manage Active and Inactive relationships via DAX, build an independent **Master Calendar Table**, and resolve the canonical **Sort by Column** issue. Every topic is demonstrated with exact UI click sequences, configuration options, and architectural best practices.

---

## 📂 Reference Datasets Path for this Module:
All hands-on data modeling labs reference these three relational tables:
- **Fact Table:** `d:\YSM Info Solution\Data Analytics &Cyber Security\python\Power BI\data\sales_data_1000.csv` (1,000 transactional order rows)
- **Customer Dimension:** `d:\YSM Info Solution\Data Analytics &Cyber Security\python\Power BI\data\customer_dim.csv` (100 unique customers)
- **Product Dimension:** `d:\YSM Info Solution\Data Analytics &Cyber Security\python\Power BI\data\product_dim.csv` (15 unique products)

---

## 📌 Topic 3.1: Relational Modeling Concepts (Primary Key vs. Foreign Key)

### 1. Conceptual Framework: Why Relationships are Mandatory
If customer profile attributes reside in `customer_dim` while transaction revenue is logged in `sales_data_1000`, attempting to summarize sales by customer without an active relational link produces distorted totals, repeated Cartesian products, and calculation errors.

### 2. Primary Key vs. Foreign Key:
1. **Primary Key (PK):** A column within a Dimension table that uniquely identifies each individual entity record with zero duplicates and no null values.
   - *Example:* **`CustomerID`** in `customer_dim` (`CUST-1001`, `CUST-1002`, ...).
   - *Example:* **`ProductID`** in `product_dim` (`PRD-101`, `PRD-102`, ...).
2. **Foreign Key (FK):** A column residing in the Fact table that references the Primary Key of an associated Dimension table. It naturally contains duplicate keys as customers complete multiple transactions over time.
   - *Example:* **`CustomerID`** and **`ProductID`** within `sales_data_1000`.

---

## 📌 Topic 3.2: Fact Tables vs. Dimension Tables

| Parameter | Fact Table (`sales_data_1000`) | Dimension Table (`customer_dim`, `product_dim`) |
| :--- | :--- | :--- |
| **Nature of Data** | Numerical, aggregatable business metrics (Sales, Profit, Quantity, Discount). | Descriptive contextual attributes, names, categories, geographic locations. |
| **Typical Attributes** | `SalesAmount`, `CostAmount`, `Profit`, `Quantity`, relational Foreign Keys. | `CustomerName`, `City`, `Region`, `ProductName`, `Category`. |
| **Row Cardinality** | High volume: tens of thousands to hundreds of millions of transaction rows. | Low volume: concise master entity records (hundreds to thousands of rows). |
| **Role in Visualizations** | Mapped to **Values / Y-Axis** for calculation (SUM, AVERAGE, MIN, MAX). | Mapped to **X-Axis, Slicers, Legends, Matrix Rows & Columns** for slicing. |

---

## 📌 Topic 3.3: Star Schema vs. Snowflake Schema

### 1. Star Schema (Industry Standard Best Practice ⭐):
- **Architecture:** A centralized **Fact Table** surrounded by and directly related to surrounding **Dimension Tables**, resembling a star pattern.
- **Why it is the Recommended Design:**
  - Power BI's in-memory **VertiPaq Engine** is engineered specifically for Star Schema query performance.
  - Slicers, cross-filtering, and visual interactions render with minimal latency.
  - DAX formula authoring remains intuitive and execution plans remain concise.

```
       +--------------------+
       |   customer_dim     |
       |  (1) [CustomerID]  |
       +---------+----------+
                 |
                 | (1 to Many: 1:*)
                 v
+----------------+------------------+         +--------------------+
|         sales_data_1000           |<--------|    product_dim     |
|   (*) [CustomerID, ProductID]     |  (1:*)  |  (1) [ProductID]   |
+----------------+------------------+         +--------------------+
                 ^
                 | (1 to Many: 1:*)
                 |
       +---------+----------+
       |    Dim_Calendar    |
       |     (1) [Date]     |
       +--------------------+
```

### 2. Snowflake Schema:
- **Architecture:** Dimension tables undergo secondary normalization into sub-dimension entities (e.g., `Fact_Sales` ➡️ `Product_Dim` ➡️ `SubCategory_Dim` ➡️ `Category_Dim`).
- **Architectural Disadvantages:** Increases relational join overhead, degrades visual rendering latency, and complicates DAX filter propagation. Best practice is to de-normalize dimensions during ETL into a clean **Star Schema**.

---

## 📌 Topic 3.4: Model View Interface & Managing Relationships

### 🧭 Model View Navigation Guide Path:
In the extreme left navigation bar of Power BI Desktop, click the 3rd icon:  
👉 **Model View (Relationship Diagram Icon)**

---

### 🛠️ Operation 1: Drag-and-Drop Relationship Creation

#### Business Scenario:
Establish One-to-Many (`1:*`) relationships connecting `customer_dim` and `product_dim` to `sales_data_1000`.

#### Step-by-Step UI Actions:
- **Step 1:** Click the **Model View** icon on the left sidebar.
- **Step 2:** The canvas will present diagram boxes for `customer_dim`, `product_dim`, and `sales_data_1000`.
- **Step 3 (Arrange Canvas):**
  - Place `sales_data_1000` in the center of the diagram.
  - Position `customer_dim` in the upper-left and `product_dim` in the upper-right quadrant.
- **Step 4 (Connect Customer Relationship):**
  - Click and hold the primary key field **`CustomerID`** in `customer_dim`.
  - Drag the cursor across to `sales_data_1000` and drop it directly onto the foreign key field **`CustomerID`**.
  - *Result:* A solid relational connector line links the two tables.
- **Step 5 (Connect Product Relationship):**
  - Click and drag **`ProductID`** from `product_dim` and drop it onto **`ProductID`** in `sales_data_1000`.
  - *Result:* A solid relational connector line links the product dimension to the fact table.

---

### 🛠️ Operation 2: Inspecting & Editing Relationship Properties

#### Step-by-Step UI Actions:
- **Step 1:** Double-click on any relational connector line (or right-click the line and select **Properties**).
- **Step 2:** The **Edit relationship** dialog will open:
  - Top Table: Displays `customer_dim` with `CustomerID` highlighted.
  - Bottom Table: Displays `sales_data_1000` with `CustomerID` highlighted.
- **Step 3 (Cardinality Dropdown):**
  - Verify that **`One to many (1:*)`** is selected.
  - *(Meaning: One distinct customer maps to multiple historical transaction rows).*
- **Step 4 (Cross Filter Direction Dropdown):**
  - Verify that **`Single`** is selected.
- **Step 5 (Active State):**
  - Confirm that the checkbox ✅ **Make this relationship active** is checked.
- **Step 6:** Click **OK**.

---

### Cardinality Reference Guide:

| Cardinality | Notation | Typical Relational Context | Design Rule |
| :--- | :---: | :--- | :--- |
| **One-to-Many (`1:*`)** | `1` ➡️ `*` | Dimension table (`1`) to Fact table (`*`) | ⭐ **Standard Practice!** Over 95% of enterprise links should be One-to-Many. |
| **Many-to-One (`*:1`)** | `*` ➡️ `1` | Fact table (`*`) to Dimension table (`1`) | Equivalent logic to One-to-Many with inverted table selection order. |
| **One-to-One (`1:1`)** | `1` ➡️ `1` | Symmetrical unique primary keys in both tables | Sub-optimal. Merge both tables into a unified entity in Power Query. |
| **Many-to-Many (`*:*`)** | `*` ➡️ `*` | Non-unique keys exist on both sides of the link | ⚠️ **Caution!** Prone to ambiguous Cartesian aggregates. Use a Bridge Table. |

---

## 📌 Topic 3.5: Cross-Filter Direction (Single vs. Both)

### 1. Conceptual Mechanics:
- **Single Direction (Arrow ➡️ Fact Table):**
  - Filters propagate unidirectionally from Dimension tables down to Fact tables.
  - *Example:* Slicing by Customer "Aarav Sharma" filters the Sales records; Sales activity does not inversely filter customer dimension tables.
- **Both Directions (Bi-Directional Filtering 🔁):**
  - Filters propagate bidirectionally between Fact and Dimension tables.
  - *Risks:* Bi-directional paths introduce circular ambiguity, non-deterministic calculation paths, and substantial query latency across enterprise models.
  - *Architectural Standard:* Enforce **Single** direction globally. When temporary bi-directional propagation is required for specific calculations, activate it dynamically using DAX `CROSSFILTER()`.

---

## 📌 Topic 3.6: Active vs. Inactive Relationships & `USERELATIONSHIP()`

### 1. Business Context: Role-Playing Dimensions
The `sales_data_1000` fact table contains two distinct temporal attributes:
1. **`OrderDate`** (Transaction submission timestamp)
2. **`ShipDate`** (Fulfillment dispatch timestamp)

Because a data model should connect to a single unified Calendar table (`Dim_Calendar`), and Power BI allows strictly **one active relationship** between any two tables at a time, secondary relationships are marked inactive.

### 2. Step-by-Step UI Configuration:
- **Step 1:** Open **Model View**.
- **Step 2 (Active Relationship):**
  - Drag `Dim_Calendar[Date]` onto `sales_data_1000[OrderDate]`.
  - *Result:* Represented by a **Solid Line** (Active Relationship). Standard sales metrics evaluate against order timestamps.
- **Step 3 (Inactive Relationship):**
  - Drag `Dim_Calendar[Date]` onto `sales_data_1000[ShipDate]`.
  - *Result:* Represented by a **Dotted Line (`- - - -`)** (Inactive Relationship).
- **Step 4 (Review Status):**
  - Double-click the dotted line to confirm the checkbox *"Make this relationship active"* is unchecked due to the existing active link. Click **Cancel**.

### 3. Programmatic Activation via DAX:
When executive reporting requires calculating fulfillment sales by dispatch date, activate the inactive path dynamically via `USERELATIONSHIP()`:

```dax
// Standard metric evaluating via active OrderDate relationship
Total Sales = SUM(sales_data_1000[SalesAmount])

// Fulfillment metric evaluating via inactive ShipDate relationship
Total Sales by Shipped Date = 
CALCULATE(
    [Total Sales],
    USERELATIONSHIP(sales_data_1000[ShipDate], Dim_Calendar[Date])
)
```

---

## 📌 Topic 3.7: Creating a Master Calendar Dimension using DAX

> [!IMPORTANT]
> **Why an Explicit Date Dimension is Mandatory:**
> Power BI's default "Auto Date/Time" engine generates hidden background calendar tables for every datetime column, increasing memory consumption by up to 10x. Production data models require an explicit centralized `Dim_Calendar` table to support standard Time Intelligence DAX functions (MTD, QTD, YTD, YoY).

---

### 🛠️ Step-by-Step Creation of `Dim_Calendar`:

- **Step 1:** In Power BI Desktop, click the **Modeling Tab** in the ribbon.
- **Step 2:** Within the **Calculations** group, click **New Table**.
- **Step 3:** Enter the following production DAX definition in the formula bar:

```dax
Dim_Calendar = 
VAR MinYear = YEAR(MIN(sales_data_1000[OrderDate]))
VAR MaxYear = YEAR(MAX(sales_data_1000[OrderDate]))
RETURN
ADDCOLUMNS(
    CALENDAR(DATE(MinYear, 1, 1), DATE(MaxYear, 12, 31)),
    "Year", YEAR([Date]),
    "MonthNumber", MONTH([Date]),
    "MonthName", FORMAT([Date], "MMMM"),
    "MonthShort", FORMAT([Date], "MMM"),
    "Quarter", "Q" & FORMAT([Date], "Q"),
    "YearMonth", FORMAT([Date], "YYYY-MM"),
    "DayOfWeekNumber", WEEKDAY([Date], 2),
    "DayOfWeekName", FORMAT([Date], "DDDD")
)
```

- **Step 4:** Press `Enter` to commit the table definition.
- **Step 5:** The new `Dim_Calendar` table appears in the **Data Pane**.
- **Step 6 (Mark as Official Date Table):**
  - Right-click `Dim_Calendar` in the Data Pane.
  - Select **Mark as date table** ➡️ **Mark as date table**.
  - In the configuration dialog, designate **`Date`** as the primary temporal column.
  - Click **OK**.

---

### 🛠️ Resolving the "Sort by Column" Issue (Month Sorting)

#### Problem Diagnosis:
When plotting `MonthName` (January, February, March...) on an axis or slicer, Power BI defaults to alphabetical sorting (April, August, December, February, January...), breaking chronological business presentation.

#### Step-by-Step Resolution:
- **Step 1:** In the left sidebar, navigate to **Table View** (Grid icon).
- **Step 2:** In the Data Pane, expand `Dim_Calendar`.
- **Step 3:** Click the header of the **`MonthName`** column.
- **Step 4:** The contextual **Column Tools Tab** will appear in the ribbon.
- **Step 5:** Within the **Sort** group, click the **Sort by column** dropdown.
- **Step 6:** Select the numerical sequence column: **`MonthNumber`**.
- **Step 7:** Visuals and slicers utilizing `MonthName` will now sort chronologically from January through December.

---

## 📌 Topic 3.8: Data Modeling Best Practices (Scalable Architecture)

### 1. Hide Foreign Keys from Report View:
- Foreign keys in Fact tables (`CustomerID`, `ProductID`) serve exclusively as relational join targets and should not be dragged directly onto report visual canvases.
- **Configuration:** In **Model View**, right-click `CustomerID` in `sales_data_1000` ➡️ select **Hide in report view**. Repeat for `ProductID`. This cleans the report authoring interface and guides report builders to use dimension attributes.

### 2. Disable Auto Date/Time Globally:
- **Configuration:** Navigate to `File > Options and settings > Options > Current File > Data Load` ➡️ uncheck **Auto Date/Time** ➡️ click **OK**. Disabling this reduces `.pbix` file size substantially and improves memory efficiency.

---

## 📌 Topic 3.9: Hands-On Practice Checklist (Student Lab Challenge)

- [ ] **Task 1:** Open Model View and arrange imported tables into a Star Schema visual layout.
- [ ] **Task 2:** Establish a `1:*` Single filter relationship from `customer_dim[CustomerID]` to `sales_data_1000[CustomerID]`.
- [ ] **Task 3:** Establish a `1:*` Single filter relationship from `product_dim[ProductID]` to `sales_data_1000[ProductID]`.
- [ ] **Task 4:** Create `Dim_Calendar` using the provided DAX table script under the Modeling tab.
- [ ] **Task 5:** Mark `Dim_Calendar` as an official Date Table.
- [ ] **Task 6:** Configure `MonthName` to sort by `MonthNumber` using **Sort by column**.
- [ ] **Task 7:** Link `Dim_Calendar[Date]` to `sales_data_1000[OrderDate]` (Active relationship).
- [ ] **Task 8:** Link `Dim_Calendar[Date]` to `sales_data_1000[ShipDate]` (Verify inactive relationship creation).
- [ ] **Task 9:** Hide Fact table foreign keys (`CustomerID`, `ProductID`) in Report View.
