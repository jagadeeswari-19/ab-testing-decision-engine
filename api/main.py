from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/results")
def get_results():
    with open("data/summary.json") as f:
        data = json.load(f)
    return data