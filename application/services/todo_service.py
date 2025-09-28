from application.configuration import client, database, APPWRITE_DATABASE_ID, APPWRITE_COLLECTION_ID
from application.model import TodoItem, TodoOutput
import secrets

class TodoService:
    def __init__(self):
        self.database = database
        self.database_id = APPWRITE_DATABASE_ID
        self.collection_id = APPWRITE_COLLECTION_ID

    def get_all_todos(self):
        todos = self.database.list_documents(
            database_id=self.database_id,
            collection_id=self.collection_id
        )
        return todos

    def create_todo(self, data: TodoItem):
        todo = self.database.create_document(
            database_id=self.database_id,
            collection_id=self.collection_id,
            document_id=secrets.token_hex(16),
            data =  {
                "title": data.title,
                "description": data.description,
                "created_on": data.created_on
            }
        )
        return todo

    def get_todo(self, todo_id):
        todo = self.database.get_document(
            database_id=self.database_id,
            collection_id=self.collection_id,
            document_id=todo_id
        )
        return todo

    def update_todo(self, todo_id, data: TodoItem):
        updated_todo = self.database.update_document(
            database_id=self.database_id,
            collection_id=self.collection_id,
            document_id=todo_id,
            data= {
                "title": data.title,
                "description": data.description
            }
        )
        return updated_todo

    def delete_todo(self, todo_id):
        self.database.delete_document(
            database_id=self.database_id,
            collection_id=self.collection_id,
            document_id=todo_id
        )
        return {"message": "Todo deleted successfully"}