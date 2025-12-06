from fastapi import FastAPI
import json
app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
def home():
    return {"msg": "Patients Management system API is running"}

@app.get("/about")
def about():
    return {"msg": "API to mangage patients records"}

@app.get("/view")
def view():
    data = load_data()
    return data