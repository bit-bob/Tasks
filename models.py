from pydantic import BaseModel
from uuid import UUID


class TaskModel(BaseModel):
    id: UUID
    name: str
