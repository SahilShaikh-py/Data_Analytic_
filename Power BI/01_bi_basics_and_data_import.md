# 📘 Module 1: Business Intelligence Basics & Data Ingestion Guide
### 🎯 Objective:
Set up the Power BI environment, understand its core architectural layers, and perform step-by-step data ingestion of our **1,000-row enterprise sales dataset** into Power BI Desktop.

---

## 📂 Reference Dataset Path for this Module
Throughout this and subsequent modules, we will work with this interconnected relational dataset:
- **Primary Fact Data:** `d:\YSM Info Solution\Data Analytics &Cyber Security\python\Power BI\data\sales_data_1000.csv`
- **Customer Dimension:** `d:\YSM Info Solution\Data Analytics &Cyber Security\python\Power BI\data\customer_dim.csv`
- **Product Dimension:** `d:\YSM Info Solution\Data Analytics &Cyber Security\python\Power BI\data\product_dim.csv`

---

## 📌 Topic 1.1: Business Intelligence (BI) Fundamentals & Tool Comparison

### 1. Conceptual Framework
- **Business Intelligence (BI):** The discipline of transforming raw, transactional data (such as ERP transactions, logs, invoices, and CRM records) into actionable insights, interactive dashboards, and executive KPIs to empower rapid, data-informed business decisions.
- **Traditional BI vs. Modern Self-Service BI:**
  - *Traditional BI (e.g., SSRS, SAP Business Objects):* Required heavy dependency on centralized IT teams and SQL developers. Report turnarounds often took weeks or months.
  - *Modern Self-Service BI (Power BI):* Empowers Business Analysts and Data Analysts to clean data, model schemas, and build interactive dashboards via intuitive graphical interfaces without deep software engineering prerequisites.
- **Power BI vs. Advanced Excel vs. Tableau:**
  - *Excel:* Strictly limited to 1,048,576 rows per worksheet. Experiences significant degradation with complex formulas; lacks automated real-time cloud scheduled refresh.
  - *Tableau:* Highly capable visual analytics layer, but lacks native integrated ETL and relational modeling equivalent to Power BI's **Power Query + DAX** architecture.
  - *Power BI:* Compresses and queries hundreds of millions of rows via the in-memory VertiPaq engine, offers seamless native integration with Microsoft 365, and provides an exceptionally cost-effective enterprise pricing model.

---

## 📌 Topic 1.2: Power BI Architecture & Ecosystem

Power BI consists of five primary enterprise architectural components:
1. **Power BI Desktop (Free):** Windows authoring application used for data ingestion, ETL transformation (Power Query), data modeling, and DAX metric formulation.
2. **Power BI Service (Cloud SaaS):** Secure cloud collaboration portal (`app.powerbi.com`) for publishing reports, building executive dashboards, and managing access governance.
3. **Power BI Mobile App:** Native iOS and Android application delivering phone-optimized mobile layouts with real-time KPI alerts.
4. **Power BI Data Gateway:** Secure hybrid communication bridge synchronizing on-premises data sources (local SQL servers, internal spreadsheets) with the Power BI Cloud.
5. **Power BI Report Server:** On-premises hosting server tailored for organizations subject to strict regulatory or air-gapped data compliance requirements.

---

## 📌 Topic 1.3: Power BI Desktop Interface Walkthrough

When launching Power BI Desktop, the UI is organized into four major operational sections:

```
+-----------------------------------------------------------------------------------+
|  RIBBON: [File] [Home] [Insert] [Modeling] [View] [Optimize] [Help]               |
+-----+-------------------------------------------------------+---------------------+
| V   |                                                       | PANES:              |
| I   |                     CANVAS                            | 1. Filters Pane     |
| E   |                                                       | 2. Visualizations   |
| W   |             (Report Designing Area)                   |    (Bar, Line, etc) |
| S   |                                                       | 3. Data Pane        |
|     |                                                       |    (Tables & Fields)|
+-----+-------------------------------------------------------+---------------------+
| Pages: [Page 1 (+)] [Sales Summary]                         | Zoom: 100%          |
+-----------------------------------------------------------------------------------+
```

### Three Core Views (Left Navigation Sidebar):
1. **Report View (Bar-chart icon):** The primary canvas where charts, KPI cards, slicers, and interactive dashboard layouts are assembled.
2. **Table / Data View (Grid/Table icon):** Tabular data viewer to inspect cleaned datasets, verify data types, and review calculated column outputs.
3. **Model View (Relationship diagram icon):** Visual entity-relationship diagram (ERD) canvas where relationships (`1:*`, `*:1`) between Fact and Dimension tables are configured.

---

## 📌 Topic 1.4: Step-by-Step Data Ingestion (Connecting to Data)

We will now perform the practical workflow of importing **`sales_data_1000.csv`** into Power BI Desktop.

### 🧭 Navigation Guide Path:
`Ribbon > Home Tab > Data Group > Get Data > Text/CSV`

### 🛠️ Step-by-Step Execution:
1. **Step 1:** Launch Power BI Desktop. Dismiss the startup splash screen (`X`).
2. **Step 2:** Click the **Home Tab** in the top ribbon menu.
3. **Step 3:** Within the **Data** group, click the **Get Data** dropdown and select **Text/CSV** (or click the dedicated **Text/CSV** icon in the ribbon).
4. **Step 4:** In the file dialog, navigate to the target data location:
   ```
   d:\YSM Info Solution\Data Analytics &Cyber Security\python\Power BI\data\sales_data_1000.csv
   ```
   Select the file and click **Open**.
5. **Step 5 (Preview Dialog):** A preview dialog will display the first 200 rows of the dataset:
   - **File Origin:** `65001: Unicode (UTF-8)` (Retain default).
   - **Delimiter:** `Comma` (Retain default).
   - **Data Type Detection:** `Based on first 200 rows`.
6. **Step 6 (Crucial Selection):** Three action options are presented:
   - `Load`: Bypasses transformation and injects raw data directly into the model (Avoid this in production).
   - `Transform Data`: Opens the dataset in the **Power Query Editor** (⭐ **Recommended Best Practice!**).
   - `Cancel`: Aborts the ingestion workflow.
7. **Step 7:** Click **Transform Data** to launch the Power Query Editor.

---

## 📌 Topic 1.5: Connecting to Other Common Sources (Excel, Web, Folder)

Key ingestion patterns frequently tested in technical interviews:

### 1. Connecting to Excel Workbooks:
- **Path:** `Home Tab > Get Data > Excel Workbook`
- **Action:** Select the `.xlsx` file -> Select the target worksheet checkbox in the Navigator -> Click `Transform Data`.

### 2. Connecting to an Entire Directory / Folder (Automated File Consolidation):
- **Purpose:** Clients frequently provide periodic monthly transaction batches (`Jan.csv`, `Feb.csv`, etc.). Connecting directly to the directory dynamically appends all current and future incoming files.
- **Path:** `Home Tab > Get Data > More... > Folder > Connect`
- **Action:** Specify the directory path -> Click `Combine > Combine & Transform Data`.

### 3. Connecting to Web Data (Live HTML Web Scraping):
- **Path:** `Home Tab > Get Data > Web`
- **Action:** Provide the web endpoint URL (e.g., Wikipedia country population table) -> Select the target HTML table -> Click `Transform Data`.

---

## 📌 Topic 1.6: Storage Modes (Import Mode vs. DirectQuery vs. Dual Mode)

A fundamental technical architecture comparison in enterprise Power BI deployments:

| Feature | Import Mode (Default) | DirectQuery Mode | Dual / Composite Mode |
| :--- | :--- | :--- | :--- |
| **Storage Location** | Cached in local RAM using the columnar VertiPaq engine. | Remains stored directly within source database (SQL Server, Snowflake, BigQuery). | Hybrid combination (Dimensions cached in-memory, Facts queried live). |
| **Query Performance** | ⚡ **Extremely Fast** (Compressed in-memory columnar index). | ⏳ Dependent on network bandwidth and database hardware capability. | High-performance balanced execution. |
| **DAX Compatibility** | 100% of all DAX formulas and Time-Intelligence functions supported. | Certain advanced Time-Intelligence DAX formulas restricted. | Full DAX feature set supported. |
| **Dataset Capacity** | 1 GB per dataset (Pro license compressed); up to 400 GB in PPU/Fabric. | Virtually limitless (Billions of records). | Scalable enterprise architecture. |
| **Optimal Use Cases** | Standard business dashboards, CSV/Excel sources, high-speed reporting. | Real-time financial tickers, telemetry sensors, strict data-residency policies. | Massive enterprise reporting architectures. |

---

## 🎯 Practical Exercise for Students:
1. Launch Power BI Desktop.
2. Ingest `sales_data_1000.csv`, `customer_dim.csv`, and `product_dim.csv` sequentially.
3. Instead of clicking **Load**, select **Transform Data** for each to open the Power Query Editor.
4. Confirm that all three queries are visible in the left **Queries** navigation pane.
