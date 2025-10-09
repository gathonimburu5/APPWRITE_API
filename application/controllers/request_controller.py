from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from application.services.request_service import RequestService
from application.model import RequestHeaderItem
from application.utils.token import get_current_user

request_router = APIRouter()
request_service = RequestService()

@request_router.post("/requests", response_model=RequestHeaderItem)
async def create_request(request: RequestHeaderItem, user: dict = Depends(get_current_user)):
    result = request_service.create_request(request, user)
    if result:
        return JSONResponse(status_code=201, content={"message": "Request created successfully", "data": result})
    return JSONResponse(status_code=500, content={"message": "Error creating request"})

@request_router.get("/requests")
async def get_all_requests(user: dict = Depends(get_current_user)):
    return request_service.get_all_requests()

@request_router.get("/requests/{request_id}")
async def get_request(requestId: str, user: dict = Depends(get_current_user)):
    return request_service.get_request(requestId)