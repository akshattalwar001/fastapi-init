from pydantic import BaseModel

class patient(BaseModel):
    name : str
    age  : int

patient_info = {"name" : "John Doe", "age": 30}
patient1 = patient(**patient_info) # ** is used to unpack the dictionary into keyword arguments

def get_patient_info(patient: patient):
    print(patient.name)
    print(patient.age)
get_patient_info(patient1)