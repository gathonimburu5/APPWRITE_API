from fastapi import APIRouter
from fastapi.responses import JSONResponse
from application.services.request_service import RequestService
from application.model import RequestHeaderItem

request_router = APIRouter()
request_service = RequestService()

@request_router.post("/requests", response_model=RequestHeaderItem)
async def create_request(request: RequestHeaderItem):
    result = request_service.create_request(request)
    if result:
        return JSONResponse(status_code=201, content={"message": "Request created successfully", "data": result})
    return JSONResponse(status_code=500, content={"message": "Error creating request"})

@request_router.get("/requests")
async def get_all_requests():
    return request_service.get_all_requests()