-- =============================================================================
-- CAPSTONE SQL ANALYTICS: AURAKART ENTERPRISE KPI EXTRACTION
-- Database: aurakart_analytics.db (SQLite / MySQL)
-- =============================================================================

-- 1. Monthly Revenue, Profit & Margin Health Trend
SELECT 
    f.YearMonth,
    COUNT(f.OrderID) AS total_orders,
    SUM(f.GrossSales) AS total_gross_sales,
    SUM(f.DiscountAmount) AS total_discounts_given,
    SUM(f.NetRevenue) AS total_net_revenue,
    SUM(f.GrossProfit) AS total_gross_profit,
    ROUND((SUM(f.GrossProfit) * 100.0 / SUM(f.NetRevenue)), 2) AS gross_margin_pct
FROM fact_orders f
WHERE f.DeliveryStatus != 'Cancelled'
GROUP BY f.YearMonth
ORDER BY f.YearMonth ASC;

-- 2. Category-Wise Performance & Discount Dependency Audit
SELECT 
    p.Category,
    COUNT(f.OrderID) AS units_ordered,
    SUM(f.NetRevenue) AS category_revenue,
    SUM(f.GrossProfit) AS category_profit,
    ROUND((SUM(f.GrossProfit) * 100.0 / SUM(f.NetRevenue)), 2) AS margin_pct,
    ROUND(AVG(f.DiscountApplied) * 100, 2) AS avg_discount_rate_pct
FROM fact_orders f
INNER JOIN dim_products p ON f.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY category_revenue DESC;

-- 3. Regional Market Hub Leaderboard & Customer Tier Analysis
SELECT 
    c.City,
    c.MarketTier,
    COUNT(DISTINCT c.CustomerID) AS active_customers,
    COUNT(f.OrderID) AS total_transactions,
    SUM(f.NetRevenue) AS regional_revenue,
    ROUND(AVG(f.NetRevenue), 2) AS avg_order_value
FROM fact_orders f
INNER JOIN dim_customers c ON f.CustomerID = c.CustomerID
WHERE f.DeliveryStatus = 'Delivered'
GROUP BY c.City, c.MarketTier
ORDER BY regional_revenue DESC;

-- 4. Customer Lifetime Value (CLV) & VIP Segmentation
SELECT 
    c.CustomerID,
    c.CustomerName,
    c.City,
    c.AcquisitionChannel,
    COUNT(f.OrderID) AS lifetime_orders,
    SUM(f.NetRevenue) AS total_lifetime_spend,
    SUM(f.GrossProfit) AS total_profit_contributed,
    CASE 
        WHEN SUM(f.NetRevenue) >= 500000 THEN 'Tier 1 - VIP Platinum'
        WHEN SUM(f.NetRevenue) >= 300000 THEN 'Tier 2 - High Growth'
        ELSE 'Tier 3 - Standard'
    END AS customer_vip_segment
FROM dim_customers c
INNER JOIN fact_orders f ON c.CustomerID = f.CustomerID
GROUP BY c.CustomerID, c.CustomerName, c.City, c.AcquisitionChannel
ORDER BY total_lifetime_spend DESC;

-- 5. Acquisition Channel Conversion & Fulfillment Reliability
SELECT 
    c.AcquisitionChannel,
    COUNT(f.OrderID) AS orders_acquired,
    SUM(f.NetRevenue) AS revenue_generated,
    ROUND(SUM(CASE WHEN f.DeliveryStatus = 'Delivered' THEN 1 ELSE 0 END) * 100.0 / COUNT(f.OrderID), 2) AS delivery_success_rate_pct,
    ROUND(SUM(CASE WHEN f.DeliveryStatus = 'Returned' THEN 1 ELSE 0 END) * 100.0 / COUNT(f.OrderID), 2) AS return_rate_pct
FROM fact_orders f
INNER JOIN dim_customers c ON f.CustomerID = c.CustomerID
GROUP BY c.AcquisitionChannel
ORDER BY revenue_generated DESC;
