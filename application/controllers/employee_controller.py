from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from application.services.employee_service import EmployeeService
from application.model import EmployeeItem
from application.utils.token import get_current_user

employee_router = APIRouter()
employee_service = EmployeeService()

@employee_router.get("/employees")
def get_all_employees(user: dict = Depends(get_current_user)):
    return employee_service.get_all_employees()

@employee_router.post("/employees", status_code=201)
def create_employee(data: EmployeeItem, user: dict = Depends(get_current_user)):
    try:
        employee = employee_service.create_employee(data, user)
        return JSONResponse(content={"message": "Employee created successfully", "data": employee}, status_code=201)
    except Exception as e:
        raise JSONResponse(content={"message": "Error creating employee", "error": str(e)}, status_code=500)

@employee_router.get("/employees/{employee_id}")
def get_employee(employee_id: str, user: dict = Depends(get_current_user)):
    return employee_service.get_employee(employee_id)

@employee_router.put("/employees/{employee_id}")
def update_employee(employee_id: str, update_data: EmployeeItem, user: dict = Depends(get_current_user)):
    try:
        updated_employee = employee_service.update_employee(employee_id, update_data, user)
        return JSONResponse(content={"message": "Employee updated successfully", "data": updated_employee}, status_code=200)
    except Exception as e:
        raise JSONResponse(content={"message": "Error updating employee", "error": str(e)}, status_code=500)