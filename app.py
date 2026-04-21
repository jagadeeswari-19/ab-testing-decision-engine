import streamlit as st
import numpy as np
from scipy import stats
import json

st.set_page_config(layout="wide")

st.title("🚀 A/B Testing Engine (Instant Mode)")

# ---------- LOAD SUMMARY (SUPER FAST) ----------
@st.cache_data
def load_summary():
    with open("data/summary.json") as f:
        return json.load(f)

summary = load_summary()

c_sum = summary["control_sum"]
c_n = summary["control_n"]
t_sum = summary["treatment_sum"]
t_n = summary["treatment_n"]

# ---------- ANALYSIS ----------
p1 = c_sum / c_n
p2 = t_sum / t_n
lift = p2 - p1

p_pool = (c_sum + t_sum) / (c_n + t_n)
se = np.sqrt(p_pool * (1 - p_pool) * (1/c_n + 1/t_n))
z = lift / se
p_value = 1 - stats.norm.cdf(z)

# ---------- BAYESIAN ----------
control_samples = np.random.beta(1 + c_sum, 1 + c_n - c_sum, 5000)
treatment_samples = np.random.beta(1 + t_sum, 1 + t_n - t_sum, 5000)

prob = np.mean(treatment_samples > control_samples)

# ---------- DECISION ----------
if prob > 0.95 and lift > 0:
    decision = "🚀 ROLLOUT"
elif prob > 0.80:
    decision = "⚠️ TEST MORE"
else:
    decision = "❌ DO NOT ROLLOUT"

impact = lift * 1_000_000

# ---------- UI ----------
col1, col2, col3, col4 = st.columns(4)
col1.metric("Control", f"{p1:.4f}")
col2.metric("Treatment", f"{p2:.4f}")
col3.metric("Lift", f"{lift:.4f}")
col4.metric("P-value", f"{p_value:.5f}")

st.divider()

col5, col6, col7 = st.columns(3)
col5.metric("Decision", decision)
col6.metric("Impact ₹", f"{int(impact):,}")
col7.metric("Prob Better", f"{prob:.2%}")