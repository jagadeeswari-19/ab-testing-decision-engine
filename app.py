import streamlit as st
import numpy as np
from scipy import stats
import json
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("🚀 A/B Testing Engine (Instant Mode)")
st.markdown("⚡ Instant Analytics • Bayesian + Frequentist • Visual Insights")

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

# ---------- FORMATTING ----------
lift_pct = lift * 100

# ---------- UI ----------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Control Rate", f"{p1:.4f}")
col2.metric("Treatment Rate", f"{p2:.4f}")

col3.metric(
    "Lift",
    f"{lift_pct:.2f}%",
    delta=f"{lift_pct:.2f}%",
    delta_color="inverse"   # green if positive, red if negative
)

col4.metric("P-value", f"{p_value:.5f}")

# ---------- BAYESIAN ----------
control_samples = np.random.beta(1 + c_sum, 1 + c_n - c_sum, 5000)
treatment_samples = np.random.beta(1 + t_sum, 1 + t_n - t_sum, 5000)

prob = np.mean(treatment_samples > control_samples)
lift_samples = treatment_samples - control_samples

# ---------- DECISION ----------
if prob > 0.95 and lift > 0:
    decision = "🚀 ROLLOUT"
elif prob > 0.80:
    decision = "⚠️ TEST MORE"
else:
    decision = "❌ DO NOT ROLLOUT"

impact = lift * 1_000_000

# ---------- METRICS ----------
col1, col2, col3, col4 = st.columns(4)
col1.metric("Control Rate", f"{p1:.4f}")
col2.metric("Treatment Rate", f"{p2:.4f}")
col3.metric("Lift", f"{lift:.4f}")
col4.metric("P-value", f"{p_value:.5f}")

st.divider()

col5, col6, col7 = st.columns(3)
col5.metric("Decision", decision)
col6.metric("Impact ₹", f"{int(impact):,}")
col7.metric("Prob Treatment Better", f"{prob:.2%}")

st.divider()

# ---------- VISUALS ----------
st.subheader("📊 Visual Insights")

plt.style.use("default")

# 1️⃣ Conversion Comparison
fig1, ax1 = plt.subplots()
ax1.bar(["Control", "Treatment"], [p1, p2])
ax1.set_title("Conversion Rate Comparison")
ax1.set_ylabel("Conversion Rate")
st.pyplot(fig1)

# 2️⃣ Lift Distribution
st.subheader("📈 Bayesian Lift Distribution")

fig2, ax2 = plt.subplots()
ax2.hist(lift_samples, bins=50)
ax2.axvline(0)
ax2.set_title("Lift Distribution (Treatment - Control)")
st.pyplot(fig2)

# 3️⃣ Probability Curve
st.subheader("📉 Probability Curve")

sorted_lift = np.sort(lift_samples)
cumulative = np.arange(len(sorted_lift)) / len(sorted_lift)

fig3, ax3 = plt.subplots()
ax3.plot(sorted_lift, cumulative)
ax3.set_xlabel("Lift")
ax3.set_ylabel("Probability")
ax3.set_title("Probability Treatment is Better")
st.pyplot(fig3)

# 4️⃣ Confidence Interval
st.subheader("🎯 Confidence Interval (95%)")

fig4, ax4 = plt.subplots()
ax4.errorbar(
    x=["Lift"],
    y=[lift],
    yerr=[[lift - ci_low], [ci_high - lift]],
    fmt='o'
)
ax4.axhline(0)
ax4.set_title("Confidence Interval")
st.pyplot(fig4)

if lift > 0:
    st.success("📈 Treatment improved performance")
else:
    st.error("📉 Treatment decreased performance")