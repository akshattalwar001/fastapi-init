from pydantic import BaseModel ,Field , computed_field
from fastapi import FastAPI , Path , Query , HTTPException
from fastapi.responses import JSONResponse
from typing import Annotated , Literal , Optional
import json
app = FastAPI()
class Patient(BaseModel):
    id: Annotated[str, Field(..., description="The ID of the patient")]
    name: Annotated[str, Field(..., description="The name of the patient")]
    age: Annotated[int, Field(..., description="Age of the patient")]
    gender: Annotated[Literal["male","female", "others"], Field(..., description="Gender of the patient")]
    city : Annotated[str, Field(..., description="City of the patient")]
    weight: Annotated[float, Field(..., description="Weight in kgs")]
    height: Annotated[float, Field(..., description="Height in cms")]

    @computed_field
    @property
    def bmi(self) -> float:
        height_in_mtr = self.height / 100
        bmi = round(self.weight/(height_in_mtr**2),2)  # rounds off to 2 decimal digits
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal weight"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"
class UpdatePatient(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]


def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data
def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f)
@app.post("/create")
def create_patient(patient: Patient):

    #load existing data
    data = load_data()

    #check if id already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")
    
    # new patient data to existing data
    data[patient.id] = patient.model_dump(exclude = ['id'])

    #save data
    save_data(data)

    return JSONResponse(content={"msg": "Patient created successfully"}, status_code=201)
@app.get("/")
def home():
    return {"msg": "Patients Management system API is running"}
