import pandas as pd

def segment_analysis(df, segment_col):
    results = {}
    for seg in df[segment_col].dropna().unique():
        subset = df[df[segment_col] == seg]
        control = subset[subset['group']=='control']['converted']
        treatment = subset[subset['group']=='treatment']['converted']

        if len(control) > 0 and len(treatment) > 0:
            lift = treatment.mean() - control.mean()
            results[str(seg)] = round(lift, 4)

    return results