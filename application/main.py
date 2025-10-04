from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Todo API",
    description="A simple Todo API using FastAPI and Appwrite",
    version="1.0.0",
    docs_url="/"
)

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from application.controllers.todo_controller import todo_router
app.include_router(todo_router, prefix="/api", tags=["Todos"])

from application.controllers.employee_controller import employee_router
app.include_router(employee_router, prefix="/api", tags=["Employees"])

from application.controllers.request_controller import request_router
app.include_router(request_router, prefix="/api", tags=["Requests"])

from application.controllers.product_controller import product_router
app.include_router(product_router, prefix="/api", tags=["Products"])