# FastAPI Todo App with Appwrite Backend

This is a Todo application built using FastAPI and Appwrite as the backend database. The application provides a RESTful API for managing todo items with full CRUD (Create, Read, Update, Delete) operations.

## Features

- Create new todo items
- Retrieve all todo items
- Get a specific todo item by ID
- Update existing todo items
- Delete todo items
- Data persistence using Appwrite database
- FastAPI automatic API documentation
- Pydantic models for data validation

## Prerequisites

- Python 3.12 or higher
- Appwrite instance running
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/gathonimburu5/APPWRITE_API.git
cd APPWRITE_API
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Configure your Appwrite credentials in the `application/configuration.py` file:
```python
APPWRITE_DATABASE_ID = "your_database_id"
APPWRITE_COLLECTION_ID = "your_collection_id"
```

## Running the Application

To start the application, run:
```bash
python run.py
```

The API will be available at `http://127.0.0.1:8030`
The interactive API documentation (Swagger UI) will be available at `http://127.0.0.1:8030/docs`

## API Endpoints

- `GET /todos` - Get all todo items
- `POST /todos` - Create a new todo item
- `GET /todos/{todo_id}` - Get a specific todo item
- `PUT /todos/{todo_id}` - Update a todo item
- `DELETE /todos/{todo_id}` - Delete a todo item

## Data Models

### TodoItem (Request Model)
```python
{
    "title": "string",
    "description": "string",
    "created_on": "string" (auto-generated if not provided)
}
```

### TodoOutput (Response Model)
```python
{
    "id": "string",
    "title": "string",
    "description": "string",
    "created_on": "datetime"
}
```

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation using Python type annotations
- [Appwrite](https://appwrite.io/) - Backend as a Service (BaaS)
- [Uvicorn](https://www.uvicorn.org/) - Lightning-fast ASGI server
- [Python-dotenv](https://pypi.org/project/python-dotenv/) - Environment variable management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).