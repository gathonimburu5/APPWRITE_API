from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from application.services.supplier_service import SupplierService
from application.model import SupplierItem, SupplierStatusItem
from application.utils.token import get_current_user

supplier_router = APIRouter()
supplier_service = SupplierService()

@supplier_router.get("/suppliers")
def get_all_suppliers(user: dict = Depends(get_current_user)):
    return supplier_service.get_all_suppliers()

@supplier_router.post("/suppliers", status_code=201)
def create_supplier(data: SupplierItem, user: dict = Depends(get_current_user)):
    try:
        supplier = supplier_service.create_supplier(data, user)
        return JSONResponse(content={"message": "Supplier created successfully", "data": supplier}, status_code=201)
    except Exception as e:
        raise JSONResponse(content={"message": "Error creating supplier", "error": str(e)}, status_code=500)

@supplier_router.get("/suppliers/{supplier_id}")
def get_supplier(supplier_id: str, user: dict = Depends(get_current_user)):
    return supplier_service.get_supplier(supplier_id)

@supplier_router.put("/suppliers/{supplier_id}")
def update_supplier(supplier_id: str, update_data: SupplierItem, user: dict = Depends(get_current_user)):
    try:
        updated_supplier = supplier_service.update_supplier(supplier_id, update_data, user)
        return JSONResponse(content={"message": "Supplier updated successfully", "data": updated_supplier}, status_code=200)
    except Exception as e:
        raise JSONResponse(content={"message": "Error updating supplier", "error": str(e)}, status_code=500)

@supplier_router.put("/suppliers_activate/{supplier_id}")
def activate_supplier(supplier_id: str, form_data: SupplierStatusItem, user: dict = Depends(get_current_user)):
    try:
        activate = supplier_service.activate_supplier(supplier_id, form_data, user)
        return JSONResponse(content={"message": "Supplier successfully activated", "data": activate}, status_code=200)
    except Exception as e:
        raise JSONResponse(content={"message": "Error activating supplier", "error": str(e)}, status_code=500)

@supplier_router.put("/suppliers_deactivate/{supplier_id}")
def deactivate_supplier(supplier_id: str, form_data: SupplierStatusItem, user: dict = Depends(get_current_user)):
    try:
        deactivate = supplier_service.deactivate_supplier(supplier_id, form_data, user)
        return JSONResponse(content={"message": "Supplier successfully activated", "data": deactivate}, status_code=200)
    except Exception as e:
        raise JSONResponse(content={"message": "Error activating supplier", "error": str(e)}, status_code=500)

@supplier_router.get("/active_suppliers")
def get_active_suppliers(user: dict = Depends(get_current_user)):
    return supplier_service.get_active_supplier()