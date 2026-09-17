# 🔍 Excel Formulas & Lookup Functions Master Guide

Lookup functions and conditional formulas form the core engine of Excel financial models, sales audits, and inventory reconciliation.

---

## 📌 1. XLOOKUP (The Modern Gold Standard)

Introduced in modern Excel (Office 365 / Excel 2021), `XLOOKUP` replaces `VLOOKUP`, `HLOOKUP`, and `INDEX-MATCH` with a safer, more intuitive syntax.

### Syntax Anatomy:
```excel
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
```

- **`lookup_value`**: What you are searching for (e.g., Employee ID `103`).
- **`lookup_array`**: Where to search for the ID (e.g., `Employees!A2:A50`).
- **`return_array`**: Which column to return values from (e.g., `Employees!E2:E50` for Salary).
- **`[if_not_found]`**: Value to return if no match is found (e.g., `"Not Found"`). No need for `IFNA` or `IFERROR` wrapper!
- **`[match_mode]`**: Defaults to `0` (Exact Match).
- **`[search_mode]`**: Defaults to `1` (Search first-to-last).

### Practical Example:
```excel
=XLOOKUP(A2, Employees!$A$2:$A$100, Employees!$D$2:$D$100, "Employee Not Found")
```

### XLOOKUP vs Legacy VLOOKUP:

| Feature | Legacy VLOOKUP | Modern XLOOKUP |
| :--- | :--- | :--- |
| **Match Mode Default** | Approximate (`TRUE`) - Causes errors if omitted! | Exact Match (`0`) - Safe by default |
| **Left Lookups** | ❌ Cannot look to the left of the lookup column | ✅ Can look left, right, up, or down |
| **Column Insertions** | ❌ Hardcoded column index breaks if columns are inserted | ✅ Dynamic cell ranges adapt automatically |
| **Missing Values** | Requires `=IFNA(VLOOKUP(...), "N/A")` | Built-in `[if_not_found]` argument |
| **Speed & Performance** | Slower on 500k+ rows | Significantly faster memory engine |

---

## 📌 2. INDEX - MATCH (The Powerhouse Combo)

`INDEX-MATCH` is the industry standard in companies still running legacy Excel versions.

### How it works:
1. `MATCH(lookup_value, lookup_array, 0)` finds the **row number** where the value resides.
2. `INDEX(array, row_num, [col_num])` retrieves the cell value from that specific row.

### Formula Structure:
```excel
=INDEX(Return_Range, MATCH(Lookup_Value, Lookup_Range, 0))
```

### Business Example: Finding Product Price by Product Code
```excel
=INDEX(Products!$D$2:$D$500, MATCH(B2, Products!$A$2:$A$500, 0))
```

---

## 📌 3. Logical Decisions: IF & IFS

### 1. Standard IF Statement
```excel
=IF(logical_test, value_if_true, value_if_false)
```
- **Example:** Check if sales exceed target:
  ```excel
  =IF(D2 >= 50000, "Bonus Eligible", "Standard")
  ```

### 2. Compound Logic with AND & OR
- **AND:** All conditions must be true:
  ```excel
  =IF(AND(D2 >= 50000, E2 >= 90), "Top Performer", "Standard")
  ```
- **OR:** At least one condition must be true:
  ```excel
  =IF(OR(F2="VIP", D2 > 100000), "Priority Support", "Standard Support")
  ```

### 3. Multi-Condition IFS (Clean Alternative to Nested IFs)
```excel
=IFS(
    D2 >= 100000, "Platinum",
    D2 >= 50000,  "Gold",
    D2 >= 20000,  "Silver",
    TRUE,         "Bronze"
)
```

---

## 📌 4. Conditional Business Aggregations: SUMIFS, COUNTIFS, AVERAGEIFS

Unlike `SUMIF` (which only supports 1 condition), `SUMIFS` allows analysts to filter by **unlimited simultaneous business conditions**.

### SUMIFS Syntax:
> **Important Rule:** In `SUMIFS`, the `sum_range` is always the **FIRST** argument!
```excel
=SUMIFS(sum_range, criteria_range1, criteria1, criteria_range2, criteria2, ...)
```

### Business Scenarios:

1. **Calculate Total Sales for "Electronics" in "Mumbai":**
   ```excel
   =SUMIFS(Sales!$E$2:$E$1000, Sales!$B$2:$B$1000, "Electronics", Sales!$C$2:$C$1000, "Mumbai")
   ```

2. **Calculate Sales for Deals Greater than Rs. 10,000 in Year 2026:**
   ```excel
   =SUMIFS(
       Sales!$E$2:$E$1000, 
       Sales!$E$2:$E$1000, ">10000", 
       Sales!$A$2:$A$1000, ">=2026-01-01", 
       Sales!$A$2:$A$1000, "<=2026-12-31"
   )
   ```

3. **Count Number of Repeat Transactions for Customer "CUST-901":**
   ```excel
   =COUNTIFS(Orders!$B$2:$B$1000, "CUST-901", Orders!$F$2:$F$1000, "Delivered")
   ```

4. **Calculate Average Order Value for "Online UPI" Orders:**
   ```excel
   =AVERAGEIFS(Orders!$E$2:$E$1000, Orders!$D$2:$D$1000, "UPI")
   ```
