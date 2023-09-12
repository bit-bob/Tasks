from pydantic import BaseModel
from uuid import UUID


class Task(BaseModel):
    id: UUID
    name: str
