from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class TaskModel(BaseModel):
    id: UUID
    name: str
    created_date: Optional[datetime]
    completed_date: Optional[datetime]
