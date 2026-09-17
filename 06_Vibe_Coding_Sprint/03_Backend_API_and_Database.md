# ⚙️ Vibe Coding Stage 3: Backend API Architecture, Database & Security

A robust web application requires a secure backend to manage database connections, sanitize inputs, execute queries, and expose clean RESTful endpoints to the frontend.

---

## 📌 1. REST API Endpoint Specifications

| Method | Endpoint | Description | Request Payload | Response |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/api/health` | Service health & DB connection check | None | `{"status": "ok", "db": "connected"}` |
| `GET` | `/api/kpis` | Executive summary KPI cards | None | `{"revenue": 4520000, "orders": 576, "margin": 40.16}` |
| `POST`| `/api/query` | Natural language question to SQL execution | `{"question": "Top 5 products"}` | `{"sql": "...", "data": [...], "chart": "bar"}` |
| `GET` | `/api/export` | Download query results as CSV | Query string params | Streaming CSV attachment |

---

## 📌 2. Security & SQL Injection Protection

Allowing arbitrary user-generated SQL is dangerous. We enforce **strict defense-in-depth**:

1. **Read-Only Database Connection:** Open the SQLite database with `mode=ro` (Read-Only) URI parameter. Any `DROP`, `DELETE`, or `UPDATE` query fails at the database driver level.
2. **Keyword Whitelisting & Blacklist Filtering:**
   ```python
   def sanitize_query(sql: str) -> bool:
       sql_upper = sql.upper().strip()
       if not sql_upper.startswith("SELECT") and not sql_upper.startswith("WITH"):
           return False
       forbidden_keywords = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "TRUNCATE", "EXEC", "--", ";"]
       for kw in forbidden_keywords:
           if kw in sql_upper:
               return False
       return True
   ```
3. **CORS (Cross-Origin Resource Sharing):** Explicitly whitelist authorized frontend origins (e.g. `http://localhost:3000` or your live Vercel domain).

---

## 🧪 3. AI-Assisted Automated Test Generation

Generate comprehensive unit and integration tests using `pytest` to guarantee reliability before deployment:

```python
import pytest
from app import app, sanitize_query

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Verify backend health endpoint responds with 200 OK."""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"

def test_sql_injection_prevention():
    """Verify dangerous destructive SQL commands are rejected."""
    malicious_query = "DROP TABLE customers;"
    assert sanitize_query(malicious_query) is False

def test_valid_query_allowed():
    """Verify clean SELECT statements pass validation."""
    valid_query = "SELECT * FROM orders WHERE amount > 1000"
    assert sanitize_query(valid_query) is True
```
