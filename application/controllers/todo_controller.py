from fastapi import APIRouter
from fastapi.responses import JSONResponse
from application.services.todo_service import TodoService
from application.model import TodoItem, TodoOutput

todo_router = APIRouter()
todo_service = TodoService()

@todo_router.get("/todos")
def get_all_todos():
    try:
        todos = todo_service.get_all_todos()
        return todos
    except Exception as e:
        raise JSONResponse(content={"message": "Error fetching todos", "error": str(e)}, status_code=500)

@todo_router.post("/todos", status_code=201)
def create_todo(data: TodoItem):
    try:
        todo = todo_service.create_todo(data)
        return JSONResponse(content={"message": "Todo created successfully", "data": todo}, status_code=201)
    except Exception as e:
        raise JSONResponse(content={"message": "Error creating todo", "error": str(e)}, status_code=500)

@todo_router.get("/todos/{todo_id}")
def get_todo(todo_id: str):
    try:
        todo = todo_service.get_todo(todo_id)
        return todo
    except Exception as e:
        raise JSONResponse(content={"message": "Error fetching todo", "error": str(e)}, status_code=500)

@todo_router.put("/todos/{todo_id}")
def update_todo(todo_id: str, update_data: TodoItem):
    try:
        updated_todo = todo_service.update_todo(todo_id, update_data)
        return JSONResponse(content={"message": "Todo updated successfully", "data": updated_todo}, status_code=200)
    except Exception as e:
        raise JSONResponse(content={"message": "Error updating todo", "error": str(e)}, status_code=500)

@todo_router.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    try:
        result = todo_service.delete_todo(todo_id)
        return result
    except Exception as e:
        raise JSONResponse(content={"message": "Error deleting todo", "error": str(e)}, status_code=500)