from pydantic import BaseModel

class Address(BaseModel):

    city : str
    state : str
    pin : str
    
class Patient(BaseModel):
    name : str
    age  : int
    address : Address

address_dict = {'city': 'New York', 'state': 'NY', 'pin': '10001'}

address1 = Address(**address_dict)

patient_info = {'name':'John Doe', 'age':30, 'address': address1}

patient1 = Patient(**patient_info)

temp = patient1.model_dump()

print(temp)
print(type(temp))