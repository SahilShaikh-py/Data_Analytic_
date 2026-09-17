# 🧠 Vibe Coding Stage 2: Google AI Studio & Gemini Integration

Google AI Studio is Google's web-based prototyping environment for developers to experiment with Gemini models, engineer system prompts, test few-shot examples, and generate production code with one click.

---

## 📌 1. Setting Up Google AI Studio

1. **Access Portal:** Navigate to [https://aistudio.google.com/](https://aistudio.google.com/).
2. **Select Model:** Choose **Gemini 1.5 Flash** (Ultra-fast latency, high throughput, free tier friendly) or **Gemini 1.5 Pro** (Complex multi-step reasoning).
3. **Generate API Key:** Click **Get API key** ➡️ Create key in a new Google Cloud project. Store this key securely; never commit it to public GitHub repositories!

---

## 📌 2. System Instructions (Prompt Engineering for Analytics)

System instructions dictate the model's persona, constraints, and behavioral boundaries before user questions are evaluated.

### Production System Prompt for SQL Analytics Assistant:
```text
You are DataSense AI, an expert Senior Data Architect and SQL generator.

Target Database Schema:
- Table `orders` (order_id INT, customer_id INT, product_id INT, order_date DATE, quantity INT, amount FLOAT, status TEXT)
- Table `customers` (customer_id INT, customer_name TEXT, city TEXT, tier TEXT)
- Table `products` (product_id INT, product_name TEXT, category TEXT, unit_price FLOAT)

Rules:
1. Output MUST be strictly valid JSON conforming to the requested schema.
2. Generate only read-only SELECT queries. Never generate DROP, DELETE, INSERT, or ALTER statements.
3. If the user asks an ambiguous question, return a clarification request in the "explanation" field.
4. Always alias computed columns with descriptive, professional business headers.
```

---

## 📌 3. Enforcing Structured JSON Output

To reliably connect Gemini to your web application backend without regex or fragile string parsing, configure **Structured JSON Outputs**:

```python
import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
    "temperature": 0.1,  # Low temperature for deterministic SQL generation
    "top_p": 0.95,
    "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="You are a data assistant that converts natural language to SQLite queries."
)

prompt = "Show me the top 3 customers who spent the most money in Mumbai."
response = model.generate_content(prompt)
print(response.text)
```

### Expected Structured JSON Response:
```json
{
  "sql_query": "SELECT c.customer_name, SUM(o.amount) AS total_spend FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id WHERE c.city = 'Mumbai' GROUP BY c.customer_id, c.customer_name ORDER BY total_spend DESC LIMIT 3;",
  "chart_type": "bar",
  "explanation": "This query aggregates total order spend for Mumbai customers and ranks them in descending order, returning the top 3."
}
```
