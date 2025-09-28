from pydantic import BaseModel, Field
from datetime import datetime

class TodoItem(BaseModel):
    title: str
    description: str
    created_on: str = Field(default=datetime.utcnow().isoformat())

class TodoOutput(BaseModel):
    id: str
    title: str
    description: str
    created_on: datetime

    class Config:
        orm_mode = True