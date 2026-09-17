-- =============================================================================
-- SQL MODULE 02: AGGREGATIONS, GROUP BY & HAVING CLAUSE
-- =============================================================================

-- 1. Overall Aggregate Metrics
-- Calculating Total, Average, Lowest, Highest, and Count across all records
SELECT 
    COUNT(*) AS total_employees,
    COUNT(bonus) AS employees_receiving_bonus,  -- Nulls are automatically ignored!
    SUM(salary) AS total_monthly_payroll,
    AVG(salary) AS average_salary,
    MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary
FROM employees;

-- 2. Count of Unique Distinct Departments
SELECT COUNT(DISTINCT department) AS total_distinct_departments
FROM employees;

-- 3. Grouping Data with GROUP BY (Department-wise Analysis)
SELECT 
    department,
    COUNT(*) AS headcount,
    ROUND(AVG(salary), 2) AS avg_salary,
    SUM(salary) AS total_department_budget,
    MAX(salary) AS highest_paid_in_dept
FROM employees
GROUP BY department
ORDER BY total_department_budget DESC;

-- 4. Multi-Column Grouping (Department and City Breakdown)
SELECT 
    department,
    city,
    COUNT(*) AS employee_count,
    ROUND(AVG(salary), 2) AS avg_salary
FROM employees
GROUP BY department, city
ORDER BY department ASC, employee_count DESC;

-- 5. Filtering Aggregated Groups using HAVING
-- CRITICAL DISTINCTION:
-- WHERE filters individual rows BEFORE aggregation.
-- HAVING filters calculated groups AFTER aggregation.

-- Scenario: Find departments that have at least 2 employees AND an average salary > 65,000
SELECT 
    department,
    COUNT(*) AS headcount,
    ROUND(AVG(salary), 2) AS avg_dept_salary
FROM employees
GROUP BY department
HAVING COUNT(*) >= 2 AND AVG(salary) > 65000
ORDER BY avg_dept_salary DESC;

-- 6. Combining WHERE and HAVING in the Same Query
-- Step 1: Filter out inactive or probation employees (WHERE)
-- Step 2: Group by department
-- Step 3: Retain only departments with total payroll budget > 150,000 (HAVING)
SELECT 
    department,
    COUNT(*) AS permanent_headcount,
    SUM(salary) AS confirmed_payroll
FROM employees
WHERE is_active = 1
GROUP BY department
HAVING SUM(salary) > 150000
ORDER BY confirmed_payroll DESC;
