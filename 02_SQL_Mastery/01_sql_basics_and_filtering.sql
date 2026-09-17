-- =============================================================================
-- SQL MODULE 01: DATABASE BASICS, SELECT & FILTERING (ANSI SQL / MySQL / SQLite)
-- =============================================================================

-- 1. Retrieving All Columns
SELECT * 
FROM employees;

-- 2. Selecting Specific Columns with Descriptive Aliases (AS)
SELECT 
    emp_id AS Employee_Identifier,
    emp_name AS Full_Name,
    department AS Dept,
    salary AS Monthly_Salary
FROM employees;

-- 3. Filtering Records with Comparison Operators
-- Find all employees earning at least Rs. 70,000
SELECT emp_name, department, salary
FROM employees
WHERE salary >= 70000;

-- 4. Compound Conditions using AND & OR
-- Find IT employees earning over Rs. 60,000 OR any employee in Executive leadership
SELECT emp_name, department, salary
FROM employees
WHERE (department = 'IT' AND salary > 60000)
   OR department = 'Executive';

-- 5. Range Filtering using BETWEEN (Inclusive)
-- Find employees aged between 25 and 35
SELECT emp_name, age, department
FROM employees
WHERE age BETWEEN 25 AND 35;

-- 6. List Membership Filtering using IN
-- Retrieve employees belonging to specific target departments
SELECT emp_name, department, salary
FROM employees
WHERE department IN ('IT', 'Finance', 'Data Analytics');

-- 7. Pattern Matching using LIKE and Wildcards (% and _)
-- % represents zero or more characters
-- _ represents exactly one single character
-- Find employees whose names begin with 'A'
SELECT emp_name, department
FROM employees
WHERE emp_name LIKE 'A%';

-- Find employees with email containing 'corp'
SELECT emp_name, email
FROM employees
WHERE email LIKE '%corp%';

-- 8. Handling Missing Values using IS NULL / IS NOT NULL
SELECT emp_name, department, bonus
FROM employees
WHERE bonus IS NOT NULL;

-- 9. Sorting Output using ORDER BY (Ascending & Descending)
-- Sort primarily by Department ascending, and secondarily by Salary descending
SELECT emp_name, department, salary
FROM employees
ORDER BY department ASC, salary DESC;

-- 10. Limiting Result Row Counts (Pagination)
-- Retrieve top 3 highest-paid employees in the organization
SELECT emp_name, department, salary
FROM employees
ORDER BY salary DESC
LIMIT 3;
