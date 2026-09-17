# 🏆 End-to-End Industry Capstone Project
## Project Title: Omni-Channel E-Commerce Customer Retention & Revenue Optimization Pipeline

This Capstone simulates an enterprise consulting engagement. It consolidates everything learned across **Python, SQL, Excel, and Power BI** into a complete portfolio-ready project for students' resumes and technical interviews.

---

## 📌 Business Problem Statement

**Client:** *AuraKart*, a rapid-delivery Indian omni-channel retail brand.  
**Situation:** While overall transaction volumes grew by 28% year-over-year, customer repeat purchase rates declined by 14%, and marketing acquisition spend surged.  
**Leadership Questions:**
1. What is the true Customer Lifetime Value (CLV) across different customer tiers and regional hubs?
2. Which product categories drive healthy gross margins vs. which ones are subsidized by unprofitable discounts?
3. Which customer cohorts are churning after their first order, and what early indicators predict churn?
4. How can executive leadership track live revenue, margin, and order fulfillment KPIs through a centralized dashboard?

---

## 🔄 End-to-End Enterprise Architecture

```
[Raw Dirty Ingestion] ──▶ [Python Automated ETL Pipeline] ──▶ [SQLite / MySQL Warehouse]
  (CSV / JSON Files)        - Deduplication & Null Imputation    - Star Schema Relational Tables
                            - Financial Metric Calculation       - Fast SQL Analytical Views
                                                                          ⬇️
[Executive Presentation] ◀── [Power BI Executive Dashboard] ◀─────────────┘
  - Portfolio Storytelling     - Executive KPI Cards & Slicers
  - Actionable Strategy        - DAX Measures (Margin %, MoM Growth)
```

---

## 📂 Project Assets & Deliverables

| File | Purpose |
| :--- | :--- |
| **`capstone_etl_pipeline.py`** | Production Python script that generates raw transactional data, cleans anomalies, engineer features, and exports clean tables directly into a database warehouse. |
| **`capstone_sql_queries.sql`** | Enterprise SQL queries computing Cohort Retention rates, Regional margins, and High-value repeat client segments. |
| **`Capstone_Executive_Presentation_Deck.md`** | Complete executive slide-deck structure and presentation script for data analyst portfolio interviews. |
