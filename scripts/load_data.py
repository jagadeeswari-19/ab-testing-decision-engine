import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///ab_testing.db")

df = pd.read_csv("data/ab_test_data.csv")
df.rename(columns={"group":"group_name"}, inplace=True)
df.to_sql("experiments", engine, if_exists="replace", index=False)