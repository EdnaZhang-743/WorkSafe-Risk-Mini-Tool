# 🧩 WorkSafe Risk Mini Tool

**WorkSafe Risk Mini Tool** is a lightweight, **no-database, low-code Streamlit plugin** that helps businesses and safety professionals manage **musculoskeletal disorder (MSD)** risks.  

It supports the five essential steps of risk management — **Identify, Assess, Control, Review, and Monitor** — all within an intuitive, user-friendly dashboard.

---

## ✨ Key Features

✅ **Low-code interface** – built with Streamlit, easy to modify and maintain  
✅ **No installation database required** – uses CSV import/export for simplicity  
✅ **MSD-focused risk assessment** – supports manual handling, lifting, pushing/pulling tasks  
✅ **Dynamic risk scoring** – adjustable thresholds for different workplaces  
✅ **Trend visualization** – historical charts to track safety performance  

---

## 🚀 Quick Start

### 1️⃣ Install Requirements

**Clone or download the repository:**
```bash
git clone https://github.com/EdnaZhang-743/WorkSafe-Risk-Mini-Tool.git
cd WorkSafe-Risk-Mini-Tool
(Optional) Create a virtual environment:

python -m venv .venv
For Windows:

.venv\Scripts\activate
For macOS/Linux:

source .venv/bin/activate
Install dependencies:

pip install -r requirements.txt
```bash
2️⃣ Run the App
```bash
streamlit run app.py
```bash
Then open your browser at 👉 http://localhost:8501

🧭 How to Use

🪪 Step 1 — Identify
Go to “New Assessment” and fill in:

Task name (e.g., “Box lifting”)
Load weight (kg)
Frequency per hour
Posture type (e.g., bending, repetitive upper limb, pushing/pulling)

🧮 Step 2 — Assess
The system calculates a risk score automatically based on the input data.
You can view all current assessments in the “Overview” tab.

⚙️ Step 3 — Control
Use sliders to adjust thresholds for “High”, “Medium-high”, and “Medium” risk levels.
This allows workplaces to fine-tune the assessment model to match their internal safety policies.

📊 Step 4 — Review
Export your current dataset as CSV for offline recordkeeping or import new data from Google Sheets.
All uploaded data will automatically refresh in the dashboard.

📈 Step 5 — Monitor
Track the historical risk trend of each task through the “History & Trends” section.
This helps identify slow improvement or high-risk patterns over time.

📦 Project Structure
WorkSafe-Risk-Mini-Tool/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Dependency list
├── risk_data.csv         # Sample dataset
└── README.md             # Documentation

🧰 Tech Stack
Category	Tools
Frontend	Streamlit
Backend	Python 3.x
Data	Pandas, NumPy
Charts	Matplotlib
File I/O	CSV / Google Sheets Integration

🧑‍💻 Developer Notes
This project is designed for non-technical users, such as workplace safety professionals.
Fully compatible with no-code or low-code maintenance environments.
Can be deployed independently, suitable for integrated use.

