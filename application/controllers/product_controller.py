from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from application.services.product_service import ProductService
from application.model import ProductItem, CategoryItem, MeasureUnitItem, UpdateCategoryItem, DeactivateCategoryItem, UpdateMeasureUnitItem, DeactivateMeasureUnitItem
from application.utils.token import get_current_user

product_router = APIRouter()
product_service = ProductService()

@product_router.get("/products")
def get_all_products(user: dict = Depends(get_current_user)):
    return product_service.get_all_products()

@product_router.post("/products", status_code=201)
def create_product(data: ProductItem, user: dict = Depends(get_current_user)):
    try:
        product = product_service.create_product(data, user)
        return JSONResponse(content={"message": "Product created successfully", "data": product}, status_code=201)
    except Exception as e:
        raise JSONResponse(content={"message": "Error creating product", "error": str(e)}, status_code=500)

@product_router.get("/products/{product_id}")
def get_product(product_id: str, user: dict = Depends(get_current_user)):
    return product_service.get_product(product_id)

@product_router.put("/products/{product_id}")
def update_product(product_id: str, update_data: ProductItem, user: dict = Depends(get_current_user)):
    try:
        updated_product = product_service.update_product(product_id, update_data, user)
        return JSONResponse(content={"message": "Product updated successfully", "data": updated_product}, status_code=200)
    except Exception as e:
        raise JSONResponse(content={"message": "Error updating product", "error": str(e)}, status_code=500)

@product_router.get("/categories")
def get_all_categories(user: dict = Depends(get_current_user)):
    return product_service.get_all_categories()

@product_router.post("/categories", status_code=201)
def create_category(data: CategoryItem, user: dict = Depends(get_current_user)):
    try:
        category = product_service.create_category(data, user)
        return JSONResponse(content={"message": "Category created successfully", "data": category}, status_code=201)
    except Exception as e:
        raise JSONResponse(content={"message": "Error creating category", "error": str(e)}, status_code=500)

@product_router.get("/categories/{category_id}")
def get_category(category_id: str, user: dict = Depends(get_current_user)):
    return product_service.get_category(category_id)

@product_router.put("/categories/{category_id}")
def update_category(category_id: str, update_data: UpdateCategoryItem, user: dict = Depends(get_current_user)):
    try:
        updated_category = product_service.update_category(category_id, update_data, user)
        return JSONResponse(content={"message": "Category updated successfully", "data": updated_category}, status_code=200)
    except Exception as e:
        raise JSONResponse(content={"message": "Error updating category", "error": str(e)}, status_code=500)

@product_router.put("/categories/{category_id}/deactivate")
def deactivate_category(category_id: str, update_data: DeactivateCategoryItem, user: dict = Depends(get_current_user)):
    try:
        deactivated_category = product_service.deactivate_category(category_id, update_data, user)
        return JSONResponse(content={"message": "Category deactivated successfully", "data": deactivated_category}, status_code=200)
    except Exception as e:
        raise JSONResponse(content={"message": "Error deactivating category", "error": str(e)}, status_code=500)

@product_router.get("/active-categories")
def get_active_categories(user: dict = Depends(get_current_user)):
    return product_service.get_active_categories()

@product_router.get("/measure-units")
def get_all_measure_units(user: dict = Depends(get_current_user)):
    return product_service.get_all_measure_units()

@product_router.post("/measure-units", status_code=201)
def create_measure_unit(data: MeasureUnitItem, user: dict = Depends(get_current_user)):
    try:
        measure_unit = product_service.create_measure_unit(data, user)
        return JSONResponse(content={"message": "Measure unit created successfully", "data": measure_unit}, status_code=201)
    except Exception as e:
        raise JSONResponse(content={"message": "Error creating measure unit", "error": str(e)}, status_code=500)

@product_router.get("/measure-units/{unit_id}")
def get_measure_unit(unit_id: str, user: dict = Depends(get_current_user)):
    return product_service.get_measure_unit(unit_id)

@product_router.put("/measure-units/{unit_id}")
def update_measure_unit(unit_id: str, update_data: UpdateMeasureUnitItem, user: dict = Depends(get_current_user)):
    try:
        updated_measure_unit = product_service.update_measure_unit(unit_id, update_data, user)
        return JSONResponse(content={"message": "Measure unit updated successfully", "data": updated_measure_unit}, status_code=200)
    except Exception as e:
        raise JSONResponse(content={"message": "Error updating measure unit", "error": str(e)}, status_code=500)

@product_router.put("/measure-units/{unit_id}/deactivate")
def deactivate_measure_unit(unit_id: str, update_data: DeactivateMeasureUnitItem, user: dict = Depends(get_current_user)):
    try:
        deactivated_unit = product_service.deactivate_measure_unit(unit_id, update_data, user)
        return JSONResponse(content={"message": "Measure unit deactivated successfully", "data": deactivated_unit}, status_code=200)
    except Exception as e:
        raise JSONResponse(content={"message": "Error deactivating measure unit", "error": str(e)}, status_code=500)

@product_router.get("/active-measure-units")
def get_active_measure_units(user: dict = Depends(get_current_user)):
    return product_service.get_active_measure_units()