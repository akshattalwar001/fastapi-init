from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator
from typing import List , Dict , Optional , Annotated

class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool
    allergies: List[str]
    contact_details :Dict[str , str]

    @field_validator('email')
    @classmethod
    def validate_age(cls , value):
        valid_domains = ['hdfc.com' , 'icici.com']
        domain_name = value.split("@")[-1]
        if domain_name not in valid_domains:
            raise ValueError('not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def validate_name(cls , value):
        return value.upper() #uppercase the name
    
    @field_validator('age' , mode='after') #mode = 'after' means its called after the default validation of converting to int
    @classmethod
    def validate_age(cls , value): 
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in 0 and 100')


def update_patient(patient : Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

patient_info = {
    'name':'Rike',
    'email':'rike@icici.com',
    'age': '30',
    'weight': 75.2,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details':{'phone':'2353462'}
    }

patient1 = Patient(**patient_info)
update_patient(patient1)
