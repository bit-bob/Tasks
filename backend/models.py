from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class TaskModel(BaseModel):
    id: UUID
    name: str
    completed: Optional[datetime]
