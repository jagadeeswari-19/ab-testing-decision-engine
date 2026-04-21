import streamlit as st
import requests

API_URL = "http://127.0.0.1:9000"

st.set_page_config(page_title="A/B Testing Platform", layout="wide")

st.markdown(
    """
    <h1 style='text-align: center;'>🚀 A/B Testing Decision Engine</h1>
    <p style='text-align: center;'>Make data-driven rollout decisions instantly</p>
    """,
    unsafe_allow_html=True
)

st.divider()

file = st.file_uploader("📂 Upload Experiment CSV")

if file:

    files = {"file": file.getvalue()}

    if st.button("⚡ Run Analysis"):

        try:
            with st.spinner("Running analysis..."):
                res = requests.post(f"{API_URL}/analyze", files=files).json()
        except:
            st.error("🚨 API not running. Start backend first.")
            st.stop()

        if "error" in res:
            st.error(res["error"])
            st.stop()

        st.success("✅ Analysis Complete")

        # Metrics Row
        col1, col2, col3 = st.columns(3)

        col1.metric("Control Rate", f"{res['control_rate']:.4f}")
        col2.metric("Treatment Rate", f"{res['treatment_rate']:.4f}")
        col3.metric("Lift", f"{res['lift']:.4f}")

        st.divider()

        # Decision Section
        st.subheader("📌 Decision")

        if res["lift"] > 0:
            st.success(res["decision"])
        else:
            st.error(res["decision"])

        st.write(res["explanation"])

        # Chart
        st.subheader("📊 Conversion Comparison")

        st.bar_chart({
            "Control": res["control_rate"],
            "Treatment": res["treatment_rate"]
        })

        # Business Impact
        st.subheader("💰 Business Impact")

        if res["impact"] < 0:
            st.warning(f"₹ {int(res['impact']):,} loss expected")
        else:
            st.success(f"₹ {int(res['impact']):,} gain expected")

        # Confidence
        confidence = abs(res["lift"]) * 100
        st.subheader("📈 Confidence Score")
        st.progress(min(confidence / 10, 1.0))
        st.write(f"{round(confidence,2)}% confidence")