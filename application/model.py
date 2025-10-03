from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

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

class RequestDetailsItem(BaseModel):
    #header_id: str
    product_id: int
    extra_details: str
    quantity: int
    unit_price: float
    vat_percentage: int
    vat_amount: float
    total_net: float
    
class RequestHeaderItem(BaseModel):
    request_type: str
    request_description: str
    request_status: str = Field(default="PENDING")
    request_date: datetime
    details: List[RequestDetailsItem]
    created_on: str = Field(default=datetime.utcnow().isoformat())

