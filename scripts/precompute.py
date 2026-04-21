import pandas as pd
import json

print("⚡ Precomputing metrics...")

df = pd.read_csv("data/ab_test_data.csv")

control = df[df["group"] == "control"]["converted"]
treatment = df[df["group"] == "treatment"]["converted"]

summary = {
    "control_sum": int(control.sum()),
    "control_n": int(len(control)),
    "treatment_sum": int(treatment.sum()),
    "treatment_n": int(len(treatment))
}

with open("data/summary.json", "w") as f:
    json.dump(summary, f)

print("✅ summary.json created (FAST LOAD ENABLED)")