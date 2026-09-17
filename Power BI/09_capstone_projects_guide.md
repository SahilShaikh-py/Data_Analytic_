# 🏆 Module 9: Real-World Industry Capstone Projects (Portfolio & Interview Ready)

### 🎯 Objective:
Guide learners through building four comprehensive, end-to-end industrial dashboards from raw ingestion to cloud deployment. These projects equip students with a portfolio-ready body of work for resumes, GitHub repositories, and NovyPro showcases. Each project is presented across six structured implementation phases.

---

## 🚀 Project 1: Global E-Commerce & Retail Performance Suite

- **Industry Domain:** Retail, FMCG & E-Commerce Analytics
- **Target Audience:** Chief Commercial Officer (CCO) & Regional Sales Executives
- **Source Files:**
  - `data/sales_data_1000.csv` (Transactions Fact)
  - `data/customer_dim.csv` (Customer Dimension)
  - `data/product_dim.csv` (Product Dimension)

---

### 📋 Phase-by-Phase Implementation Blueprint:

#### Phase 1: Data Ingestion & Power Query ETL
- **Step 1:** In Power BI Desktop, navigate to `Home > Get Data > Text/CSV`, select all three source files, and click **Transform Data**.
- **Step 2:** In `sales_data_1000`, cast `OrderDate` and `ShipDate` to **Date**, and `SalesAmount` and `Profit` to **Decimal Number**.
- **Step 3:** Right-click `ReturnStatus` ➡️ **Replace Values...** ➡️ substitute `null` with `"Not Returned"`.
- **Step 4:** In `customer_dim`, apply `Transform > Format > Capitalize Each Word` to `CustomerName`.
- **Step 5:** Click **Close & Apply** in the top-left corner.

#### Phase 2: Relational Data Modeling (Star Schema)
- **Step 1:** Navigate to **Model View** on the left sidebar.
- **Step 2:** Position `sales_data_1000` centrally on the canvas.
- **Step 3:** Establish a `1:*` Single-direction relationship from `customer_dim[CustomerID]` to `sales_data_1000[CustomerID]`.
- **Step 4:** Establish a `1:*` Single-direction relationship from `product_dim[ProductID]` to `sales_data_1000[ProductID]`.
- **Step 5:** Click **New Table** in the Modeling tab to construct `Dim_Calendar` via DAX, linking its `Date` key to `sales_data_1000[OrderDate]`.
- **Step 6:** Right-click `CustomerID` and `ProductID` in the Fact table and select **Hide in report view**.

#### Phase 3: Core DAX Metrics (`_All_Measures` Table)
- **Step 1:** Create an isolated measure repository table named **`_All_Measures`** via `Home > Enter Data`.
- **Step 2:** Author the following core measures:
  ```dax
  Total Revenue = SUM(sales_data_1000[SalesAmount])
  Total Profit = SUM(sales_data_1000[Profit])
  Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)
  Total Orders = COUNTROWS(sales_data_1000)
  YoY Sales Growth % = 
  VAR CurrentSales = [Total Revenue]
  VAR PYSales = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(Dim_Calendar[Date]))
  RETURN
      DIVIDE(CurrentSales - PYSales, PYSales, 0)
  ```

#### Phase 4: Canvas Layout & Executive Visuals Grid
- **Header Banner:** Dark slate banner (`#0F172A`) displaying report title *"Global Sales & Commercial Intelligence"*, corporate branding logo, and a temporal Date Slicer.
- **Row 1 (Executive KPI Ribbon):**
  - **New Card Visual:** Bind `[Total Revenue]`, `[Total Profit]`, `[Profit Margin %]`, and `[Total Orders]`.
  - Apply Royal Blue accent borders (`#2563EB`) and rounded corner cards (`8px`).
- **Row 2 (Analytical Trends & Proportions):**
  - **Left Visual:** Dual-Axis Line and Clustered Column Chart (X-axis: `MonthName`, Columns: `Total Revenue`, Line: `Profit Margin %`).
  - **Right Visual:** Treemap visualizing Category and SubCategory revenue distribution.
- **Row 3 (Geographic Breakdown & Customer Matrix):**
  - **Left Visual:** Donut Chart displaying Regional market share (`customer_dim[Region]`).
  - **Right Visual:** Customer Ranking Matrix with embedded conditional data bars on revenue.

#### Phase 5: Interactive UX Polish
- **View-Swapping Buttons:** Configure **Chart View 🔁 Table View** toggle controls via Bookmarks and the Selection pane.
- **Custom Tooltip Canvas:** Bind a product breakdown tooltip to the monthly trend chart.
- **Clear All Filters Action:** Add an interactive action button to reset slicer selections with a single click.

---

## 🚀 Project 2: Corporate HR Analytics & Employee Attrition Tracker

- **Industry Domain:** People Analytics & Human Resources
- **Target Audience:** Chief Human Resources Officer (CHRO) & Workforce Strategy Heads
- **Problem Statement:** What underlying organizational factors drive employee turnover, and which departments, compensation bands, and tenure cohorts suffer the greatest attrition risk?

---

### 📋 Key Metrics & Visual Architecture:

#### Core DAX Formulas:
```dax
Total Headcount = COUNTROWS(Fact_HR)
Total Attrition = CALCULATE(COUNTROWS(Fact_HR), Fact_HR[Attrition] = "Yes")
Attrition Rate % = DIVIDE([Total Attrition], [Total Headcount], 0)
Avg Monthly Income = AVERAGE(Fact_HR[MonthlyIncome])
Avg Years at Company = AVERAGE(Fact_HR[YearsAtCompany])
```

#### Executive Dashboard Layout:
1. **Executive KPI Ribbon:** Total Headcount (1,470), Total Leavers (237), Attrition Rate % (16.1%), and Average Monthly Salary ($6,500).
2. **AI Decomposition Tree:**
   - **Analyze:** `[Total Attrition]`.
   - **Explain by:** `Department ➡️ JobRole ➡️ OverTime ➡️ MaritalStatus`.
   - *Key Business Finding:* R&D staff working uncompensated overtime exhibit a 3.4x higher probability of departure.
3. **Demographic Cohort Analysis:**
   - Stacked Column Chart: X-axis: Age Cohorts (Under 25, 25-34, 35-44, 45+), Y-axis: Headcount, Legend: Attrition Status (Yes/No).
4. **Satisfaction vs. Attrition Correlation Matrix:**
   - Heatmap Matrix mapping Job Satisfaction levels against attrition frequency.

---

## 🚀 Project 3: Executive Financial P&L & Profitability Suite

- **Industry Domain:** Corporate Finance & Investment Banking
- **Target Audience:** Chief Financial Officer (CFO) & Board of Directors
- **Problem Statement:** Provide an executive profit-and-loss walk from Gross Sales to Net Profit (EBITDA), highlighting quarterly budget variances.

---

### 📋 Key Metrics & Visual Architecture:

#### Core DAX Formulas:
```dax
Gross Revenue = SUM(Fact_Financials[GrossSales])
COGS = SUM(Fact_Financials[CostOfGoodsSold])
Gross Profit = [Gross Revenue] - [COGS]
Gross Margin % = DIVIDE([Gross Profit], [Gross Revenue], 0)
Operating Expenses = SUM(Fact_Financials[OPEX])
Net Profit (EBITDA) = [Gross Profit] - [Operating Expenses]
Net Margin % = DIVIDE([Net Profit (EBITDA)], [Gross Revenue], 0)
```

#### Executive Dashboard Layout:
1. **Financial Waterfall Chart (P&L Walk):**
   - **Category Breakdown:** Gross Sales ➡️ Discounts ➡️ Net Revenue ➡️ COGS ➡️ Gross Margin ➡️ OPEX ➡️ Taxes ➡️ Net Profit.
   - **Color Logic:** Green for revenue additions, Red for expense deductions, Navy for subtotal pillars.
2. **Quarterly Budget Variance Tracking:**
   - Line Chart plotting Actual Net Profit against Budget Targets across quarters (`Q1`, `Q2`, `Q3`, `Q4`).
3. **Operating Expense Decomposition:**
   - Donut chart breaking down OPEX across R&D, Marketing, Administrative, and Infrastructure cost centers.

---

## 🚀 Project 4: Supply Chain, Inventory & Delivery Logistics

- **Industry Domain:** Logistics, Warehousing & Supply Chain Operations
- **Target Audience:** Chief Operating Officer (COO) & Global Logistics Directors
- **Problem Statement:** Track On-Time In-Full (OTIF) fulfillment rates, identify transportation bottleneck hubs, and minimize shipment transit delays.

---

### 📋 Key Metrics & Visual Architecture:

#### Core DAX Formulas:
```dax
Total Shipments = COUNTROWS(Fact_Logistics)
On-Time Deliveries = CALCULATE(COUNTROWS(Fact_Logistics), Fact_Logistics[DeliveryStatus] = "On Time")
On-Time Delivery Rate % = DIVIDE([On-Time Deliveries], [Total Shipments], 0)
Avg Delivery Days = AVERAGE(Fact_Logistics[ActualDeliveryDays])
Delayed Shipments = CALCULATE(COUNTROWS(Fact_Logistics), Fact_Logistics[DeliveryStatus] = "Delayed")
```

#### Executive Dashboard Layout:
1. **SLA Delivery Gauge Visual:**
   - Active Metric: `[On-Time Delivery Rate %]`.
   - SLA Target Threshold: `95.0%`.
   - Scale: 50% to 100%.
2. **Geographic Route Map:**
   - Location: `DestinationCity`, Bubble Magnitude: `Total Shipments`, Color Threshold: `On-Time Delivery Rate %`.
3. **Fulfillment Mode Clustered Bar:**
   - Y-axis: `ShipMode` (Standard, Express, Same Day).
   - X-axis: `Avg Delivery Days` vs. `Contracted SLA Target Days`.

---

## 📌 Topic 9.5: Portfolio Presentation & GitHub / NovyPro Publication Guide

Follow these guidelines to present your analytics portfolio effectively to hiring managers:

### 1. High-Resolution Visual Asset Capture:
- Enter presentation mode in Power BI Desktop (`View > Full screen`).
- Use the Windows Snipping Tool (`Win + Shift + S`) to capture crisp, uncompressed screenshots of every dashboard page.

### 2. Standard GitHub Repository Architecture:
Organize your project repository cleanly:
```text
📦 Power-BI-Executive-Analytics-Portfolio
 ┣ 📂 datasets
 ┃ ┣ 📜 sales_data_1000.csv
 ┃ ┣ 📜 customer_dim.csv
 ┃ ┗ 📜 product_dim.csv
 ┣ 📂 pbix_reports
 ┃ ┗ 📜 Global_Retail_Sales_Dashboard.pbix
 ┣ 📂 screenshots
 ┃ ┣ 🖼️ executive_summary_page.png
 ┃ ┗ 🖼️ drillthrough_details_page.png
 ┗ 📜 README.md (Business problem, DAX definitions, key findings, live embed link)
```

### 3. Publishing Interactive Web Demos via NovyPro:
- Deploy the report to Power BI Service ➡️ `File > Embed report > Publish to web (public)`.
- Submit the public embed code to [NovyPro.com](https://www.novypro.com) to provide recruiters with an interactive live link to evaluate your slicers, tooltips, and dashboard interactions without requiring corporate credentials.
