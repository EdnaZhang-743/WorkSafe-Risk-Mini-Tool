# 🦺 WorkSafe Risk Mini Tool

A **lightweight, low-code Streamlit tool** that helps safety professionals and small businesses quickly **identify, assess, control, review, and monitor** workplace musculoskeletal disorder (MSD) risks — all in an intuitive, database-free interface.

---

## ✨ Key Features

✅ **Low-code interface** – built with Streamlit, easy to modify and maintain  
✅ **No database installation required** – uses simple CSV import/export  
✅ **MSD-focused risk assessment** – supports manual handling, lifting, pushing/pulling tasks  
✅ **Dynamic risk scoring** – adjustable thresholds for different workplaces  
✅ **Trend visualization** – historical charts to track safety performance  

---

## 🚀 Quick Start

### 1️⃣ Install Requirements

Clone or download the repository:

```bash
git clone https://github.com/EdnaZhang-743/WorkSafe-Risk-Mini-Tool.git
cd WorkSafe-Risk-Mini-Tool

# (Optional) Create a virtual environment
python -m venv .venv

# For Windows
.venv\Scripts\activate

# For macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

---

2️⃣ Run the App

```bash
streamlit run app.py
Then open your browser at 👉 http://localhost:8501

---

🧭 How to Use
Step 1 – Identify
Go to “New Assessment” tab and fill in:

Task name (e.g., “Box lifting”)
Load weight (kg)
Frequency per hour
Posture type (e.g., bending, repetitive upper limb, pushing/pulling)

Step 2 – Assess
The system automatically generates a risk score based on your inputs.
You can view results immediately in the Overview tab.

Step 3 – Control
Based on the calculated risk, the tool provides control suggestions, such as:

Use lifting aids
Rotate tasks
Reduce frequency
Provide ergonomic training

Step 4 – Review
Use the History & Trends tab to view past data, compare tasks, and observe progress.
Charts display risk trends and allow filtering by date or task type.

Step 5 – Monitor
Regularly import/export updated CSV data for ongoing monitoring.
All information can be shared or reviewed offline — no database needed.

---

💾 Data Import / Export
Upload CSV files to replace existing data
Export current results with one click
Ideal for users without IT background — no installation, no server setup

---

🧩 Tech Stack
Component	Technology
Frontend	Streamlit (Python Web Framework)
Backend Logic	pandas + numpy
Visualization	matplotlib
Data Storage	Local CSV files

---

🧠 Project Background
This tool was designed for workplace ergonomics and safety assessment, helping identify and control manual handling risks such as lifting, pushing, and repetitive motion tasks.
It aligns with the core stages of risk management defined by WorkSafe:

Identify → Assess → Control → Review → Monitor
