from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///ab_testing.db")

query = """
CREATE TABLE IF NOT EXISTS experiments (
    user_id INTEGER,
    group_name TEXT,
    converted INTEGER,
    device TEXT,
    country TEXT,
    timestamp TEXT
);
"""

with engine.connect() as conn:
    conn.execute(text(query))
