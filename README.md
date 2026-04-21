🚀 A/B Testing Decision Engine

🔗 Live App: https://ab-testing-decision-engine-qd7pmbjgckxdcj9qkr7o6w.streamlit.app/

A production-grade A/B testing platform that delivers instant statistical decisions (0.1s) using both Frequentist and Bayesian methods, along with business impact estimation.

📌 Problem Statement

Modern experimentation platforms are:

⏳ Slow (large CSV processing)
📊 Hard to interpret (statistical outputs only)
❌ Lack decision clarity

This system solves that by providing:

✅ Instant insights
✅ Clear rollout decisions
✅ Business-focused metrics

⚡ Key Features

🧠 Dual Statistical Engine
Frequentist: Z-test, p-value, confidence intervals
Bayesian: Probability treatment is better

⚡ Ultra-Fast Processing (FAANG-style optimization)
Precomputed aggregates (summary.json)
No runtime CSV parsing
~0.1 sec response time

📊 Advanced Visualizations
Conversion rate comparison
Lift distribution (Bayesian)
Probability curves
Confidence intervals

💼 Business Impact Engine
Converts lift → revenue impact
Example:
Lift: -0.0015 → ₹ -73,979 loss

🎯 Smart Decision System
if prob > 0.95 → 🚀 ROLLOUT  
elif prob > 0.80 → ⚠️ TEST MORE  
else → ❌ DO NOT ROLLOUT

🏗️ Architecture
                ┌───────────────┐
                │  Streamlit UI │
                └──────┬────────┘
                       │
                       ▼
           ┌──────────────────────┐
           │ Precomputed Summary  │  (JSON)
           └──────────────────────┘
                       │
                       ▼
        ┌───────────────────────────┐
        │ Statistical Engine        │
        │ - Z-test                 │
        │ - Bayesian inference     │
        └───────────────────────────┘
                       │
                       ▼
             ┌────────────────┐
             │ Decision Layer │
             └────────────────┘


📂 Project Structure
ab_testing_platform/
│
├── app.py                # Streamlit dashboard (main app)
├── requirements.txt
├── README.md
│
├── data/
│   └── summary.json      # Precomputed metrics (fast load)
│
├── scripts/
│   └── precompute.py     # Converts CSV → summary.json
│
├── api/                  # (Optional FastAPI backend)
├── services/
├── db/


⚙️ How It Works
Step 1: Precompute (offline)
python scripts/precompute.py
Step 2: Run App
streamlit run app.py


📊 Example Output
Metric	Value
Control Rate	0.1204
Treatment Rate	0.1189
Lift	-0.0015
Decision	❌ DO NOT ROLLOUT
Impact	₹ -73,979


🚀 Deployment

Deployed using Streamlit Cloud

Steps:
Push code to GitHub
Connect repo to Streamlit
Set entry file: app.py


🧠 Technical Highlights
Performance Optimization
Eliminated CSV bottleneck
Cached JSON loading
Vectorized NumPy operations
Statistical Rigor
Pooled standard error
Z-score hypothesis testing
Bayesian posterior sampling
Scalability Design
Decoupled data processing (precompute.py)
Stateless UI layer
Ready for API integration


📈 Future Improvements (FAANG-level roadmap)
Real-time experiment tracking (Kafka / streaming)
Multi-variant testing (A/B/n)
Sequential testing (early stopping)
Experiment history dashboard
User segmentation analysis


🏆 Why This Project Stands Out

This project demonstrates:

⚡ Performance engineering
📊 Statistical depth
🧠 Product thinking
💼 Business impact awareness
🎯 Decision-driven design


👩‍💻 Author

Jagadeeswari
