from typing import List, Dict
from pydantic import BaseModel


class TasksResponse(BaseModel):
    tasks: List[Dict]
