from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class TaskModel(BaseModel):
    id: UUID
    name: str
    completed: Optional[str]
