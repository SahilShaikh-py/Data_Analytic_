# 📊 Microsoft Excel Masterclass: Data Analytics Lifecycle & Essentials

Welcome to the **Microsoft Excel Masterclass for Data Analysts**. In any enterprise organization, Excel remains the foundational spreadsheet tool for ad-hoc business analysis, financial audits, and quick executive summaries.

---

## 🎯 The 6 Stages of the Data Analytics Lifecycle

Before writing a single formula, every professional analyst follows the industry-standard **Analytics Lifecycle**:

```
[1. ASK] ➡️ [2. PREPARE] ➡️ [3. PROCESS] ➡️ [4. ANALYZE] ➡️ [5. SHARE] ➡️ [6. ACT]
```

1. **Ask (Define the Problem):** Understand the core business objective. *(Example: Why are sales declining in the West region during Q3?)*
2. **Prepare (Data Collection):** Identify data sources (CRM, ERP, SQL databases, CSV flat files) and verify data storage integrity.
3. **Process (Data Cleaning):** Fix incorrect data types, eliminate duplicate rows, remove extra whitespace, and handle missing values.
4. **Analyze (Exploration & Calculations):** Use formulas, lookup functions, pivot tables, and statistical summaries to discover trends.
5. **Share (Visualization & Storytelling):** Build charts, 1-page interactive dashboards, and executive slide summaries.
6. **Act (Data-Driven Decisions):** Present actionable recommendations to leadership to optimize operations and drive revenue.

---

## 📌 Topic 1: Sorting & Filtering in Excel

### 1. Multi-Level Custom Sorting
Standard A-to-Z sorting is often insufficient for business data. Multi-level sorting arranges data hierarchically.
- **Path:** Select Data ➡️ `Data` Tab ➡️ `Sort`
- **Business Example:**
  - **Level 1 (Sort by):** `Region` (A to Z)
  - **Level 2 (Then by):** `Department` (A to Z)
  - **Level 3 (Then by):** `Net Sales` (Largest to Smallest)
- **Shortcut:** `ALT + D + S` (Windows)

### 2. Advanced Filtering
- **Keyboard Shortcut:** `CTRL + SHIFT + L` (Toggles filter dropdowns on/off instantly).
- **Text Filters:**
  - *Contains:* Find all product names containing `"Wireless"`
  - *Begins With:* Find all customer IDs starting with `"VIP-"`
- **Number Filters:**
  - *Top 10 / Above Average:* Identify highest performing sales reps.
  - *Between:* Transactions between `Rs. 5,000` and `Rs. 25,000`.

---

## 📌 Topic 2: Conditional Formatting

Conditional formatting automatically applies colors, icons, and data bars to cells based on business thresholds, allowing stakeholders to spot anomalies at a glance.

### 1. Highlight Cells Rules & Top/Bottom Rules
- **Greater Than:** Format deals `> Rs. 50,000` with soft green fill.
- **Less Than:** Format customer satisfaction scores `< 70%` with soft red fill.
- **Top 10%:** Automatically highlights the top 10th percentile of revenue drivers.

### 2. Visual Enhancements (Data Bars & Color Scales)
- **Data Bars:** Embeds mini horizontal bar charts inside cells representing relative values.
- **Color Scales (Heatmaps):** 3-Color gradient (Green = High, Yellow = Mid, Red = Low) for regional sales heatmaps.

### 3. Custom Formula Formatting
To format an entire row based on the value of a specific cell:
1. Select the entire table (e.g., `A2:G100`).
2. Navigate to `Home` ➡️ `Conditional Formatting` ➡️ `New Rule` ➡️ `Use a formula to determine which cells to format`.
3. Formula: `=$E2="Pending"` (Note the dollar sign before column `E` locks the column evaluation across the entire row).
4. Select a light yellow highlight fill.

---

## 📌 Topic 3: Data Validation (Drop-Down Lists)

Dirty data is often caused by manual typos (e.g., `"Mumbaai"`, `"mumbai"`, `"MUMBAI"` entered in the same column). Data Validation enforces strict entry control.

### How to Create a Drop-Down List:
1. Select the target range of cells (e.g., `Department` column `C2:C50`).
2. Go to `Data` Tab ➡️ `Data Validation` (Shortcut: `ALT + A + V + V`).
3. Under **Allow**, select **List**.
4. In **Source**, enter comma-separated values:
   ```text
   IT, Finance, HR, Marketing, Operations, Sales
   ```
   *Best Practice:* Place the lookup categories in a separate reference sheet and select the range (e.g., `=Lists!$A$2:$A$7`).
5. Configure the **Error Alert** tab:
   - *Title:* `"Invalid Department"`
   - *Error Message:* `"Please choose a valid department from the drop-down menu."`

---

## 📂 Included Practice Materials in this Folder

- **`formulas_and_lookups_guide.md`**: Complete deep-dive into XLOOKUP, VLOOKUP, INDEX-MATCH, IF, and SUMIFS.
- **`pivot_tables_and_dashboards_guide.md`**: Interactive dashboard design blueprint.
- **`create_excel_practice_workbooks.py`**: Automated script that generates practice `.xlsx` spreadsheets for students.
