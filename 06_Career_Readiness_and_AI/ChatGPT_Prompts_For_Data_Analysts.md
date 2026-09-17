# 🤖 AI Prompt Engineering Playbook for Data Analysts (ChatGPT & Gemini)

Using AI assistants effectively as a "Pair Analyst" can accelerate query writing, DAX debugging, and executive communication by 5x. Below are production-tested prompt templates.

---

## 🗄️ 1. SQL Query Generation & Optimization

### Prompt: Complex Multi-Table SQL Query
```text
Act as a Senior Database Administrator and SQL Expert.
I have three tables:
1. `orders` (order_id, customer_id, product_id, order_date, amount)
2. `customers` (customer_id, customer_name, region, sign_up_date)
3. `products` (product_id, category, cost)

Please write a clean, optimized SQL query (compatible with PostgreSQL and MySQL 8.0) that:
1. Calculates the customer's total spend and order frequency.
2. Identifies the rank of each customer within their region using a Window Function.
3. Filters for customers who made at least 2 purchases in the last 90 days.
Include comments explaining the logic and index recommendations for performance.
```

### Prompt: SQL Performance Tuning
```text
I have the following SQL query that is taking over 45 seconds to execute on a 5-million row table:
[PASTE YOUR SLOW QUERY HERE]

Here is the table schema and existing indexes:
[PASTE SCHEMA]

Please analyze why this query is slow (e.g. Cartesian products, non-SARGable WHERE predicates, missing indexes) and provide an optimized rewrite.
```

---

## 📈 2. Power BI & DAX Measure Generation

### Prompt: Advanced Time Intelligence DAX
```text
Act as a Microsoft Certified Power BI Specialist (PL-300).
I have a Star Schema model with a fact table `FactSales` and a contiguous date table `DimDate`.
I need a DAX measure to calculate Month-over-Month (MoM) Percentage Growth in [Total Revenue].

Requirements:
- Must handle blank edge cases gracefully (divide-by-zero protection using DIVIDE).
- Must work seamlessly across Year, Quarter, and Month visual hierarchies.
- Please provide step-by-step comments explaining the filter context and CALCULATE transitions.
```

---

## 🐍 3. Python & Pandas Data Wrangling

### Prompt: Regex & Messy String Extraction
```text
Act as a Senior Python Data Engineer.
I have a Pandas DataFrame column `df['raw_feedback']` containing messy customer survey text with embedded phone numbers, currency symbols, and order IDs like "Ref: ORD-9402 spent Rs. 15,400 on 12/05/2026 call 9876543210".

Write a robust, vectorized Pandas function using regex (`re` or `.str.extract()`) to:
1. Extract the order ID pattern (ORD-XXXX).
2. Extract the cleaned numeric transaction amount as a float.
3. Extract the 10-digit Indian phone number.
Ensure invalid or missing patterns return NaN instead of raising an exception.
```

---

## 📊 4. Exploratory Data Analysis & Hypothesis Brainstorming

### Prompt: Generating EDA Hypotheses
```text
I am analyzing an e-commerce dataset for a retail company. The columns are:
[customer_id, age, gender, city, product_category, order_value, discount_pct, rating, delivery_days, return_status]

As a Lead Data Analyst, provide:
1. Five specific business hypotheses worth testing during EDA.
2. The exact bivariate and multivariate relationships to investigate.
3. Recommended charts (e.g. boxplot, heatmap) to visualize each hypothesis.
```

---

## 📝 5. Executive Storytelling & Stakeholder Emails

### Prompt: Translating Findings to C-Suite Communication
```text
Act as a Director of Business Intelligence.
Here are the raw analytical findings from our quarterly retail audit:
- Total Revenue: Rs. 4.52M (up 12% YoY)
- Net Profit Margin: Dropped from 44% to 40.16%
- Grocery Category: High transaction volume but only 28% margin due to 15% discounts
- Return Rate: Direct App has 1.8% return rate; Instagram ad campaigns have 6.2% return rate

Write a concise, high-impact executive summary email to the Chief Operating Officer (COO):
- Use an executive tone (bullet points, clear headers).
- Highlight the "So What?" behind the metrics.
- Provide 3 clear, prioritized recommendations.
```
