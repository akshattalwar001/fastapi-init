from fastapi import FastAPI , Path , Query
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

@app.get("/view/{patient_id}")
def view_patient(patient_id : str  = Path(..., description="The ID of the patient to retrieve")):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return HTTPException(status_code = 404, detail="Patient not found")

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="On basis of height, weight and bmi")  ,
                   order : str = Query("asc", description ="ascending or descending")):
    
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400)
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400)
    
    data = load_data()

    sort_order = True if order =="desc" else False

    sorted_data = sorted(data.values(), key=lambda x: x.get("height" ,0) ,reverse = sort_order)

    return sorted_data
