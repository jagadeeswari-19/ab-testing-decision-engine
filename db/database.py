from sqlalchemy import create_engine
import pandas as pd

DATABASE_URL = "sqlite:///ab_testing.db"
engine = create_engine(DATABASE_URL)


def fetch_experiment(table_name: str):
    return pd.read_sql(f"SELECT * FROM {table_name}", engine)