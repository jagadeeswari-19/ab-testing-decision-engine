import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

st.set_page_config(page_title="A/B Testing Engine", layout="wide")

st.title("🚀 Advanced A/B Testing Decision Engine")
st.markdown("Fast • Scalable • Bayesian + Frequentist Analysis")

# ---------- FAST DATA LOADING ----------
@st.cache_data
def load_data(file):
    return pd.read_csv(
        file,
        dtype={"group": "category", "converted": "int8"}
    )

# ---------- FREQUENTIST ----------
def frequentist_analysis(control, treatment):
    n1, n2 = len(control), len(treatment)
    p1, p2 = control.mean(), treatment.mean()

    lift = p2 - p1
    p_pool = (control.sum() + treatment.sum()) / (n1 + n2)

    se = np.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))
    z = (p2 - p1) / se
    p_value = 1 - stats.norm.cdf(z)

    ci_low = lift - 1.96 * se
    ci_high = lift + 1.96 * se

    return p1, p2, lift, p_value, ci_low, ci_high

# ---------- BAYESIAN ----------
@st.cache_data
def bayesian_analysis(control_sum, control_n, treatment_sum, treatment_n, samples=10000):
    alpha_c = 1 + control_sum
    beta_c = 1 + control_n - control_sum

    alpha_t = 1 + treatment_sum
    beta_t = 1 + treatment_n - treatment_sum

    control_samples = np.random.beta(alpha_c, beta_c, samples)
    treatment_samples = np.random.beta(alpha_t, beta_t, samples)

    prob_treatment_better = np.mean(treatment_samples > control_samples)
    lift_samples = treatment_samples - control_samples

    return prob_treatment_better, lift_samples

# ---------- MAIN ----------
uploaded_file = st.file_uploader("📂 Upload CSV", type=["csv"])

if uploaded_file:
    st.write(f"📦 File size: {round(len(uploaded_file.getvalue())/1e6,2)} MB")

    with st.spinner("⏳ Processing dataset..."):
        df = load_data(uploaded_file)

    if not {"group", "converted"}.issubset(df.columns):
        st.error("❌ CSV must contain 'group' and 'converted'")
    else:
        control = df[df["group"] == "control"]["converted"]
        treatment = df[df["group"] == "treatment"]["converted"]

        # Frequentist
        p1, p2, lift, p_value, ci_low, ci_high = frequentist_analysis(control, treatment)

        # Bayesian (optimized)
        prob_better, lift_samples = bayesian_analysis(
            control.sum(), len(control),
            treatment.sum(), len(treatment)
        )

        # Decision logic
        if prob_better > 0.95 and lift > 0:
            decision = "🚀 STRONG ROLLOUT"
        elif prob_better > 0.80:
            decision = "⚠️ TEST LONGER"
        else:
            decision = "❌ DO NOT ROLLOUT"

        impact = lift * 1_000_000

        st.success("✅ Analysis Complete")

        # ---------- METRICS ----------
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Control Rate", f"{p1:.4f}")
        col2.metric("Treatment Rate", f"{p2:.4f}")
        col3.metric("Lift", f"{lift:.4f}")
        col4.metric("P-Value", f"{p_value:.5f}")

        st.divider()

        col5, col6, col7 = st.columns(3)
        col5.metric("Decision", decision)
        col6.metric("Business Impact (₹)", f"{int(impact):,}")
        col7.metric("Prob Treatment Better", f"{prob_better:.2%}")

        st.divider()

        # ---------- CONFIDENCE INTERVAL ----------
        st.subheader("📊 Confidence Interval (95%)")
        st.write(f"Lower: {ci_low:.4f} | Upper: {ci_high:.4f}")

        # ---------- BAR CHART ----------
        st.subheader("📈 Conversion Comparison")
        fig1, ax1 = plt.subplots()
        ax1.bar(["Control", "Treatment"], [p1, p2])
        ax1.set_ylabel("Conversion Rate")
        st.pyplot(fig1)

        # ---------- LIFT DISTRIBUTION ----------
        st.subheader("📊 Lift Distribution (Bayesian)")
        fig2, ax2 = plt.subplots()
        ax2.hist(lift_samples, bins=50)
        ax2.axvline(0)
        ax2.set_title("Lift Distribution")
        st.pyplot(fig2)

        # ---------- PROBABILITY CURVE ----------
        st.subheader("📈 Probability Curve")
        sorted_lift = np.sort(lift_samples)
        cumulative = np.arange(len(sorted_lift)) / len(sorted_lift)

        fig3, ax3 = plt.subplots()
        ax3.plot(sorted_lift, cumulative)
        ax3.set_xlabel("Lift")
        ax3.set_ylabel("Probability")
        st.pyplot(fig3)

        # ---------- SAMPLE SIZE ----------
        st.subheader("📦 Sample Size")
        st.write(f"Control: {len(control)}")
        st.write(f"Treatment: {len(treatment)}")

        # ---------- DATA PREVIEW ----------
        st.subheader("🔍 Data Preview")
        st.dataframe(df.head(100))

else:
    st.info("Upload a CSV to start analysis.")