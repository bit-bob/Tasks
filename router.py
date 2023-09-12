from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from tasks import TaskList
from models import Task


# App
router = APIRouter(
    prefix="/api",
    tags=["tasks"],
)


# Demo tasks
demo_tasks = TaskList()
demo_tasks.add_task('Demo task from the backend')


# -- Tasks --
# Read
class GetTasksResponse(BaseModel):
    tasks: List[Task]


@router.get("/tasks")
async def get_tasks() -> GetTasksResponse:
    return GetTasksResponse(tasks=[Task(name=t.name) for t in demo_tasks.get_tasks()])
