# 🎯 Capstone Executive Presentation Deck (Portfolio & Interview Template)
## Project: AuraKart Customer Retention & Revenue Optimization Analytics

> **Student Guide:** Use this structured slide deck outline during portfolio walkthroughs and technical interviews. It tells a compelling end-to-end data story following the STAR method (Situation, Task, Action, Result).

---

## 📽️ Slide 1: Executive Title & Summary

- **Title:** AuraKart Omni-Channel Customer Retention & Margin Optimization
- **Presenter:** [Your Name] | Data Analyst & BI Consultant
- **Tools Leveraged:** Python (Pandas, NumPy), SQLite / MySQL, Microsoft Excel, Microsoft Power BI
- **Executive Summary:** Analyzed 600+ multi-category transactions across 10 metropolitan markets. Uncovered that while overall gross revenue reached Rs. 4.5M+, aggressive 15% promotional discounting eroded margins in low-ticket categories by 8.4%. Designed an automated ETL pipeline and interactive Power BI executive dashboard to empower leadership with real-time KPI visibility.

---

## 📽️ Slide 2: Business Problem & Discovery (The "Why")

- **The Client Situation:** AuraKart observed surging top-line revenue but stagnation in net profitability and a 14% drop in customer repeat purchase frequency.
- **Key Discovery Questions:**
  1. *Are marketing discounts driving profitable customer cohorts or subsidizing one-time deal seekers?*
  2. *Which acquisition channels (Google Ads vs Organic vs Instagram) yield the highest Customer Lifetime Value (CLV)?*
  3. *Which operational hubs suffer from high return and cancellation rates?*

---

## 📽️ Slide 3: Technical Pipeline & Data Architecture

```
[Raw CSV / Ingestion] ──▶ [Python Sanitization] ──▶ [SQL Data Warehouse] ──▶ [Power BI Dashboard]
  • 600 Dirty Rows         • Dropped Negatives      • Star Schema             • Executive KPI Cards
  • Missing Keys           • Type Coercion          • Fact & Dim Tables       • Interactive Slicers
  • Inconsistent Dates     • Margin Feature Eng.    • Analytical Views        • DAX Measures
```

- **Python ETL Script:** [`capstone_etl_pipeline.py`](file:///d:/YSM%20Info%20Solution/Data%20Analytics%20&Cyber%20Security/python/04_Industry_Capstone_Project/capstone_etl_pipeline.py)
- **Database Schema:** 1 Fact Table (`fact_orders`), 2 Dimension Tables (`dim_customers`, `dim_products`).

---

## 📽️ Slide 4: Key Insights & Financial Findings

1. **Category Profitability Drivers:**
   - *Electronics & Apparel* generated over 62% of net profit, maintaining a healthy gross margin of ~46%.
   - *Grocery* generated steady recurring transaction frequency (basket size), but heavy discounting reduced gross margins to 28%.
2. **Channel Acquisition Disparity:**
   - *Direct App* and *Organic Search* exhibited the lowest return rates (under 2%) and highest CLV (Rs. 480k+ avg spend).
   - *Instagram Ads* had a higher cancellation rate (6.2%), indicating impulsive, uncommitted purchases.
3. **Regional Market Concentration:**
   - Mumbai, Delhi, and Bangalore contributed 71% of total enterprise volume.

---

## 📽️ Slide 5: Power BI Executive Dashboard Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│  📊 AURAKART C-SUITE EXECUTIVE PERFORMANCE DASHBOARD           [2026]  │
├────────────────────────────────────────────────────────────────────────┤
│  [NET REVENUE]       [GROSS PROFIT]       [MARGIN %]     [ACTIVE USERS]│
│   Rs. 4.52M             Rs. 1.81M           40.16%             10      │
├───────────────────────────────────┬────────────────────────────────────┤
│  [SLICERS & FILTERS]              │  [CHART 1: Monthly Revenue Trend]  │
│  • Market Tier: [Tier-1] [Tier-2] │  Area chart showing steady growth  │
│  • Category: [All] [Electronics]  │  from Jan to June 2026             │
├───────────────────────────────────┼────────────────────────────────────┤
│  [CHART 2: Category Margins]      │  [CHART 3: Regional Hub Matrix]    │
│  Clustered Bar Chart:             │  Matrix visual with conditional    │
│  Sales vs Profit per Category     │  formatting heatmaps               │
└───────────────────────────────────┴────────────────────────────────────┘
```

---

## 📽️ Slide 6: Strategic Recommendations & Action Plan

1. **Cap Promotional Discounts:** Eliminate blanket 15% discounts on low-margin Grocery SKUs; shift toward minimum basket thresholds (e.g., *"Free shipping on orders over Rs. 999"*).
2. **Launch VIP Concierge Program:** The top 3 customers generate 42% of total company profit. Provide dedicated account perks and early product access.
3. **Optimize Channel Spend:** Reallocate 20% of Instagram ad budget toward Google Search and Referral loyalty rewards to attract higher-intent buyers.

---

## 💡 How to Explain this Project in an Interview (Talking Script)

> *"In my AuraKart Capstone project, I led an end-to-end data analytics engagement addressing declining customer repeat purchases. I first used Python to automate the ETL pipeline—cleaning dirty transactions, handling missing attributes, and calculating financial metrics like Net Revenue and COGS. Next, I structured the data into a Star Schema within an SQLite relational warehouse, writing advanced SQL queries to analyze customer cohorts and channel ROI. Finally, I visualized these findings in an interactive Power BI Executive Dashboard with DAX measures and slicers. Our analysis recommended capping low-margin promotional discounts and reallocating ad spend toward high-CLV organic and referral channels, projecting an estimated 4.2% margin recovery."*
