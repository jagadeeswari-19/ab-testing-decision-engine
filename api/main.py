from fastapi import FastAPI, UploadFile, File
import pandas as pd
import asyncio

from services.experiment_service import run_experiment

app = FastAPI()


@app.get("/")
def home():
    return {"status": "FAANG-level API running"}


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    loop = asyncio.get_event_loop()

    result = await loop.run_in_executor(
        None, run_experiment, df
    )

    return result


@app.get("/history")
def history():
    import sqlite3

    conn = sqlite3.connect("ab_testing.db")
    c = conn.cursor()

    data = c.execute("SELECT * FROM experiments").fetchall()

    return {"history": data}
API_URL = "http://127.0.0.1:8000"