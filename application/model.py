from pydantic import BaseModel, Field
from datetime import datetime

class TodoItem(BaseModel):
    title: str
    description: str
    created_on: str = Field(default=datetime.utcnow().isoformat())

class TodoOutput(BaseModel):
    id: str
    title: str
    description: str
    created_on: datetime

    class Config:
        orm_mode = True

class EmployeeItem(BaseModel):
    employee_name: str
    employee_email: str
    phone_number: str
    postal_address: str
    physical_address: str
    department: str
    gender: str
    kra_pin: str
    date_birth: datetime
    created_on: str = Field(default=datetime.utcnow().isoformat())