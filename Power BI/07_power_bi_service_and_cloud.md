# ☁️ Module 7: Power BI Service (Cloud Collaboration, Sharing & Governance)

### 🎯 Objective:
Deploy Power BI Desktop reports to the Microsoft Cloud environment (`app.powerbi.com`), establish automated scheduled refreshes via the On-Premises Data Gateway, assemble cross-report executive dashboards, and enforce enterprise-grade **Row-Level Security (RLS)** with both Static and Dynamic access controls. Every workflow is detailed with step-by-step UI actions, configuration settings, and administrative best practices.

---

## 📂 Reference Data Context for this Module:
- **Fact Table:** `sales_data_1000.csv` containing a **`ManagerEmail`** attribute (`apac.manager@ysm.com`, `us.manager@ysm.com`, `emea.manager@ysm.com`).
- **Country & Region Columns:** Employed for validating localized security access partitions.

---

## 📌 Topic 7.1: Power BI Service Architecture & Licensing

In enterprise deployments, Power BI Desktop is strictly the report authoring environment. Business executives, managers, and end consumers consume reports through the web browser (`app.powerbi.com`) or native mobile apps.

| License Tier | Typical Cost | Target Persona | Key Architectural Capabilities |
| :--- | :--- | :--- | :--- |
| **Power BI Desktop (Free)** | $0 | Developer / Student | Local data ingestion, Power Query ETL, DAX formulation (No cloud sharing). |
| **Power BI Pro** | ~$10 / user / mo | Business Analyst & Viewers | Cloud publishing, App Workspace collaboration, Scheduled refresh up to 8x/day. |
| **Premium Per User (PPU)** | ~$20 / user / mo | Enterprise Analyst | Advanced AI capabilities, 100 GB semantic models, Scheduled refresh up to 48x/day. |
| **Fabric / Premium Capacity** | Capacity tier | Enterprise-wide | Read-only consumers can view reports without requiring individual Pro licenses. |

---

## 📌 Topic 7.2: Publishing Reports to Power BI Cloud (Step-by-Step)

### 🧭 Navigation Guide Path:
`Desktop Ribbon > Home Tab > Share Group > Publish`

---

### 🛠️ Step-by-Step UI Actions:
- **Step 1 (Sign In):**
  - Click the **Sign In** button in the upper-right corner of Power BI Desktop.
  - Enter your organizational work/school credentials (e.g., `arman@company.com`).
- **Step 2 (Save File):**
  - Save your active report: `File > Save As` ➡️ `Global_Sales_Executive_Dashboard.pbix`.
- **Step 3 (Initiate Deployment):**
  - Click the **Home Tab** in the ribbon.
  - In the **Share** group on the far right, click **Publish**.
- **Step 4 (Select Destination Workspace):**
  - In the destination dialog:
    - *My Workspace:* Private development and sandbox area.
    - *App Workspace (e.g., `Sales-Analytics-Team`):* Collaborative team workspace.
  - Choose the target destination and click **Select**.
- **Step 5 (Monitor Deployment & Launch):**
  - Track deployment progress: *"Publishing Global_Sales_Executive_Dashboard.pbix to Power BI..."*
  - Upon completion, a confirmation dialog appears with a direct link:  
    👉 **Open 'Global_Sales_Executive_Dashboard.pbix' in Power BI**.
  - Click the link to view and interact with the deployed report in your web browser.

---

## 📌 Topic 7.3: Reports vs. Dashboards (Critical Technical Distinction)

A fundamental concept tested across Power BI technical interviews:

| Parameter | Power BI Report (`.pbix`) | Power BI Dashboard (Cloud Tile Suite) |
| :--- | :--- | :--- |
| **Page Layout** | Multi-page document structure (Tabs: Page 1, Page 2, Page 3). | Strictly **Single-Page Canvas** (Unified high-level executive summary). |
| **Data Scope** | Bound strictly to **one single semantic model (dataset)**. | Can pin visual tiles sourced from **multiple independent reports and datasets**. |
| **Interactivity** | Full interactive capabilities: Slicers, cross-highlighting, and drill-through. | High-level KPI monitoring; clicking a visual tile navigates to the source report. |
| **NLP Querying** | Optional Q&A visual container. | Features a built-in persistent **Q&A Natural Language Bar** at the top. |

---

### 🛠️ Step-by-Step Creation of a Cloud Dashboard:
- **Step 1:** Open your deployed report in the browser (`app.powerbi.com`).
- **Step 2:** Hover your cursor over a high-level visual (e.g., `Total Revenue KPI Card` or `Monthly Sales Trend`).
- **Step 3:** Click the **Pin Visual Icon (📌)** that appears on the visual header.
- **Step 4:** In the modal dialog:
  - Select **New dashboard**.
  - Enter the Dashboard name: **`CEO Executive Suite`**.
- **Step 5:** Click **Pin**.
- **Step 6:** Navigate to other charts, click the Pin icon, and add them to the existing `CEO Executive Suite` dashboard.
- **Step 7:** Access **Dashboards** from the left navigation pane to view the unified executive dashboard.

---

## 📌 Topic 7.4: On-Premises Data Gateway & Automated Scheduled Refresh

### 1. Architectural Purpose:
When source files (`sales_data_1000.csv`) or transactional SQL databases reside within internal on-premises corporate infrastructure, cloud services (`app.powerbi.com`) cannot reach them through internal firewalls. The **On-Premises Data Gateway** functions as a secure, outbound-encrypted proxy facilitating communication between the cloud dataset and local resources.

---

### 🛠️ Step-by-Step Gateway Configuration:

#### Phase 1: Gateway Installation
- **Step 1:** In `app.powerbi.com`, click the **Download Icon** in the top navigation bar ➡️ select **Data Gateway**.
- **Step 2:** Run the downloaded installer.
- **Step 3:** Select **Standard mode** (Required for shared organizational scheduled refreshes).
- **Step 4:** Sign in with your organizational credentials and register the gateway (e.g., `YSM-Main-Gateway`).

#### Phase 2: Scheduling Automated Dataset Refresh in the Service
- **Step 1:** Open your workspace in Power BI Service (`app.powerbi.com`).
- **Step 2:** Locate the dataset (`Global_Sales_Executive_Dashboard`) and click the **Three Dots (`...`)** menu.
- **Step 3:** Select **Settings**.
- **Step 4 (Gateway Connection):**
  - Expand the **Gateway connections** section.
  - Toggle your active registered Gateway to **Running / Connected**.
- **Step 5 (Data Source Credentials):**
  - Expand **Data source credentials** ➡️ click **Edit credentials** ➡️ authenticate via Windows or OAuth2.
- **Step 6 (Configure Refresh Schedule):**
  - Expand the **Refresh** section.
  - Toggle the switch to **On**.
  - **Refresh frequency:** Select `Daily`.
  - **Time zone:** Select your local regional time zone (e.g., `(UTC +05:30) Chennai, Kolkata, Mumbai, New Delhi`).
  - **Time:** Click **Add another time** ➡️ set to `09:00 AM`.
  - Check: *"Send refresh failure notifications to the dataset owner"*.
- **Step 7:** Click **Apply** at the bottom.
- **Step 8:** The cloud semantic model will now refresh automatically every morning without manual intervention.

---

## 📌 Topic 7.5: Row-Level Security (RLS) - Static & Dynamic Implementations

### 1. Business Scenario:
The organization employs three regional executives:
- **APAC Regional Manager:** Strictly authorized to view transactions within APAC.
- **US Regional Manager:** Strictly authorized to view transactions within North America.
- Both managers access the identical report link, but the underlying data dynamically scopes to their geographic identity upon login.

---

### 🛠️ Method 1: Static Row-Level Security (Configured in Desktop)

#### Step-by-Step UI Actions:
- **Step 1:** Open the report in Power BI Desktop.
- **Step 2:** Click the **Modeling Tab** in the ribbon.
- **Step 3:** In the **Security** group, click **Manage Roles**.
- **Step 4:** In the Manage Roles modal:
  - Under Roles, click **Create**.
  - Name the role: **`APAC_Manager_Role`**.
- **Step 5 (Apply DAX Filter Expression):**
  - In the Tables list, select **`customer_dim`**.
  - In the DAX filter expression box, enter:
    ```dax
    [Region] = "APAC"
    ```
- **Step 6:** Click **Save**.

#### Testing Role Validation in Desktop:
- **Step 7:** In the **Modeling Tab**, click the **View as** button.
- **Step 8:** Check **`APAC_Manager_Role`** and click **OK**.
- **Step 9:** A persistent yellow indicator bar displays: *"Now viewing as: APAC_Manager_Role"*.
- **Step 10:** Verify that all charts and tables restrict display exclusively to APAC records. Click **Stop viewing** to exit.

---

### 🛠️ Method 2: Dynamic Row-Level Security using `USERPRINCIPALNAME()`

#### Business Context:
When managing hundreds of departmental managers, creating separate static roles is unmaintainable. Dynamic RLS extracts the logged-in user's Azure Active Directory (AAD) email and dynamically filters fact records.

#### Step-by-Step UI Actions:
- **Step 1:** In the **Modeling Tab**, click **Manage Roles**.
- **Step 2:** Click **Create** ➡️ name the role: **`Dynamic_Regional_Security`**.
- **Step 3:** Select the fact table: **`sales_data_1000`**.
- **Step 4:** In the DAX filter editor, enter:
  ```dax
  [ManagerEmail] = USERPRINCIPALNAME()
  ```
- **Step 5:** Click **Save**.
- **Step 6 (Simulate Dynamic User Identity):**
  - Click **View as**.
  - Check **Dynamic_Regional_Security**.
  - Check **Other user** and input a test manager's email: `apac.manager@ysm.com`.
  - Click **OK**.
  - The report immediately isolates transactions where `ManagerEmail` matches the simulated user.

---

### 🛠️ Method 3: Assigning Users to Roles in Power BI Cloud Service

- **Step 1:** Publish the `.pbix` report to your target workspace.
- **Step 2:** Navigate to the workspace in `app.powerbi.com`.
- **Step 3:** Locate the semantic model, click the **Three Dots (`...`)** menu ➡️ select **Security**.
- **Step 4:** On the Row-Level Security administration screen:
  - Highlight the target role (e.g., `APAC_Manager_Role`).
  - In the user assignment input, enter individual user emails or Azure Active Directory Security Groups (e.g., `arman.apac@company.com`).
  - Click **Add**.
- **Step 5:** Click **Save**. When assigned users access the report, security filtering applies automatically.

---

## 📌 Topic 7.6: Hands-On Cloud & RLS Practice Checklist (Student Lab Challenge)

- [ ] **Task 1:** Sign into Power BI Desktop using an organizational account and publish the report to an App Workspace.
- [ ] **Task 2:** Launch the deployed report in the browser, pin key metrics, and construct a consolidated **Executive Dashboard**.
- [ ] **Task 3:** In Desktop, author a Static RLS role restricting access to `[Region] = "APAC"`.
- [ ] **Task 4:** Validate the security rule using Desktop's **View as** simulation interface.
- [ ] **Task 5:** Implement Dynamic RLS using `[ManagerEmail] = USERPRINCIPALNAME()`.
- [ ] **Task 6:** Navigate to Cloud Security settings and bind real user emails to the configured security roles.
- [ ] **Task 7:** Establish an automated Scheduled Refresh timetable configured for daily morning execution.
