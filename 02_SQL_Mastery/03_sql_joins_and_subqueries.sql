-- =============================================================================
-- SQL MODULE 03: RELATIONAL JOINS & NESTED SUBQUERIES
-- =============================================================================

-- -------------------------------------------------------------
-- SECTION A: RELATIONAL JOINS
-- -------------------------------------------------------------

-- 1. INNER JOIN: Returns only matching records present in BOTH tables
-- Scenario: Find all orders with matching customer details
SELECT 
    o.order_id,
    o.order_date,
    c.customer_name,
    c.city,
    c.tier
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id;

-- 2. LEFT JOIN: Returns ALL records from the Left table, plus matched records from Right
-- Scenario: Identify all customers, including those who have NEVER placed an order
SELECT 
    c.customer_id,
    c.customer_name,
    c.city,
    COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, c.city
ORDER BY total_orders ASC;

-- Scenario: Find "Zero-Order" inactive customers (Unmatched records)
SELECT 
    c.customer_id,
    c.customer_name,
    c.city
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- 3. Multi-Table Relational JOIN across 3 Tables (Orders, Customers, Products)
SELECT 
    o.order_id,
    o.order_date,
    c.customer_name,
    c.city,
    p.product_name,
    p.category,
    o.quantity,
    p.unit_price,
    (o.quantity * p.unit_price) AS line_item_total
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id
ORDER BY o.order_id ASC;


-- -------------------------------------------------------------
-- SECTION B: NESTED SUBQUERIES
-- -------------------------------------------------------------

-- 4. Subquery in WHERE Clause: Scalar comparison
-- Scenario: Find all products priced higher than the average product price
SELECT 
    product_name,
    category,
    unit_price
FROM products
WHERE unit_price > (SELECT AVG(unit_price) FROM products)
ORDER BY unit_price DESC;

-- 5. Subquery in WHERE Clause: List Membership (IN)
-- Scenario: Find all customers who ordered products in the 'Computers' category
SELECT customer_id, customer_name, city
FROM customers
WHERE customer_id IN (
    SELECT o.customer_id
    FROM orders o
    INNER JOIN products p ON o.product_id = p.product_id
    WHERE p.category = 'Computers'
);

-- 6. Subquery in FROM Clause (Derived Table)
-- Scenario: Calculate average spend across only customers who placed more than 1 order
SELECT 
    ROUND(AVG(customer_total_spend), 2) AS avg_spend_of_repeat_buyers
FROM (
    SELECT 
        o.customer_id,
        SUM(o.quantity * p.unit_price) AS customer_total_spend
    FROM orders o
    INNER JOIN products p ON o.product_id = p.product_id
    GROUP BY o.customer_id
    HAVING COUNT(o.order_id) > 1
) AS repeat_buyer_summary;

-- 7. Correlated Subquery in SELECT Clause (Scalar calculation)
-- Scenario: Display each customer alongside their total lifetime order count
SELECT 
    c.customer_id,
    c.customer_name,
    c.city,
    (SELECT COUNT(*) FROM orders o WHERE o.customer_id = c.customer_id) AS total_orders_placed
FROM customers c;
