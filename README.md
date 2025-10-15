WorkSafe Risk Mini-Tool

Low/No-Code Musculoskeletal Risk Management Plug-in (Streamlit Prototype)

A lightweight, fully self-contained Streamlit app that helps safety professionals and small business owners identify, assess, control, review, and monitor musculoskeletal (MSD) risks — all without needing technical knowledge or databases.

1️⃣ Installation

Requirements

Python 3.10+

pip (Python package manager)

Step-by-Step Setup
# 1. Clone or download this folder
cd worksafe_mini_tool

# 2. (Recommended) Create a virtual environment
python -m venv .venv
# Activate it
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the app
streamlit run app.py


Once you run the command, Streamlit will open automatically at:
👉 http://localhost:8501

2️⃣ How to Use

🏁 Step 1 – Launch

After the app opens, you will see a sidebar with navigation options:

Info | New Assessment | History & Trends | Export/Import

🧭 Step 2 – Identify (Recognize potential risks)

Go to 📋 New Assessment.

Fill in the five input fields:

Date — defaults to today

Task Name — e.g. Lifting boxes, Assembly work

Posture Type — choose from dropdown (Neutral, Bending, Twisting, etc.)

Load (kg) — weight handled

Frequency (times/hour) — how often the task is performed

Click Calculate & Save.

The system will create a new record and show:

Risk Score (0–100)

Current Risk Level (Low / Moderate / High)

Recommended actions for control

📊 Step 3 – Assess (Evaluate the risk)

The app automatically calculates a risk score based on:

load weight × posture multiplier × frequency factor


The score is color-coded and categorized by thresholds:

🟢 Low (<40)

🟡 Moderate (40–59)

🟠 Medium-High (60–79)

🔴 High (≥80)

You can fine-tune thresholds via the sidebar sliders.

🧩 Step 4 – Control (Apply corrective actions)

Each posture type has its own recommended improvements, such as:

Use mechanical aids for heavy lifting

Introduce rest breaks or job rotation

Redesign workstation layout

Adjust height of workbench

These actions appear automatically below the risk score whenever you assess a task.

🔁 Step 5 – Review (Re-evaluate over time)

Navigate to 📈 History & Trends.

Select a specific task or view All Tasks.

Review the Risk Trend chart to see whether risk levels improve or worsen.

Download all records in CSV format for reports or audits.

📈 Step 6 – Monitor (Track performance and improvements)

Continuously update new assessments each week or month.

Tasks that remain at 🔴 High Risk can be prioritized for intervention.

The trend visualization helps identify patterns and measure the effectiveness of improvements.


3️⃣ Data Management

All information is stored locally in one simple file:

risk_data.csv


You can:

Open it directly in Excel or Google Sheets

Upload a new version via the Export/Import page

Replace old data or merge datasets manually

Share this CSV file among teams — no database or backend required

Example structure:

date,task,load_kg,frequency_per_hour,posture,risk_score
2025-10-11,Lift boxes,15,20,Bending,35
2025-10-12,Push cart,10,30,Pushing,33
2025-10-13,Assembly work,5,60,Repetitive Upper Limb,63

4️⃣ Core Concepts (5-Step Framework Alignment)

Step	Description	How It’s Implemented
Identify	Recognize physical activities that might cause MSDs	Simple form input for task, posture, load, and frequency
Assess	Quantify the risk using a numeric score	Algorithm calculates score (0–100) and categorizes it
Control	Recommend interventions	Context-based safety suggestions appear automatically
Review	Analyze data over time	Downloadable CSV and interactive trend chart
Monitor	Ensure continuous improvement	Trend visualization and threshold adjustment

5️⃣ Example Workflow

Open the app and fill in a new task (e.g., “Lifting boxes”).

Click “Calculate & Save” → see the risk score and recommendations.

Repeat weekly for key tasks.

View the Trend Chart to see improvements or rising risk.

Export CSV for your health & safety meeting.

6️⃣ Project Files

File	Description
app.py	Core Streamlit application
requirements.txt	Dependency list
risk_data.csv	Local dataset (auto-generated)
README.md	Documentation & usage guide