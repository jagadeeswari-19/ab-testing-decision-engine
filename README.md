🚀 A/B Testing Decision Engine

A production-grade platform to analyze A/B experiments, evaluate statistical significance, and generate automated rollout decisions with business impact.

🌐 Live Demo (Replit)
🔗 Application: <YOUR_REPLIT_LINK>

This project is deployed on Replit and runs both the FastAPI backend and Streamlit dashboard in a unified environment.

📌 Overview

This project provides an end-to-end system for A/B testing:

Upload experiment data (CSV)
Compute conversion metrics
Evaluate statistical significance
Generate rollout decisions
Store experiment results in a database
Visualize insights via an interactive dashboard

✨ Features
📊 CSV Upload Interface (Streamlit UI)
⚡ High-performance FastAPI backend
📈 Conversion rate & lift calculation
🧠 Automated decision engine
💾 SQLite-based experiment tracking
🔄 Async + parallel processing
🧪 Extensible statistical methods (Frequentist, Bayesian-ready)

🏗️ System Architecture
Streamlit Dashboard (Frontend)
            ↓
        FastAPI (Backend)
            ↓
   Experiment Service Layer
            ↓
   Metrics + Statistical Engine
            ↓
        SQLite Database

📂 Project Structure
ab_testing_platform/
│
├── api/                 # FastAPI routes
├── services/            # Business logic
├── core/                # Metrics, decision logic
├── stats/               # Statistical models
├── db/                  # Database layer
├── utils/               # Utilities
├── features/            # Segmentation
├── dashboard/           # Streamlit frontend
├── data/                # Sample datasets
├── scripts/             # Data scripts
│
├── ab_testing.db
├── requirements.txt
└── README.md

⚙️ Installation (Local Setup)
git clone <your-repo-url>
cd ab_testing_platform

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
▶️ Running Locally
1️⃣ Start Backend
uvicorn api.main:app --host 127.0.0.1 --port 9000
2️⃣ Start Frontend
streamlit run dashboard/app.py

📊 Input Format
group_name,converted
control,1
treatment,0

📈 Sample Output
Control Rate: 0.1204
Treatment Rate: 0.1189
Lift: -0.0015
Decision: ❌ DO NOT ROLLOUT
Business Impact: ₹ -73,979

🧠 Decision Logic

The system evaluates:

Conversion rate difference
Statistical significance
Expected business impact

🗄️ Database
SQLite used for experiment tracking
Stores experiment metrics and decisions

⚡ Performance Optimizations
Async FastAPI endpoints
Thread-based execution for heavy tasks
Efficient data processing using Pandas

🛠️ Tech Stack
Python
FastAPI
Streamlit
SQLite
Pandas / NumPy


🔮 Future Enhancements
Bayesian A/B testing
Multi-variant experiments (A/B/n)
User authentication
Experiment history dashboard
Cloud database (PostgreSQL)

👨‍💻 Author

Jagadeeswari