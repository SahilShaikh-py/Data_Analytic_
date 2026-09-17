# 🎨 Module 5: Visualizations & Executive Dashboard Designing (UI/UX)

### 🎯 Objective:
Transform raw tabular data and DAX calculations into polished, interactive, executive-grade dashboards. Master modern UI/UX principles, the new KPI Card visual, Dual-Axis combo charts, Matrix conditional data bars, Bookmarks, Custom Tooltip pages, and contextual Drill-Through navigation with precise step-by-step guidance.

---

## 📂 Reference Data & Measures for this Module:
- **Dimensions:** `product_dim[Category]`, `product_dim[SubCategory]`, `customer_dim[Region]`, `customer_dim[CustomerName]`
- **Calendar:** `Dim_Calendar[Year]`, `Dim_Calendar[MonthName]`, `Dim_Calendar[Date]`
- **Measures:** `[Total Revenue]`, `[Total Profit]`, `[Profit Margin %]`, `[Total Orders]`, `[YoY Sales Growth %]`

---

## 📌 Topic 5.1: Visual Selection & Best Practice Chart Matrix

Guiding principles for selecting the optimal visual type:

| Analytical Objective | Recommended Visual (⭐ Best Practice) | Anti-Pattern (❌ Avoid) |
| :--- | :--- | :--- |
| **Categorical Comparison** | Clustered Bar / Column Chart | 3D Charts (Distorts proportion and readability) |
| **Temporal Trend (Monthly/Daily)** | Line Chart, Area Chart | Pie Chart (Ineffective for time series analysis) |
| **Part-to-Whole Composition** | Donut Chart (Max 3-4 segments), Treemap | Pie Chart with 10+ categories (Visual clutter) |
| **Dual Metrics on Divergent Scales** | Line and Clustered Column Chart | Dual disconnected graphs side-by-side |
| **Tabular Detail with Hierarchies** | Matrix Visual (with Stepped Layout) | Unformatted Plain Table |
| **Executive Summary KPIs** | Card (New) Visual with Accent Bars | Legacy Multi-row card |

---

## 📌 Topic 5.2: Modern Executive KPI Cards Setup (New Card Visual)

### 🧭 Navigation Guide Path:
`Visualizations Pane > Visual Gallery > Card (new) [Icon displaying 123 card layout]`

---

### 🛠️ Step-by-Step UI Actions:
- **Step 1:** Click on a blank canvas area in the Report View.
- **Step 2:** Select the **Card (new)** visual from the Visualizations Pane.
- **Step 3 (Assign Metrics):**
  - In the right Data Pane, expand `_All_Measures`.
  - Drag the following 4 measures into the **Data** field well:
    1. `[Total Revenue]`
    2. `[Total Profit]`
    3. `[Profit Margin %]`
    4. `[Total Orders]`
- **Step 4 (Format Visual Styling):**
  - Click the **Format Visual** icon (Paintbrush icon) in the Visualizations Pane.
  - **Callout Values:**
    - Font: `Segoe UI Semibold`, Size: `26 pt`, Color: `#0F172A` (Dark Slate).
  - **Cards (Background & Styling):**
    - Under Shape, select **Rounded Rectangle** (Corner Radius: `10 px`).
    - Fill Color: `#FFFFFF` (Pure White) with Drop Shadow enabled.
  - **Accent Bar (Left Highlight Border):**
    - Toggle **Accent bar** to **On**.
    - Position: `Left`.
    - Color: `#2563EB` (Royal Blue).
    - Width: `4 px`.
- **Step 5:** Stretch the visual horizontally across the upper banner of the report canvas to establish an executive KPI header.

---

## 📌 Topic 5.3: Core Analytical Visuals Step-by-Step

---

### 🛠️ Visual 1: Line and Clustered Column Chart (Dual-Axis Monthly Trend)

#### Business Goal:
Plot monthly `Total Revenue` (Columns) alongside `Profit Margin %` (Line) on a single synchronized dual-axis canvas.

#### Step-by-Step UI Actions:
- **Step 1:** Click an empty canvas section.
- **Step 2:** Select the **Line and clustered column chart** icon from the Visualizations Pane.
- **Step 3 (Map Fields):**
  - **X-axis:** Drag `Dim_Calendar[MonthName]`.
  - **Column y-axis:** Drag `_All_Measures[Total Revenue]`.
  - **Line y-axis:** Drag `_All_Measures[Profit Margin %]`.
- **Step 4 (Format Visual):**
  - Navigate to **Format visual** (Paintbrush icon).
  - **Columns:** Set fill color to Corporate Navy (`#1E3A8A`).
  - **Lines:** Set style to Solid, Color to Emerald Green (`#10B981`), Width to `3 px`.
  - **Markers:** Toggle **On** (Display circular markers at each monthly interval).
  - **Data labels:** Toggle **On** to show exact values above data bars.
- **Step 5:** The resulting visual conveys revenue volume while revealing underlying margin health.

---

### 🛠️ Visual 2: Treemap Visual (Category & Sub-Category Proportions)

#### Business Goal:
Visualize hierarchical revenue distribution across Product Categories and Sub-Categories.

#### Step-by-Step UI Actions:
- **Step 1:** Select the **Treemap** icon in the Visualizations Pane.
- **Step 2 (Map Fields):**
  - **Category:** Drag `product_dim[Category]`.
  - **Details:** Drag `product_dim[SubCategory]`.
  - **Values:** Drag `_All_Measures[Total Revenue]`.
- **Step 3:** The canvas renders nested rectangular partitions sized proportionally to revenue volume.
- **Step 4:** Under Format Visual, turn on **Data labels** and customize categorical palette tones.

---

### 🛠️ Visual 3: Matrix Visual with Conditional Formatting (Data Bars)

#### Business Goal:
Render an expandable hierarchical tabular breakdown of Customer Regions and Customers with embedded data bars and margin indicators.

#### Step-by-Step UI Actions:
- **Step 1:** Select the **Matrix** visual in the Visualizations Pane.
- **Step 2 (Map Fields):**
  - **Rows:** Drag `customer_dim[Region]`, and nest `customer_dim[CustomerName]` underneath.
  - **Values:** Drag `_All_Measures[Total Revenue]` and `_All_Measures[Profit Margin %]`.
- **Step 3 (Embed Data Bars):**
  - In the Values field well, click the dropdown arrow on `Total Revenue`.
  - Hover over **Conditional formatting** ➡️ click **Data bars**.
  - Configure:
    - Positive bar color: `#3B82F6` (Light Blue).
    - Axis: Automatic.
    - Click **OK**.
- **Step 4 (Add Color Gradient to Margins):**
  - In the Values field well, click the dropdown on `Profit Margin %`.
  - **Conditional formatting** ➡️ click **Font color** or **Background color**.
  - Minimum color: `#FCA5A5` (Soft Coral Red), Maximum color: `#86EFAC` (Soft Emerald Green).
  - Click **OK**.
- **Step 5:** Expand any Region row using the **`+` (Expand Icon)** to reveal nested customer details with dynamic data bars.

---

## 📌 Topic 5.4: Slicers & Interactive Filtering Experience

### 🛠️ Modern Slicers Configuration:
- **Step 1:** Add a **Slicer** visual to the canvas.
- **Step 2:** Drag `customer_dim[Region]` into the **Field** bucket.
- **Step 3 (Tile Button Layout):**
  - Under Format Visual ➡️ **Slicer settings**.
  - Under Style, select **Tile** to convert vertical checkboxes into responsive filter buttons.

### 🛠️ Sync Slicers (Multi-Page Filter Synchronization):
- **Step 1:** In the ribbon, click the **View Tab**.
- **Step 2:** Within the **Show Panes** group, check **Sync Slicers**.
- **Step 3:** Click the Region tile slicer on the canvas.
- **Step 4:** The **Sync Slicers Pane** displays all report pages:
  - Check the **Sync (🔁)** checkbox across all target pages.
  - Check the **Visible (👁️)** checkbox on pages where the slicer control should physically appear.
- **Step 5:** Filter selections made on Page 1 will propagate across all synchronized pages.

---

## 📌 Topic 5.5: Advanced Interactive Dashboard UI/UX Features

---

### 🛠️ Feature 1: Bookmarks & Selection Pane (View-Swapping Buttons)

#### Business Goal:
Provide toggle buttons: **"📊 Chart View"** and **"📋 Table View"**, allowing users to dynamically alternate between visual representations on the same canvas space.

#### Step-by-Step UI Actions:
- **Step 1 (Open Necessary Panes):**
  - Go to the **View Tab** in the ribbon.
  - Enable both **Bookmarks** and **Selection** panes.
- **Step 2 (Position Overlapping Visuals):**
  - Superimpose a Chart visual and a Matrix table visual directly over each other in the identical canvas coordinates.
- **Step 3 (Create Bookmark 1 - Chart View):**
  - In the **Selection Pane**, click the **Eye Icon (👁️)** next to the Matrix visual to hide it.
  - In the **Bookmarks Pane**, click **Add**.
  - Rename the bookmark to **`BM_ChartView`**.
  - Click the three dots (`...`) next to the bookmark and **uncheck Data** *(Preserves user slicer selections during state toggles)*.
- **Step 4 (Create Bookmark 2 - Table View):**
  - In the Selection Pane, hide the Chart visual and unhide the Matrix table visual.
  - In the Bookmarks Pane, click **Add**.
  - Rename to **`BM_TableView`**.
  - Click the three dots and **uncheck Data**.
- **Step 5 (Create Action Buttons):**
  - In the ribbon, go to **Insert Tab** ➡️ **Buttons** ➡️ **Blank**.
  - Set button text to: `📊 Chart View`.
  - In the Format pane, enable **Action**.
  - Set Type to **Bookmark** and select **`BM_ChartView`**.
  - Repeat to create a `📋 Table View` button mapped to **`BM_TableView`**.
- **Step 6:** Test button interaction using `Ctrl + Click` in Desktop to verify visual swapping.

---

### 🛠️ Feature 2: Custom Tooltip Pages (Hover-Driven Drill-Down)

#### Business Goal:
When hovering over any monthly sales bar, display a custom pop-up card detailing top-performing products for that period.

#### Step-by-Step UI Actions:
- **Step 1:** Create a new page by clicking the `+` icon at the bottom. Name it **`Tooltip_Product_Breakdown`**.
- **Step 2 (Designate as Tooltip Canvas):**
  - In the Format Page pane, navigate to **Page information**.
  - Turn **Allow use as tooltip** to **On**.
  - Under **Canvas settings**, set Type to **Tooltip** (Scales canvas down to `320 x 240 px`).
- **Step 3 (Assemble Tooltip Visual):**
  - On this micro canvas, build a horizontal Bar Chart:
    - Y-axis: `product_dim[ProductName]`.
    - X-axis: `_All_Measures[Total Revenue]`.
- **Step 4 (Connect Tooltip to Main Visual):**
  - Return to the primary Dashboard page.
  - Select the Monthly Sales Line/Column chart.
  - In Format Visual, open **General** ➡️ expand **Tooltips**.
  - Under Page, select **`Tooltip_Product_Breakdown`**.
- **Step 5:** Hover over any monthly column to view the contextual product ranking pop-up.

---

### 🛠️ Feature 3: Drill-Through Pages (Entity Transaction Auditing)

#### Business Goal:
Allow report consumers to right-click a customer's name on an executive summary table and navigate directly to an audit page displaying their full order history.

#### Step-by-Step UI Actions:
- **Step 1:** Add a new report page named **`Customer_Drilldown_Details`**.
- **Step 2:** Assemble an order details Table (`OrderID`, `OrderDate`, `ProductName`, `Quantity`, `SalesAmount`).
- **Step 3 (Configure Drill-Through Target):**
  - Under the page settings, set **Page type** to **Drill-through**.
  - Drag **`customer_dim[CustomerName]`** into the **Drill-through from** field well.
  - *Result:* An automatic **`⬅️ Back Button`** appears in the top-left corner of the canvas.
- **Step 4 (Execute Drill-Through):**
  - Return to the primary Dashboard.
  - Right-click any customer (e.g., "Aarav Sharma") in the Customer Matrix.
  - Select **Drill-through ➡️ Customer_Drilldown_Details**.
  - Power BI jumps to the detail page, pre-filtered strictly for the selected customer.

---

## 📌 Topic 5.6: Executive Dashboard Design System (UI/UX Best Practices)

1. **Grid Layout & Alignment:** Align visual containers to an 8px grid system (`View Tab > Show gridlines` / `Snap to grid`).
2. **60-30-10 Color Hierarchy:**
   - **60% Dominant Base:** Clean neutral canvas surfaces (`#FFFFFF`, `#F8FAFC`).
   - **30% Structural Tones:** High-contrast slate navigation and typography (`#0F172A`, `#334155`).
   - **10% Intentional Accents:** Vibrant tones (`#2563EB` Royal Blue or `#10B981` Emerald Green) reserved for active slicers, KPIs, and visual callouts.
3. **Typography Standard:** Restrict report styling to a maximum of two font families (Standard recommendations: `Segoe UI` or `DIN`).

---

## 📌 Topic 5.7: Hands-On Visualization Practice Checklist (Student Lab Challenge)

- [ ] **Task 1:** Assemble a 4-metric executive KPI ribbon using the New Card visual with left accent borders.
- [ ] **Task 2:** Build a Dual-Axis Line and Clustered Column chart (Monthly Revenue vs. Profit Margin %).
- [ ] **Task 3:** Configure a Matrix visual with Region/Customer hierarchies and apply conditional data bars.
- [ ] **Task 4:** Format a Region Slicer into sleek horizontal tiles and synchronize across report pages via Sync Slicers.
- [ ] **Task 5:** Implement view-swapping toggle buttons (**Chart View 🔁 Table View**) using Bookmarks and the Selection pane.
- [ ] **Task 6:** Construct a dedicated Tooltip canvas and bind it to the primary monthly trend chart.
- [ ] **Task 7:** Configure a Customer Transaction Drill-Through page and validate navigation from the executive summary.
