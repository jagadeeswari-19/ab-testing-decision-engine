import sqlite3

DB_NAME = "ab_testing.db"

def save_experiment(result):

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS experiments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        control_rate REAL,
        treatment_rate REAL,
        lift REAL,
        impact REAL,
        decision TEXT
    )
    """)

    c.execute(
        """INSERT INTO experiments 
        (control_rate, treatment_rate, lift, impact, decision)
        VALUES (?, ?, ?, ?, ?)""",
        (
            result["control_rate"],
            result["treatment_rate"],
            result["lift"],
            result["impact"],
            result["decision"]
        )
    )

    conn.commit()
    conn.close()