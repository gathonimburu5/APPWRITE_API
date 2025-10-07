from fastapi import APIRouter
from fastapi.responses import JSONResponse
from application.services.supplier_service import SupplierService
from application.model import SupplierItem

supplier_router = APIRouter()
supplier_service = SupplierService()

@supplier_router.get("/suppliers")
def get_all_suppliers():
    return supplier_service.get_all_suppliers()

@supplier_router.post("/suppliers", status_code=201)
def create_supplier(data: SupplierItem):
    try:
        supplier = supplier_service.create_supplier(data)
        return JSONResponse(content={"message": "Supplier created successfully", "data": supplier}, status_code=201)
    except Exception as e:
        raise JSONResponse(content={"message": "Error creating supplier", "error": str(e)}, status_code=500)

@supplier_router.get("/suppliers/{supplier_id}")
def get_supplier(supplier_id: str):
    try:
        supplier = supplier_service.get_supplier(supplier_id)
        return supplier
    except Exception as e:
        raise JSONResponse(content={"message": "Error fetching supplier", "error": str(e)}, status_code=500)

@supplier_router.put("/suppliers/{supplier_id}")
def update_supplier(supplier_id: str, update_data: SupplierItem):
    try:
        updated_supplier = supplier_service.update_supplier(supplier_id, update_data)
        return JSONResponse(content={"message": "Supplier updated successfully", "data": updated_supplier}, status_code=200)
    except Exception as e:
        raise JSONResponse(content={"message": "Error updating supplier", "error": str(e)}, status_code=500)