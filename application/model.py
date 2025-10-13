from pydantic import BaseModel, Field, EmailStr, validator
from datetime import datetime, date
from typing import List, Optional

class TodoItem(BaseModel):
    title: str
    description: str
    created_on: str = Field(default=datetime.utcnow().isoformat())
    class Config:
        orm_mode = True
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
    created_by: str
    class Config:
        orm_mode = True
class RequestDetailsItem(BaseModel):
    #header_id: str
    product_id: int
    extra_details: str
    quantity: int
    unit_price: float
    vat_percentage: int
    vat_amount: float
    total_net: float
    class Config:
        orm_mode = True
class RequestHeaderItem(BaseModel):
    request_type: str
    request_description: str
    request_status: str = Field(default="PENDING")
    request_date: datetime
    details: List[RequestDetailsItem]
    created_on: str = Field(default=datetime.utcnow().isoformat())
    created_by: str
    class Config:
        orm_mode = True
class ProductItem(BaseModel):
    product_name: str
    product_description: str
    product_code: str
    product_type: str
    product_origin: str
    category_id: str
    measure_unit_id: str
    supplier_id: str
    vat_percentage: str
    quantity: int
    reoder_level: int
    date_added: str = Field(default=datetime.utcnow().isoformat())
    created_by: str
    class Config:
        orm_mode = True
class CategoryItem(BaseModel):
    category_name: str
    category_status: str = Field(default="ACTIVE")
    date_added: str = Field(default=datetime.utcnow().isoformat())
    created_by: str
    class Config:
        orm_mode = True
class MeasureUnitItem(BaseModel):
    unit_name: str
    unit_status: str = Field(default="ACTIVE")
    date_added: str = Field(default=datetime.utcnow().isoformat())
    created_by: str
    class Config:
        orm_mode = True
class AuditTrailItem(BaseModel):
    module_name: str
    action_type: str
    action_date: str = Field(default=datetime.utcnow().isoformat())
    created_by: str
    class Config:
        orm_mode = True
class UpdateCategoryItem(BaseModel):
    category_name: str
    date_added: str = Field(default=datetime.utcnow().isoformat())
    class Config:
        orm_mode = True
class DeactivateCategoryItem(BaseModel):
    category_status: str = Field(default="Inactive")
    date_added: str = Field(default=datetime.utcnow().isoformat())
    class Config:
        orm_mode = True
class UpdateMeasureUnitItem(BaseModel):
    unit_name: str
    date_added: str = Field(default=datetime.utcnow().isoformat())
    class Config:
        orm_mode = True
class DeactivateMeasureUnitItem(BaseModel):
    unit_status: str = Field(default="Inactive")
    date_added: str = Field(default=datetime.utcnow().isoformat())
    class Config:
        orm_mode = True
class SupplierItem(BaseModel):
    supplier_name: str
    supplier_code: str
    supplier_email: str
    supplier_phone: str
    postal_address: str
    physical_address: str
    dob: datetime
    supplier_status: str = Field(default="ACTIVE")
    date_added: str = Field(default=datetime.utcnow().isoformat())
    created_by: str
    class Config:
        orm_mode = True
class SupplierStatusItem(BaseModel):
    supplier_status: str
    class Config:
        orm_mode = True
class RegisterUserItem(BaseModel):
    full_name: str
    email_address: EmailStr
    username: str
    password: str
    confirm_password: str
    phone_number: str
    dob: date
    profile: Optional[str] = None    #= Field(default="upload/profile.png")
    date_added: str = Field(default=datetime.utcnow().isoformat())
    created_by: str
    @validator("confirm_password")
    def password_match(cls, v, values):
        if "password" in values and v != values["password"]:
            raise ValueError("password does not match")
        return v
    class Config:
        orm_mode = True
class UserLoginItem(BaseModel):
    username: str
    password: str
    class Config:
        orm_mode = True
class UserTokenItem(BaseModel):
    id: str
    access_token: str
    token_type: str
    full_name: str
    email_address: str
    phone_number: str
    username: str
    class Config:
        orm_mode = True
class UpdateUserItem(BaseModel):
    full_name: str
    email_address: str
    phone_number: str
    profile: Optional[str] = None
    class Config:
        orm_mode = True
class ChangePassword(BaseModel):
    old_password: str
    new_password: str
    confirm_password: str
    @validator("confirm_password")
    def password_match(cls, v, values):
        if "new_password" in values and v != values["new_password"]:
            raise ValueError("password does not match")
        return v
    class Config:
        orm_mode = True

