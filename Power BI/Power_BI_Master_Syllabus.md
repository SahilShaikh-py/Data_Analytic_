# 📊 Complete Power BI Master Syllabus (Beginner to Advanced)
### 🎯 Course Title: Power BI for Data Analytics & Business Intelligence (Zero to Hero)
**Target Audience:** Students, Aspiring Data Analysts, Working Professionals  
**Mode:** Practical, Hands-on, Project-Driven  
**Tools Covered:** Power BI Desktop, Power Query (M Language), DAX, Power BI Service (Cloud), DAX Studio  

---

## 📌 Course Roadmap Overview

```
[Module 1: BI Basics & Setup] ➡️ [Module 2: Power Query / ETL] ➡️ [Module 3: Data Modeling & Schema]
                                                                        ⬇️
[Module 6: Advanced Analytics & AI] ⬅️ [Module 5: Visuals & UX Design] ⬅️ [Module 4: DAX Mastery]
       ⬇️
[Module 7: Power BI Service & Cloud] ➡️ [Module 8: Performance Tuning] ➡️ [Module 9: Capstone Projects & PL-300]
```

---

## 📑 Detailed Module-by-Module Syllabus

---

### 🔹 Module 1: Introduction to Business Intelligence & Power BI Basics
**Objective:** Master core BI concepts, explore the Power BI ecosystem, and build your first interactive report.

- **1.1 Business Intelligence (BI) Fundamentals:**
  - What is BI and its strategic role in business decision-making.
  - Traditional BI vs. Modern Self-Service BI.
  - Detailed tool comparison: Power BI vs. Tableau vs. Advanced Excel.
- **1.2 Power BI Architecture & Ecosystem:**
  - Power BI Desktop (Free authoring tool).
  - Power BI Service (Cloud SaaS for sharing, governance & collaboration).
  - Power BI Mobile & Power BI Report Server.
  - Power BI Gateway (Secure hybrid data refresh link).
- **1.3 Power BI Desktop Interface Walkthrough:**
  - Ribbon, Canvas, Report Pages.
  - Three Core Views: **Report View**, **Table/Data View**, **Model View**.
  - Fields Pane, Visualizations Pane, and Filters Pane.
- **1.4 Data Ingestion (Connecting to Data Sources):**
  - Connecting to Flat Files: Excel (`.xlsx`), CSV (`.csv`), Text (`.txt`).
  - Connecting to Web Data (Web Scraping via URL).
  - Connecting to SQL Database (Concepts & Live Demo).
  - Connecting to a Folder (Automated consolidation of monthly transaction files).
- **1.5 Data Storage Modes:**
  - **Import Mode** (In-Memory VertiPaq engine - ultra fast performance).
  - **DirectQuery Mode** (Live querying against external databases).
  - **Dual Mode / Composite Models**.
- 🛠️ **Hands-on Lab:** Ingest Excel sales data, create 2 standard charts and 1 KPI card visual, and publish an initial report preview.

---

### 🔹 Module 2: Data Cleaning & Transformation (Power Query / ETL Masterclass)
**Objective:** Transform dirty, unorganized raw data into clean, structured, and analytics-ready datasets using Power Query.

- **2.1 Introduction to ETL (Extract, Transform, Load):**
  - Data profiling: Column Distribution, Column Quality, and Column Profile.
  - Understanding Applied Steps and the undo workflow.
- **2.2 Basic Data Cleaning Operations:**
  - Data Type configuration and detection.
  - Handling Missing / Null / Blank values (`Replace Values`, `Remove Empty`).
  - Removing Errors and Duplicates (`Remove Duplicates`, `Keep Duplicates`).
  - Promoting Headers (`Use First Row as Headers`).
  - Filtering Rows and Sorting Data.
- **2.3 Text, Number & Date Transformations:**
  - **Text:** Split Column (by delimiter, by character count), Trim, Clean, Upper/Lower/Capitalize, Extract length.
  - **Numbers:** Rounding, Standard arithmetic, Even/Odd evaluation.
  - **Dates:** Extracting Year, Month, Day, Quarter, Day Name, Week of Year, Age calculation.
- **2.4 Advanced Table Operations (Crucial Technical Interview Topics):**
  - **Merge Queries (Joins):**
    - Inner Join, Left Outer Join, Right Outer Join, Full Outer Join, Left Anti, Right Anti.
    - Fuzzy Matching (Handling misspelled names/product variants).
  - **Append Queries (Unions):**
    - Combining multiple tables with identical or heterogeneous schemas.
  - **Pivot vs. Unpivot Columns:**
    - Transforming Wide tabular format into Long (Normalized) format (Essential interview skill).
  - **Group By (Aggregations):**
    - Aggregating categorical rows with Sum, Count, and Average directly in ETL.
- **2.5 Custom & Conditional Logic:**
  - **Conditional Columns:** IF-ELSE logic configured without coding.
  - **Column From Examples:** Pattern recognition powered by AI.
  - **Custom Columns:** Formulating basic M-Code expressions.
  - Introduction to the **Advanced Editor** (Reading and editing M Language code).
- 🛠️ **Hands-on Lab:** Clean a raw e-commerce transaction dataset, append 12 monthly transaction logs, and unpivot matrix data into a clean relational model.

---

### 🔹 Module 3: Data Modeling & Relationships (The Engine of Power BI)
**Objective:** Design robust relational data architectures ensuring precise filtering and performant calculations.

- **3.1 Relational Data Concepts:**
  - Primary Key vs. Foreign Key.
  - **Fact Tables** (Transactions, Sales orders, Logs - Metrics and numerical values).
  - **Dimension Tables** (Lookup attributes - Customers, Products, Regions, Dates).
- **3.2 Database Schemas:**
  - **Star Schema** (Industry-standard best practice for Power BI query performance).
  - **Snowflake Schema** (Normalized dimension hierarchies - trade-offs and usage).
  - Flat Table vs. Star Schema performance benchmarks.
- **3.3 Managing Relationships:**
  - **Cardinality:**
    - One-to-Many (`1:*`) [Most common and strongly recommended].
    - Many-to-One (`*:1`).
    - One-to-One (`1:1`).
    - Many-to-Many (`*:*`) [Handling risks via Bridge Tables and Cross Join strategies].
  - **Cross Filter Direction:**
    - Single Direction vs. Both Directions (Dangers of ambiguous paths with Bi-directional filtering).
- **3.4 Inactive vs. Active Relationships:**
  - Modeling role-playing dates (Order Date, Ship Date, Delivery Date).
  - Programmatic activation using `USERELATIONSHIP()` in DAX.
- **3.5 Creating a Dedicated Date / Calendar Dimension Table:**
  - Why a Date Dimension is mandatory for robust Time Intelligence.
  - Building Calendar tables via Power Query vs. DAX (`CALENDAR()`, `CALENDARAUTO()`).
  - Marking as an Official Date Table.
- 🛠️ **Hands-on Lab:** Construct an end-to-end Star Schema relational model connecting Sales, Product, Customer, Geography, and Calendar dimensions.

---

### 🔹 Module 4: DAX Mastery (Data Analysis Expressions) - Beginner to Advanced
**Objective:** Formulate advanced business metrics and complex business KPIs using production-grade DAX.

- **4.1 DAX Fundamentals:**
  - DAX Syntax, Data Types, and Operators.
  - **Calculated Columns vs. Measures (Critical Distinction):**
    - RAM vs. CPU overhead, Row storage vs. Dynamic calculation.
    - Measure Tables (Best practice: Centralized measures table).
- **4.2 Evaluation Contexts (The Core of DAX):**
  - **Row Context:** Row-by-row iteration (Calculated columns and `X` iterator functions).
  - **Filter Context:** Dynamic filtering driven by visual coordinates, slicers, and filter panes.
  - **Context Transition:** Converting Row Context into Filter Context via `CALCULATE()`.
- **4.3 Standard & Statistical DAX Functions:**
  - `SUM()`, `AVERAGE()`, `MIN()`, `MAX()`, `COUNT()`, `COUNTA()`, `DISTINCTCOUNT()`.
  - `DIVIDE()` (Safe division with built-in zero division handling).
- **4.4 Logical & Text Functions:**
  - `IF()`, `SWITCH()` (Replacing nested IF statements for scalable status mapping).
  - `AND()`, `OR()`, `NOT()`, `COALESCE()`.
  - `CONCATENATE()`, `FORMAT()`, `LEFT()`, `RIGHT()`.
- **4.5 The Core of DAX: `CALCULATE()` & Filter Modifiers:**
  - `CALCULATE(Expression, Filter1, Filter2...)`.
  - Filter Overriding using `ALL()` (Calculating Grand Totals ignoring external filters).
  - `ALLEXCEPT()` (Percentage of Category Sales).
  - `ALLSELECTED()` (Visual-level dynamic proportions respecting slicer state).
  - `KEEPFILTERS()` & `REMOVEFILTERS()`.
- **4.6 Iterative Functions (X-Functions):**
  - `SUMX()`, `AVERAGEX()`, `MINX()`, `MAXX()`.
  - `RANKX()` (Dynamic rankings for customers and products).
  - `CONCATENATEX()` (Concatenating values into a delimited string).
- **4.7 Time Intelligence DAX (Business Reporting Core):**
  - Year-to-Date (`TOTALYTD`), Quarter-to-Date (`TOTALQTD`), Month-to-Date (`TOTALMTD`).
  - Historical Period Analysis: `SAMEPERIODLASTYEAR()`, `DATEADD()`, `PARALLELPERIOD()`.
  - Calculating **YoY (Year-over-Year) Growth %** and **MoM (Month-over-Month) Growth %**.
  - Moving Averages (Rolling 3-month and 30-day moving windows).
- **4.8 Advanced DAX Concepts:**
  - Utilizing `VAR` and `RETURN` for code clarity and execution caching.
  - Virtual Tables in DAX: `SUMMARIZE()`, `ADDCOLUMNS()`, `VALUES()`, `DISTINCT()`, `TOPN()`.
  - Dynamic Metrics via **Field Parameters** (Interactive measure switchers).
- 🛠️ **Hands-on Lab:** Author 25+ business measures (Total Revenue, Margin %, Target vs. Actual, YoY Growth %, and Dynamic Customer Rankings).

---

### 🔹 Module 5: Data Visualization & Executive Dashboard Designing (UI/UX)
**Objective:** Design executive-level, visually compelling dashboards optimized for user experience and rapid decision-making.

- **5.1 Core Visual Types & Selection Criteria:**
  - Comparison: Clustered vs. Stacked Column/Bar Charts.
  - Temporal Trends: Line Charts, Area Charts.
  - Part-to-Whole: Donut Charts, Treemaps, Waterfall Charts.
  - Distribution: Scatter Plots, Box & Whisker Charts.
  - Tabular: Tables vs. Matrix (Subtotals, Grand totals, Stepped layout).
- **5.2 Modern KPI Cards & Gauges:**
  - Single Value Card vs. Multi-Row Card vs. **New KPI Card Visual (Modern Features)**.
  - Sparklines embedded within table and matrix visuals.
- **5.3 Conditional Formatting (Data Highlighting):**
  - Rule-based background and font coloring.
  - Data Bars and KPI Status Icons (Green/Yellow/Red status indicators).
- **5.4 Slicers & Interactive Filtering:**
  - Date Hierarchy Slicers (Between, Relative Date filtering: Last 30 Days).
  - Dropdown, Tile, and Hierarchy Slicer styles.
  - Sync Slicers (Controlling multiple canvas pages from a single slicer).
  - Edit Interactions (Cross-filtering vs. Highlighting vs. None).
- **5.5 Advanced Interactivity & Visual Storytelling:**
  - **Drill-Down & Drill-Up** (Year -> Quarter -> Month -> Day).
  - **Drill-Through Pages** (Navigating from executive summaries to detailed entity sheets).
  - **Custom Tooltip Pages** (Displaying contextual micro-visuals on hover).
  - **Bookmarks & Selection Pane:**
    - Toggling between Chart and Matrix views.
    - Implementing a Collapsible Filter Sidebar (Slide-out menu).
    - Implementing a "Reset All Filters" action button.
- **5.6 Dashboard UI/UX Design System:**
  - Grid alignment, padding, visual hierarchy, and negative space.
  - Harmonious Color Theory (Corporate palettes, 60-30-10 rule).
  - Canvas scaling, Phone layout view formatting.
- 🛠️ **Hands-on Lab:** Build an Executive Sales & Profitability Dashboard featuring custom tooltips, bookmark-driven navigation, and dynamic KPI threshold alerts.

---

### 🔹 Module 6: Advanced Analytics & AI Features in Power BI
**Objective:** Leverage built-in artificial intelligence and machine learning visual capabilities in Power BI.

- **6.1 Built-in AI Visuals:**
  - **Q&A Visual:** Natural Language Processing (NLP) queries generating instant charts.
  - **Key Influencers Visual:** Determining key drivers and correlations for business metrics.
  - **Decomposition Tree:** Multi-dimensional root-cause breakdown visual.
  - **Smart Narrative:** Automated natural language text summaries of report data.
- **6.2 Predictive & Trend Analysis:**
  - Time-series Forecasting in Line Charts (Seasonality, confidence bands).
  - Analytics Pane: Trend Lines, Constant Lines, Min/Max/Average benchmarks.
  - Anomaly Detection (Pinpointing abnormal spikes or sudden troughs).
- **6.3 Python & R Integration:**
  - Executing Python scripts within Power Query for transformation.
  - Rendering custom Matplotlib and Seaborn figures directly on the report canvas.
- 🛠️ **Hands-on Lab:** Construct a Customer Churn Root-Cause Analysis report using Decomposition Tree and Key Influencers visuals.

---

### 🔹 Module 7: Power BI Service (Cloud Collaboration & Governance)
**Objective:** Deploy reports to the cloud, automate scheduled data refreshes, and distribute enterprise dashboards securely.

- **7.1 Power BI Service Overview & Licensing:**
  - Free vs. Pro vs. Premium Per User (PPU) vs. Premium Capacity / Fabric.
  - Workspaces: Personal Workspaces vs. Collaborative App Workspaces.
- **7.2 Publishing & Cloud Asset Management:**
  - Publishing `.pbix` reports from Desktop to Service.
  - Semantic Models (Datasets) vs. Reports vs. Executive Dashboards.
  - Pinning visual tiles, Web content, and Image widgets.
- **7.3 Data Gateways & Automated Refresh:**
  - On-premises Data Gateway (Personal mode vs. Standard enterprise mode).
  - Configuring Scheduled Refresh (Automated daily/hourly sync with local Excel or on-prem SQL databases).
- **7.4 Security - Row Level Security (RLS):**
  - **Static RLS:** Role definitions based on static department or regional criteria.
  - **Dynamic RLS:** Utilizing `USERPRINCIPALNAME()` mapped to security lookup tables.
  - Role validation and testing within Desktop and Service.
- **7.5 Distribution & Enterprise Collaboration:**
  - Packaging and publishing Power BI Apps.
  - Link sharing, permission tiers, and access control.
  - Email Subscriptions and Data-Driven Alerts (Teams / Outlook alerts on KPI triggers).
  - Exporting to PowerPoint, PDF, and Excel (Analyze in Excel).
- 🛠️ **Hands-on Lab:** Deploy a dashboard to Power BI Service, configure Dynamic RLS, establish scheduled gateway refresh, and publish an App.

---

### 🔹 Module 8: Performance Optimization & Best Practices
**Objective:** Optimize data models and DAX calculations to create fast, scalable, and memory-efficient enterprise reports.

- **8.1 Performance Analyzer:**
  - Measuring visual display duration, DAX query execution time, and DirectQuery overhead.
- **8.2 Data Model Optimization:**
  - VertiPaq Engine fundamentals (Columnar compression algorithms).
  - Minimizing high-cardinality columns (Stripping timestamps from date fields).
  - Enforcing Star Schema best practices and eliminating redundant relationship chains.
- **8.3 DAX Optimization:**
  - Overview of Tabular Editor and DAX Studio.
  - Eliminating `CALCULATE` within iterative rows.
  - Using Variables (`VAR`) to eliminate duplicate measure recalculations.
- 🛠️ **Hands-on Lab:** Benchmark a slow report using Performance Analyzer, identify calculation bottlenecks, and optimize the underlying DAX and model schema.

---

## 🏆 Module 9: Real-World Industry Capstone Projects (Portfolio Ready)

Four comprehensive end-to-end industry projects designed to build an impressive professional portfolio:

| Project # | Project Title | Industry Domain | Key Skills Applied |
| :--- | :--- | :--- | :--- |
| **Project 1** | **E-Commerce Global Sales & Profitability Analyzer** | Retail / E-commerce | ETL, Star Schema, Core DAX, Slicers, Bookmarks, Mobile Layout |
| **Project 2** | **HR Workforce Analytics & Employee Attrition** | Human Resources | Demographic Analysis, Attrition Rate %, Key Influencers AI visual |
| **Project 3** | **CFO Executive Financial Performance & P&L Report** | Finance / Banking | Complex Matrix, YoY %, MoM %, Variance Analysis, Custom Tooltips |
| **Project 4** | **Cybersecurity Threat & Incident Monitoring Dashboard** *(Institute Special)* | Cybersecurity / IT | Log Analysis, Severity Matrix, Mean Time to Detect (MTTD), Geo-Map IP tracking |

---

## 🎓 Module 10: Career Preparation & Microsoft PL-300 Certification Guide

- **Microsoft Certified: Power BI Data Analyst (PL-300) Exam Blueprint:**
  - Prepare the data (25–30%)
  - Model the data (25–30%)
  - Visualize and analyze the data (25–30%)
  - Deploy and maintain assets (15–20%)
- **Top 50 Power BI Technical Interview Questions & Answers:**
  - Distinctions between `CALCULATE` and `FILTER`.
  - Concrete examples of Row Context vs. Filter Context.
  - Resolving Many-to-Many relationships effectively.
  - Incremental Refresh implementation vs. DirectQuery and Import modes.
- **Portfolio & Resume Development:**
  - Publishing interactive reports to **NovyPro** and **GitHub**.
  - Writing high-impact, metric-driven resume achievement statements.

---

## 🗓️ Recommended Course Duration & Schedule

- **Total Duration:** 6 to 8 Weeks (approx. 50–60 Hours)
- **Weekly Schedule:**
  - **Week 1:** Module 1 (BI Intro & Desktop) + Module 2 (Power Query ETL Part 1)
  - **Week 2:** Module 2 (Power Query Advanced ETL) + Module 3 (Data Modeling & Star Schema)
  - **Week 3:** Module 4 (DAX Fundamentals to `CALCULATE`, Contexts & Iterators)
  - **Week 4:** Module 4 (Time Intelligence DAX & Advanced DAX) + Project 1 (Sales Dashboard)
  - **Week 5:** Module 5 (Visualizations, UX, Bookmarks, Tooltips) + Project 2 (HR Analytics)
  - **Week 6:** Module 6 (AI Visuals) + Module 7 (Power BI Service, RLS, Cloud Refresh)
  - **Week 7:** Module 8 (Performance Optimization) + Project 3 (Financial P&L Dashboard)
  - **Week 8:** Project 4 (Cybersecurity Incident Dashboard) + PL-300 Exam Prep & Mock Interviews

---
*(Created for YSM Info Solution - Data Analytics & Cybersecurity Training Program)*
