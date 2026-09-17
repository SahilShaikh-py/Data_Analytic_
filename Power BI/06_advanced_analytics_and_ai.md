  # 🧠 Module 6: Advanced Analytics & AI Capabilities in Power BI

### 🎯 Objective:
Power BI ke advanced Machine Learning aur AI algorithms ka use karke automated insights nikalna, root-cause analysis karna, forecasting karna, aur Python visuals integrate karna. Har AI tool ko **Step 1, Step 2, Step 3...** format me, exact field mappings aur practical business interpretation ke sath explain kiya gaya hai.

---

## 📂 Reference Data for this Module:
- **Fact Table:** `sales_data_1000` (`SalesAmount`, `Profit`, `Discount`, `Quantity`, `ShipMode`, `OrderDate`)
- **Dimensions:** `customer_dim` (`Region`, `Segment`, `City`), `product_dim` (`Category`, `SubCategory`)
- **Calendar:** `Dim_Calendar` (`Date`, `Year`, `MonthName`)
- **Measures:** `[Total Revenue]`, `[Total Profit]`, `[Profit Margin %]`

---

## 📌 Topic 6.1: AI Visual 1 - Decomposition Tree (Root-Cause Analysis)

### 1. Business Scenario (Kyun Zaroori Hai?):
Jab CEO poochte hain: *"Hamare $2 Million revenue me sabse bada hissa kis region aur product ka hai, aur kahan drop ho raha hai?"* Toh 10 alag charts banane ke bajaye ek single **Decomposition Tree** AI algorithm ka use karke instant drill-down breakdown deta hai.

### 🧭 Navigation Guide Path:
`Visualizations Pane > Visual Gallery > Decomposition Tree [Branching Tree Icon]`

---

### 🛠️ Step-by-Step UI Actions:
- **Step 1:** Report Canvas par click karein.
- **Step 2:** Visualizations Pane me **Decomposition Tree** icon par click karein.
- **Step 3 (Map Fields):**
  - **Analyze:** Drag karein metric: `_All_Measures[Total Revenue]`.
  - **Explain by:** Drag karein multiple dimensions:
    1. `customer_dim[Region]`
    2. `product_dim[Category]`
    3. `product_dim[SubCategory]`
    4. `sales_data_1000[ShipMode]`
    5. `customer_dim[Segment]`
- **Step 4 (Trigger AI Split):**
  - Canvas par `Total Revenue` ka single main bar ban jayega with total amount.
  - Bar ke right side me bane **`+` (Plus Icon)** par click karein.
  - Dropdown menu open hoga jisme do AI options dikhenge:
    - 💡 **High Value (AI Lightbulb):** AI automatically check karega ki saare fields me se sabse zyada revenue kis dimension ne generate kiya hai aur tree ko split kar dega.
    - 💡 **Low Value (AI Lightbulb):** AI sabse kam perform karne wale factor ko identify karega.
- **Step 5 (Multi-Level Expansion):**
  - Region bar ke aage wapas **`+`** par click karein aur `Category` choose karein.
  - Category ke aage **`+`** click karke `ShipMode` choose karein.
- **Step 6:** Canvas par ek clean, interactive root-cause tree generate ho jayega jise click karke user kisi bhi path ko dynamically explore kar sakta hai!

---

## 📌 Topic 6.2: AI Visual 2 - Key Influencers (Driver & Correlation Analysis)

### 1. Business Scenario:
Pata lagana ki kisi transaction me high profit margin ya low profitability hone ke peeche kaun se factors sabse zyada responsible hain (Category, Region, ya Discount?).

### 🧭 Navigation Guide Path:
`Visualizations Pane > Visual Gallery > Key Influencers [Lightbulb with Bar Graph Icon]`

---

### 🛠️ Step-by-Step UI Actions:
- **Step 1:** Visualizations Pane se **Key Influencers** visual select karein.
- **Step 2 (Map Fields):**
  - **Analyze:** Drag karein `_All_Measures[Profit Margin %]` (Ya `sales_data_1000[ReturnStatus]`).
  - **Explain by:** Drag karein:
    - `sales_data_1000[Discount]`
    - `product_dim[Category]`
    - `customer_dim[Region]`
    - `sales_data_1000[ShipMode]`



    2. **Top Segments Tab:**
       - Click karein **Top Segments** par.
       - AI clusters banakar bubble chart dikhayega:
         - *Segment 1: High Discount + Low UnitPrice = 85% of unprofitable transactions.*
- **Step 4:** Kisi bhi segment bubble par click karein: Right side me us segment ki complete statistical profile open ho jayegi!

---

## 📌 Topic 6.3: AI Visual 3 - Q&A (Natural Language Question & Answer)

### 1. Business Scenario:
Executives aur non-technical users jo Power BI nahi jante, wo English me question type karke chart banana chahte hain: *"Show total sales by region in 2024 as a donut chart"*.

### 🧭 Navigation Guide Path:
`Visualizations Pane > Visual Gallery > Q&A [Speech Bubble with Question Mark Icon]`  
*(Ya Canvas par blank jagah par Double-Click karein!)*

---

### 🛠️ Step-by-Step UI Actions:
- **Step 1:** Canvas ke blank space par **Double-Click** karein.
- **Step 2:** Canvas par ek search box appear hoga: *"Ask a question about your data"*.
- **Step 3:** Search box me type karein:
  ```text
  total revenue by category as bar chart
  ```
- **Step 4:** Jaise hi aap enter press karenge, Power BI NLP (Natural Language Processing) engine data model ko parse karke instant bar chart render kar dega!
- **Step 5 (Turn Q&A into Standard Visual):**
  - Search box ke right corner me bane **Turn this Q&A into a standard visual** icon par click karein.
  - Ab wo ek regular editable Bar Chart ban jayega!

---

## 📌 Topic 6.4: AI Visual 4 - Smart Narrative (Executive Commentary Generator)

### 1. Business Scenario:
Dashboard par bane huye charts ko dekhkar human analyst ki tarah automated dynamic English commentary paragraph generate karna.

### 🧭 Navigation Guide Path:
`Ribbon > Insert Tab > AI Visuals Group > Smart Narrative`  
*(Ya Visualizations Pane > Smart Narrative icon)*

---

### 🛠️ Step-by-Step UI Actions:
- **Step 1:** Pehle apne canvas par do charts banayein (Monthly Sales Line Chart aur Category Bar Chart).
- **Step 2:** Canvas ke blank area par click karein.
- **Step 3:** Top Ribbon me **Insert Tab** ➡️ **AI Visuals** group me **Smart Narrative** button par click karein.
- **Step 4:** Canvas par ek text box generate hoga jisme dynamically written bullet points honge:
  - *"Between Jan 2023 and Dec 2024, Total Revenue increased by 42.5%."*
  - *"Category 'Technology' accounted for the largest percentage (48.2%) of overall sales."*
- **Step 5 (Dynamic Slicer Interaction):**
  - Canvas par bane Region Slicer me "APAC" select karein.
  - Notice karein: Smart Narrative ka text automatically revise hokar sirf APAC region ke numbers bolne lagega!

---

## 📌 Topic 6.5: Analytics Pane & Time-Series Forecasting (Predictive AI)

### 1. Business Scenario:
Past 24 months ke historical sales trend ke base par aane wale **Next 6 Months ki Sales Forecast** karna with 95% confidence band.

### 🧭 Navigation Guide Path:
`Visualizations Pane > Analytics Tab [Magnifying Glass Icon]`

---

### 🛠️ Step-by-Step UI Actions:
- **Step 1:** Canvas par ek standard **Line Chart** create karein.
- **Step 2 (Map Time-Series Fields):**
  - **X-axis:** Drag `Dim_Calendar[Date]` (Ensure karein hierarchy nahi, actual continuous Date selected ho).
  - **Y-axis:** Drag `_All_Measures[Total Revenue]`.
- **Step 3 (Open Analytics Pane):**
  - Line chart ko select karein.
  - Visualizations Pane me 3rd tab **Analytics** (Magnifying glass icon) par click karein.
- **Step 4 (Add Forecast):**
  - Scroll down karein aur **Forecast** section ko expand karein.
  - **+ Add** button par click karein.
- **Step 5 (Set Forecast Parameters):**
  - **Forecast length:** Type karein `6` (Dropdown me `Months` select karein).
  - **Ignore last:** `0` (Agar backtesting karni ho toh 3 months ignore kar sakte hain).
  - **Confidence interval:** Select karein `95%` (Upper aur Lower risk boundary).
  - **Seasonality:** Type karein `12` (Annual seasonal cycles detect karne ke liye).
- **Step 6:** **Apply** button par click karein.
- **Step 7:** **Magic Result:** Line chart ke aage grey shaded band ke sath ek dotted future projection line draw ho jayegi!

---

## 📌 Topic 6.6: Integrating Python & R Visuals in Power BI

### 1. Concept:
Power BI me complex statistical plots (jaise Seaborn Heatmaps, Pairplots, Violin plots) banane ke liye built-in Python integration hota hai.

### 🛠️ Step-by-Step UI Actions:
- **Step 1 (Verify Python Environment):**
  - Power BI Desktop me: `File > Options and settings > Options > Python scripting`.
  - Check karein ki aapke computer ka Python home directory (e.g. `C:\Users\...\AppData\Local\Programs\Python\Python311`) detected ho. Click **OK**.
- **Step 2 (Add Python Visual):**
  - Visualizations Pane se **Python visual (Py icon)** par click karein.
  - Popup aayega: *"Enable script visuals"*. Click **Enable**.
- **Step 3 (Pass Data Columns):**
  - Right Data Pane se `sales_data_1000[SalesAmount]`, `sales_data_1000[Profit]`, aur `product_dim[Category]` ko visual ke **Values** bucket me drag karein.
  - Bottom me **Python script editor** open ho jayega jisme automatic code likha hoga:
    ```python
    # dataset = pandas.DataFrame(SalesAmount, Profit, Category)
    # dataset = dataset.drop_duplicates()
    ```
- **Step 4 (Write Matplotlib / Seaborn Code):**
  - Editor me neeche ye code type karein:
    ```python
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=dataset, x='SalesAmount', y='Profit', hue='Category', palette='viridis')
    plt.title('Sales vs Profit Correlation by Category')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()
    ```
- **Step 5 (Execute Script):**
  - Python editor bar ke right side me bane **Run (▶️ Play Icon)** par click karein.
- **Step 6:** Canvas par Python ka high-resolution statistical scatter plot render ho jayega!

---

## 📌 Topic 6.7: Hands-On AI & Analytics Practice Checklist (Student Lab Challenge)

- [ ] **Task 1:** Decomposition Tree visual create karein (`Analyze: Total Revenue`, `Explain by: Region, Category, ShipMode`).
- [ ] **Task 2:** High Value AI lightbulb trigger karke top revenue driver branch expand karein.
- [ ] **Task 3:** Key Influencers visual setup karein aur dekhein ki Discount ka Profit Margin par kya impact hai.
- [ ] **Task 4:** Canvas par double-click karke Q&A visual se *"total orders by region"* chart banayein aur standard visual me convert karein.
- [ ] **Task 5:** Smart Narrative add karein aur Region slicer change karke dynamic commentary test karein.
- [ ] **Task 6:** Monthly Line chart ke Analytics pane me jakar **6-Month Forecast with 95% Confidence Interval** add karein.
- [ ] **Task 7:** Python visual add karke `matplotlib` scatter plot successfully canvas par render karein.
