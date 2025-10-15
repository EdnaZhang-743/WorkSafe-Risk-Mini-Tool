# app.py
# WorkSafe Muscle Load Risk Mini-Tool
# Low/No-code prototype for musculoskeletal risk management
# Designed for non-technical users • Single-file • CSV storage
# Author: <Your Name> | Date: 2025-10-16

import os
from datetime import date
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# -----------------------------
# Basic Settings (readable and maintainable)
# -----------------------------
st.set_page_config(page_title="WorkSafe Risk Mini-Tool", page_icon="🦴", layout="wide")

DATA_PATH = "risk_data.csv"  # Local CSV data file (auto-created on first run)
DATE_FMT = "%Y-%m-%d"

# Easy-to-understand posture weights
POSTURE_WEIGHTS = {
    "Neutral": 1.00,
    "Bending": 1.25,
    "Twisting": 1.30,
    "Pushing": 1.15,
    "Pulling": 1.15,
    "Repetitive Upper Limb": 1.35,
}

# Suggestions for each posture and risk level
SUGGESTIONS = {
    "Neutral": [
        "Maintain current methods and schedule micro breaks (stretch/relax).",
        "Monitor changes in load and frequency, reassess if thresholds are exceeded."
    ],
    "Bending": [
        "Use adjustable workbenches or raise workpieces to reduce bending.",
        "Bend knees instead of waist; use lifting aids if necessary."
    ],
    "Twisting": [
        "Reorganize layout to avoid torso twisting (turn feet instead).",
        "Keep frequently used items directly in front to minimize reach."
    ],
    "Pushing": [
        "Use carts with good wheels to reduce friction.",
        "Work in pairs or divide the task if heavy."
    ],
    "Pulling": [
        "Prefer pushing over pulling; reduce static friction at start.",
        "Use handles or straps for better grip and leverage."
    ],
    "Repetitive Upper Limb": [
        "Schedule task rotation and micro breaks.",
        "Use jigs or mechanical aids to reduce repetition."
    ],
}

# Risk thresholds (non-technical users can adjust via sidebar)
DEFAULT_THRESHOLDS = {
    "high": 80,
    "medium": 60,
    "mild": 40
}

# -----------------------------
# Utility Functions
# -----------------------------
def _ensure_seed_csv(path: str):
    """Create demo data if not existing, so non-technical users can try immediately."""
    if os.path.exists(path):
        return
    demo = pd.DataFrame([
        {"date": "2025-10-11", "task": "Lift boxes", "load_kg": 15, "frequency_per_hour": 20, "posture": "Bending"},
        {"date": "2025-10-12", "task": "Push cart", "load_kg": 10, "frequency_per_hour": 30, "posture": "Pushing"},
        {"date": "2025-10-13", "task": "Assembly work", "load_kg": 5,  "frequency_per_hour": 60, "posture": "Repetitive Upper Limb"},
    ])
    demo["risk_score"] = demo.apply(
        lambda r: compute_risk(r["load_kg"], r["frequency_per_hour"], r["posture"]),
        axis=1
    )
    demo.to_csv(path, index=False)

def load_data() -> pd.DataFrame:
    _ensure_seed_csv(DATA_PATH)
    df = pd.read_csv(DATA_PATH)
    df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.date
    df["task"] = df["task"].astype(str)
    df["posture"] = df["posture"].astype(str)
    df["load_kg"] = pd.to_numeric(df["load_kg"], errors="coerce")
    df["frequency_per_hour"] = pd.to_numeric(df["frequency_per_hour"], errors="coerce")
    df["risk_score"] = pd.to_numeric(df["risk_score"], errors="coerce")
    return df.dropna(subset=["date", "task", "posture", "load_kg", "frequency_per_hour", "risk_score"])

def save_record(record: dict):
    df = load_data()
    df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)

def _norm(value, vmin, vmax):
    if vmax == vmin:
        return 0
    v = max(min(value, vmax), vmin)
    return 100 * (v - vmin) / (vmax - vmin)

def compute_risk(load_kg: float, freq_ph: int, posture_label: str) -> int:
    """Explainable score (0–100)"""
    load_norm = _norm(load_kg, 0, 50)
    freq_norm = _norm(freq_ph, 0, 60)
    posture_w = POSTURE_WEIGHTS.get(posture_label, 1.0)

    bonus = 0
    if "Repetitive" in posture_label and freq_ph >= 30:
        bonus = 8

    raw = (0.55 * load_norm + 0.35 * freq_norm) * posture_w + bonus
    return int(max(0, min(100, round(raw))))

def risk_label(score: int, th: dict) -> str:
    if score >= th["high"]:
        return "🔴 High Risk"
    if score >= th["medium"]:
        return "🟠 Medium-High Risk"
    if score >= th["mild"]:
        return "🟡 Moderate Risk"
    return "🟢 Low Risk"

def advice_list(posture: str, score: int, th: dict):
    base = SUGGESTIONS.get(posture, SUGGESTIONS["Neutral"]).copy()
    if score >= th["high"]:
        base.insert(0, "Immediately apply engineering/organizational control: mechanical aids, teamwork, reduced load/frequency.")
    elif score >= th["medium"]:
        base.insert(0, "Optimize workstation and methods soon; schedule short-term review.")
    elif score >= th["mild"]:
        base.insert(0, "Fine-tune posture or pace, set reminders to avoid cumulative strain.")
    else:
        base.insert(0, "Maintain current measures and continue monitoring.")
    return base

def draw_trend(df: pd.DataFrame, task_filter: str | None):
    if task_filter and task_filter != "All Tasks":
        df = df[df["task"] == task_filter]
    if df.empty:
        st.info("No historical records available.")
        return
    dfp = df.sort_values("date")
    fig, ax = plt.subplots(figsize=(8, 3.6))
    ax.plot(dfp["date"], dfp["risk_score"], marker="o")
    ax.set_xlabel("Date")
    ax.set_ylabel("Risk Score")
    ax.set_title(f"Risk Trend ({task_filter})" if task_filter and task_filter != "All Tasks" else "Risk Trend (All Tasks)")
    ax.grid(True, linestyle="--", alpha=0.4)
    st.pyplot(fig)

# -----------------------------
# Sidebar: Navigation & Threshold Adjustments
# -----------------------------
st.sidebar.title("🦴 WorkSafe Risk Tool")
page = st.sidebar.radio("Navigation", ["📖 Info", "📋 New Assessment", "📈 History & Trends", "⬇️ Export/Import"])

with st.sidebar.expander("(Optional) Adjust Risk Thresholds"):
    high = st.slider("High Risk Threshold", 70, 95, DEFAULT_THRESHOLDS["high"])
    medium = st.slider("Medium-High Risk Threshold", 50, 89, DEFAULT_THRESHOLDS["medium"])
    mild = st.slider("Moderate Risk Threshold", 20, 59, DEFAULT_THRESHOLDS["mild"])
TH = {"high": high, "medium": medium, "mild": mild}

st.sidebar.caption("Single file • No database • CSV-based\nIdeal for non-technical users to use and maintain independently")

# -----------------------------
# Page: Information / Intro
# -----------------------------
if page == "📖 Info":
    st.title("WorkSafe Musculoskeletal Risk Management Plug-in (Demo)")
    st.markdown("""
**This mini-tool helps you:**
- **Identify**: Record task, load, frequency, and posture
- **Assess**: Generate a 0–100 **risk score** with **control suggestions**
- **Control**: Review recommended measures for each posture
- **Review**: Download and replace CSV data for periodic reviews
- **Monitor**: Visualize trends to prioritize high-risk tasks

> Tip: Go to **📋 New Assessment** on the left to start.
""")

# -----------------------------
# Page: New Assessment
# -----------------------------
elif page == "📋 New Assessment":
    st.title("📋 New Musculoskeletal Risk Assessment")
    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        eval_date = st.date_input("Date", value=date.today())
        task = st.text_input("Task Name (e.g. Lift boxes / Assembly work)")
        posture = st.selectbox("Posture Type", list(POSTURE_WEIGHTS.keys()), index=0)
        load_kg = st.number_input("Load (kg)", min_value=0.0, max_value=200.0, value=10.0, step=1.0)
        freq = st.number_input("Frequency (times/hour)", min_value=0, max_value=240, value=20, step=5)

        if st.button("Calculate & Save", type="primary", use_container_width=True):
            if not task.strip():
                st.warning("Please enter a task name.")
            else:
                score = compute_risk(float(load_kg), int(freq), posture)
                st.success("Record saved ✅")

                record = {
                    "date": eval_date.strftime(DATE_FMT),
                    "task": task.strip(),
                    "load_kg": float(load_kg),
                    "frequency_per_hour": int(freq),
                    "posture": posture,
                    "risk_score": int(score),
                }
                save_record(record)

                st.markdown("---")
                left, right = st.columns(2)
                with left:
                    st.metric("Risk Score", f"{score}/100")
                    st.write(f"**Current Level: {risk_label(score, TH)}**")
                with right:
                    st.write("**Recommended Actions:**")
                    for tip in advice_list(posture, score, TH):
                        st.write(f"- {tip}")

                df_all = load_data()
                draw_trend(df_all[df_all["task"] == task.strip()], task.strip())

    with col2:
        st.markdown("#### Instructions (No IT background needed)")
        st.markdown("""
- **Only 5 fields required:** date, task, posture, load, frequency  
- Click “Calculate & Save” to complete an assessment  
- Higher score = higher risk (you can adjust thresholds on the sidebar)  
- Recommendations provide immediate improvement actions  
- Check historical data and trends under “📈 History & Trends”
        """)

# -----------------------------
# Page: History & Trends
# -----------------------------
elif page == "📈 History & Trends":
    st.title("📈 History & Trends")
    df = load_data()
    if df.empty:
        st.info("No historical records yet. Please add a new assessment.")
    else:
        colA, colB = st.columns([2, 1], gap="large")
        with colB:
            tasks = ["All Tasks"] + sorted(df["task"].unique().tolist())
            chosen = st.selectbox("Filter by Task", tasks, index=0)
            st.download_button(
                label="Download CSV Data",
                data=df.to_csv(index=False).encode("utf-8"),
                file_name="risk_data_export.csv",
                mime="text/csv",
                use_container_width=True
            )
        with colA:
            draw_trend(df, chosen)

        st.markdown("#### Recent Records")
        st.dataframe(
            df.sort_values(["date"], ascending=False),
            use_container_width=True,
            hide_index=True
        )

# -----------------------------
# Page: Export / Import
# -----------------------------
else:
    st.title("⬇️ Export / Import")
    df = load_data()
    st.markdown("**Current Data Preview** (Click top right corner to fullscreen)")
    st.dataframe(df.sort_values("date", ascending=False), use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown("**Import New Data (CSV):** Must include columns `date, task, load_kg, frequency_per_hour, posture`. "
                "If `risk_score` is missing, it will be auto-calculated.")

    uploaded = st.file_uploader("Upload CSV to replace current data (e.g. exported from Google Sheets)", type=["csv"])
    if uploaded:
        try:
            new_df = pd.read_csv(uploaded)
            req_cols = {"date", "task", "load_kg", "frequency_per_hour", "posture"}
            if not req_cols.issubset(set(new_df.columns)):
                st.error(f"Missing required columns: {sorted(req_cols)}")
            else:
                if "risk_score" not in new_df.columns:
                    new_df["risk_score"] = new_df.apply(
                        lambda r: compute_risk(float(r["load_kg"]), int(r["frequency_per_hour"]), str(r["posture"])),
                        axis=1
                    )
                new_df["date"] = pd.to_datetime(new_df["date"], errors="coerce").dt.date
                new_df = new_df.dropna(subset=["date"])
                new_df.to_csv(DATA_PATH, index=False)
                st.success("Data replaced ✅. Go to 'History & Trends' to view updates.")
        except Exception as e:
            st.error(f"Import failed: {e}")
