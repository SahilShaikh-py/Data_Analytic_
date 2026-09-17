"""
=============================================================================
TOPIC: EXCEL AUTOMATION & DATA SCIENCE PIPELINE WITH PANDAS (ExcepPandas.py)
=============================================================================
Author: Python Mastery Course
Objective: Master reading, cleaning, manipulating, and applying Data Science 
           techniques on Excel spreadsheets using Pandas.

Kyu use karte hain Pandas with Excel?
------------------------------------
1. Excel manual hota hai aur large files (1M+ rows) pe hang ho jata hai.
2. Pandas me aap VLOOKUP, XLOOKUP, Pivot Tables, aur IF-ELSE formulas ko
   Python ke clean aur fast code se automate kar sakte hain.
3. Excel data ko directly Machine Learning pipelines (Encoding, Scaling, 
   Outlier Detection) ke liye taiyar kiya ja sakta hai.

Spreadsheet Source: 'employees_data.xlsx'
- Sheet 1: 'Employees' (Core employee details with missing values)
- Sheet 2: 'Projects'  (Relational table mapping projects to Emp_IDs)
=============================================================================
"""

import os
import pandas as pd
import numpy as np

# Terminal display settings for clean tabular formatting
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1000)

EXCEL_FILE = "employees_data.xlsx"

# =============================================================================
# PART 1: READING EXCEL FILES & MULTI-SHEET INSPECTION
# =============================================================================
print("=" * 70)
print(">>> PART 1: READING EXCEL FILE & MULTI-SHEET LOADING <<<")
print("=" * 70)

# Excel workbook ke andar saare sheet names check karna
excel_reader = pd.ExcelFile(EXCEL_FILE)
print(f"• Sheets found in '{EXCEL_FILE}': {excel_reader.sheet_names}")

# Sheet 1: 'Employees' load karna (Excel ke empty cells automatically NaN ban jaate hain)
df = pd.read_excel(EXCEL_FILE, sheet_name="Employees")
print("\n• Successfully Loaded 'Employees' Sheet:")
print(df)


# =============================================================================
# PART 2: DATA INSPECTION & SUMMARY (EXCEL HEALTH CHECK)
# =============================================================================
print("\n" + "=" * 70)
print(">>> PART 2: EXCEL DATA INSPECTION & STATISTICAL SUMMARY <<<")
print("=" * 70)

# 1. head(3): Top 3 rows preview
print("• Top 3 Rows (df.head(3)):")
print(df.head(3))

# 2. shape: Total rows and columns in Excel sheet
print(f"\n• Dimensions (Rows, Columns): {df.shape}")

# 3. dtypes: Excel columns ke detected data types
print("\n• Column Data Types:")
print(df.dtypes)

# 4. describe(): Summary statistics for numerical columns
print("\n• Statistical Summary (df.describe()):")
print(df.describe())


# =============================================================================
# PART 3: DATA SELECTION (.loc VS .iloc)
# =============================================================================
print("\n" + "=" * 70)
print(">>> PART 3: DATA SELECTION (.loc VS .iloc) <<<")
print("=" * 70)

# .iloc: Integer-based indexing (Row 0 se 2, Columns 1, 2, 4 -> Name, Department, Salary)
print("• Using .iloc[0:3, [1, 2, 4]] (Zero-based Indexing):")
print(df.iloc[0:3, [1, 2, 4]])

# .loc: Label-based indexing (Actual Column names ke zariye)
print("\n• Using .loc[0:2, ['Name', 'Department', 'Salary']] (Column Labels):")
print(df.loc[0:2, ['Name', 'Department', 'Salary']])


# =============================================================================
# PART 4: FILTERING & CONDITIONAL QUERIES (EXCEL AUTOFILTER ALTERNATIVE)
# =============================================================================
print("\n" + "=" * 70)
print(">>> PART 4: FILTERING & COMPOUND QUERIES <<<")
print("=" * 70)

# 1. Single Filter: Sirf IT department ke employees
it_employees = df[df["Department"] == "IT"]
print("• Filter: IT Department Employees:")
print(it_employees[["Emp_ID", "Name", "Salary"]])

# 2. Compound Filter: Salary > 70,000 AND Experience >= 5 years
senior_high_earners = df[(df["Salary"] > 70000) & (df["Experience_Yrs"] >= 5)]
print("\n• Compound Filter (Salary > 70k & Experience >= 5 Yrs):")
print(senior_high_earners[["Name", "Department", "Salary", "Experience_Yrs"]])


# =============================================================================
# PART 5: COLUMN OPERATIONS & VECTORIZED FORMULAS
# =============================================================================
print("\n" + "=" * 70)
print(">>> PART 5: COLUMN OPERATIONS (EXCEL FORMULAS IN PYTHON) <<<")
print("=" * 70)

# Excel Formula `=E2 * 0.10` ki jagah vectorized Pandas operation
df["Bonus"] = df["Salary"] * 0.10

# Excel Formula `=E2 + H2` (Total Compensation = Salary + Bonus)
df["Total_Compensation"] = df["Salary"] + df["Bonus"]

# Column rename karna (clean naming convention)
df.rename(columns={"Name": "Employee_Name"}, inplace=True)

print("• DataFrame after adding Bonus and Total_Compensation:")
print(df[["Employee_Name", "Department", "Salary", "Bonus", "Total_Compensation"]])


# =============================================================================
# PART 6: HANDLING MISSING VALUES (EXCEL BLANK CELLS CLEANING)
# =============================================================================
print("\n" + "=" * 70)
print(">>> PART 6: MISSING VALUES HANDLING (DATA CLEANING) <<<")
print("=" * 70)

# Missing values count per column
print("• Missing (Blank) Values Count in Excel Data:")
print(df.isna().sum())

# Imputation 1: Age ke missing cell ko Median se fill karna (Outlier-resistant)
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)

# Imputation 2: Performance_Score ke missing cell ko Mean se fill karna
mean_score = round(df["Performance_Score"].mean(), 1)
df["Performance_Score"] = df["Performance_Score"].fillna(mean_score)

print(f"\n• After Imputing Missing Values (Age filled with {median_age}, Score filled with {mean_score}):")
print(df[["Employee_Name", "Age", "Performance_Score"]])


# =============================================================================
# PART 7: GROUPBY & AGGREGATIONS (DYNAMIC PIVOT REPORT)
# =============================================================================
print("\n" + "=" * 70)
print(">>> PART 7: GROUPBY & AGGREGATIONS (EXCEL PIVOT SUMMARY) <<<")
print("=" * 70)

# Department-wise Total Headcount, Average Salary, Max Salary, Average Experience
dept_summary = df.groupby("Department").agg(
    Total_Employees=("Emp_ID", "count"),
    Avg_Salary=("Salary", "mean"),
    Max_Salary=("Salary", "max"),
    Avg_Exp=("Experience_Yrs", "mean")
).round(2)

print("• Department-wise Summary Report:")
print(dept_summary)


# =============================================================================
# PART 8: MERGING RELATIONAL EXCEL SHEETS (REPLACING VLOOKUP / XLOOKUP)
# =============================================================================
print("\n" + "=" * 70)
print(">>> PART 8: MERGING MULTIPLE EXCEL SHEETS (VLOOKUP REPLACEMENT) <<<")
print("=" * 70)

# Sheet 2: 'Projects' load karna
df_projects = pd.read_excel(EXCEL_FILE, sheet_name="Projects")
print("• Loaded 'Projects' Sheet:")
print(df_projects)

# 1. Inner Merge: Jo records dono sheets me common hain
merged_inner = pd.merge(df, df_projects, on="Emp_ID", how="inner")
print("\n• Inner Merge (Employees with Assigned Projects):")
print(merged_inner[["Emp_ID", "Employee_Name", "Department", "Project_Name"]])

# 2. Left Merge: Saare employees rahenge, jinka project nahi hai wahan NaN
merged_left = pd.merge(df, df_projects, on="Emp_ID", how="left")
print("\n• Left Merge (All Employees with Optional Projects - Like Excel VLOOKUP):")
print(merged_left[["Emp_ID", "Employee_Name", "Project_Name"]])


# =============================================================================
# DATA SCIENCE & MACHINE LEARNING LEVEL PANDAS CONCEPTS
# =============================================================================

# =============================================================================
# PART 9: CATEGORICAL ENCODING (ONE-HOT & ORDINAL MAPPING)
# =============================================================================
print("\n" + "=" * 70)
print(">>> PART 9: CATEGORICAL ENCODING (ONE-HOT & ORDINAL MAPPING) <<<")
print("=" * 70)

# 1. One-Hot Encoding: Machine Learning text categories ko binary numbers (0, 1) me chahta hai
# drop_first=True Dummy Variable Trap (multicollinearity) avoid karta hai
encoded_df = pd.get_dummies(df, columns=["Department"], prefix="Dept", drop_first=True, dtype=int)
print("• One-Hot Encoded DataFrame (drop_first=True):")
print(encoded_df[["Employee_Name", "Dept_HR", "Dept_IT", "Dept_Marketing"]].head(4))

# 2. Ordinal Encoding / Mapping: Category ki hierarchy preserve karna
performance_map = {"Needs Improvement": 1, "Average": 2, "Good": 3, "Star Performer": 4}
df["Performance_Band"] = pd.cut(
    df["Performance_Score"], 
    bins=[0, 75, 85, 92, 100], 
    labels=["Needs Improvement", "Average", "Good", "Star Performer"]
)
df["Performance_Encoded"] = df["Performance_Band"].map(performance_map)
print("\n• Ordinal Categorical Mapping (Performance Band to Rank):")
print(df[["Employee_Name", "Performance_Score", "Performance_Band", "Performance_Encoded"]].head(4))


# =============================================================================
# PART 10: FEATURE SCALING & NORMALIZATION (FROM SCRATCH)
# =============================================================================
print("\n" + "=" * 70)
print(">>> PART 10: FEATURE SCALING & NORMALIZATION (FROM SCRATCH) <<<")
print("=" * 70)

# 1. Min-Max Normalization (Scale range 0 to 1): (X - min) / (max - min)
salary_min = df["Salary"].min()
salary_max = df["Salary"].max()
df["Salary_MinMax_Scaled"] = ((df["Salary"] - salary_min) / (salary_max - salary_min)).round(4)

# 2. Z-Score Standardization (Mean=0, Std=1): (X - mean) / std
salary_mean = df["Salary"].mean()
salary_std = df["Salary"].std()
df["Salary_Z_Score"] = ((df["Salary"] - salary_mean) / salary_std).round(4)

print("• Feature Scaling Comparison (Raw vs MinMax Scaled vs Z-Score):")
print(df[["Employee_Name", "Salary", "Salary_MinMax_Scaled", "Salary_Z_Score"]].head(4))


# =============================================================================
# PART 11: OUTLIER DETECTION & CLIPPING (IQR METHOD)
# =============================================================================
print("\n" + "=" * 70)
print(">>> PART 11: OUTLIER DETECTION & CLIPPING (IQR METHOD) <<<")
print("=" * 70)

# Interquartile Range (IQR): Q3 (75th percentile) - Q1 (25th percentile)
q1 = df["Salary"].quantile(0.25)
q3 = df["Salary"].quantile(0.75)
iqr = q3 - q1

lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr
print(f"• Salary Thresholds: Q1={q1}, Q3={q3}, IQR={iqr}")
print(f"  Lower Bound: {lower_limit}, Upper Bound: {upper_limit}")

outliers = df[(df["Salary"] < lower_limit) | (df["Salary"] > upper_limit)]
print(f"  Outliers Count: {len(outliers)}")

# Outlier Treatment: Data loss avoid karne ke liye values ko limits pe clip karna
df["Salary_Clipped"] = df["Salary"].clip(lower=lower_limit, upper=upper_limit)
print("• Salary after Clipping extreme values:")
print(df[["Employee_Name", "Salary", "Salary_Clipped"]].head(4))


# =============================================================================
# PART 12: CORRELATION MATRIX & FEATURE SELECTION
# =============================================================================
print("\n" + "=" * 70)
print(">>> PART 12: CORRELATION MATRIX & FEATURE RELATIONSHIPS <<<")
print("=" * 70)

# Numerical columns ke pairwise correlation coefficients (-1 to +1)
numeric_cols = ["Age", "Salary", "Experience_Yrs", "Performance_Score"]
corr_matrix = df[numeric_cols].corr().round(3)
print("• Pearson Correlation Matrix (Feature Selection for ML):")
print(corr_matrix)


# =============================================================================
# PART 13: DISCRETIZATION & BINNING (pd.cut & pd.qcut)
# =============================================================================
print("\n" + "=" * 70)
print(">>> PART 13: CONTINUOUS FEATURE BINNING (pd.cut & pd.qcut) <<<")
print("=" * 70)

# 1. pd.cut: Custom interval brackets (Experience groups)
df["Exp_Category"] = pd.cut(
    df["Experience_Yrs"],
    bins=[0, 4, 8, 20],
    labels=["Junior (0-4)", "Mid-Level (5-8)", "Senior (9+)"]
)

# 2. pd.qcut: Equal frequency quantiles (Salary tiers)
df["Salary_Tier"] = pd.qcut(df["Salary"], q=3, labels=["Tier 1 (Entry)", "Tier 2 (Mid)", "Tier 3 (High)"])

print("• Continuous Feature Binning:")
print(df[["Employee_Name", "Experience_Yrs", "Exp_Category", "Salary", "Salary_Tier"]].head(5))


# =============================================================================
# PART 14: ADVANCED APPLY, LAMBDA & DATETIME FEATURE ENGINEERING
# =============================================================================
print("\n" + "=" * 70)
print(">>> PART 14: ADVANCED APPLY & DATETIME FEATURE EXTRACTION <<<")
print("=" * 70)

# 1. Multi-column custom logic using .apply()
df["Bonus_Eligibility"] = df.apply(
    lambda row: "High Bonus" if row["Performance_Score"] >= 88 and row["Experience_Yrs"] >= 5 else "Standard Bonus",
    axis=1
)

# 2. DateTime features for ML models
sample_dates = pd.date_range(start="2021-01-15", periods=len(df), freq="120D")
df["Joining_Date"] = sample_dates
df["Join_Year"] = df["Joining_Date"].dt.year
df["Join_Month"] = df["Joining_Date"].dt.month_name()
df["Join_Quarter"] = df["Joining_Date"].dt.quarter
df["Join_DayOfWeek"] = df["Joining_Date"].dt.day_name()
df["Is_Weekend_Join"] = df["Joining_Date"].dt.dayofweek.isin([5, 6])

print("• Extracted DateTime Features:")
print(df[["Employee_Name", "Joining_Date", "Join_Year", "Join_Month", "Join_DayOfWeek", "Bonus_Eligibility"]].head(4))


# =============================================================================
# PART 15: RESHAPING DATA (PIVOT TABLES)
# =============================================================================
print("\n" + "=" * 70)
print(">>> PART 15: MULTI-DIMENSIONAL PIVOT TABLE <<<")
print("=" * 70)

# Pivot Table: Mean Salary by Experience Category & Department
pivot_salary_exp = df.pivot_table(
    values="Salary",
    index="Exp_Category",
    columns="Department",
    aggfunc="mean",
    fill_value=0,
    observed=False
).round(2)

print("• Pivot Table (Average Salary by Experience & Department):")
print(pivot_salary_exp)


# =============================================================================
# PART 16: EXPORTING CLEANED & ENGINEERED DATA BACK TO EXCEL
# =============================================================================
print("\n" + "=" * 70)
print(">>> PART 16: EXPORTING AUTOMATION RESULTS BACK TO EXCEL <<<")
print("=" * 70)

OUTPUT_EXCEL = "processed_employees_analysis.xlsx"

with pd.ExcelWriter(OUTPUT_EXCEL, engine="openpyxl") as writer:
    # Cleaned and feature-engineered full employee dataset
    df.to_excel(writer, sheet_name="Engineered_Employees", index=False)
    
    # Department summary report
    dept_summary.to_excel(writer, sheet_name="Dept_Summary")
    
    # Pivot Table report
    pivot_salary_exp.to_excel(writer, sheet_name="Salary_Pivot")
    
    # Correlation Matrix
    corr_matrix.to_excel(writer, sheet_name="Correlation_Matrix")

print(f"• Successfully generated multi-sheet Excel report: '{OUTPUT_EXCEL}'")
print(f"  Sheets generated: 'Engineered_Employees', 'Dept_Summary', 'Salary_Pivot', 'Correlation_Matrix'")

print("\n" + "=" * 70)
print(">>> EXCEL PANDAS COMPLETE GUIDE (ExcepPandas.py) COMPLETED! <<<")
print("=" * 70)
