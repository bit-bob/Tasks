from datetime import datetime
from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter
from pydantic import BaseModel

from models import TaskModel
from tasks import Task, TaskList

# App
router = APIRouter(
    prefix="/api",
    tags=["tasks"],
)


# Demo tasks
def populate_demo_tasks(task_list, info):
    for name, completed in info:
        task_list.add_task(Task(
            name=name,
            completed=completed,
        ))


demo_task_info = [
    ('Create Tasks - front end - storybook components - create button', None),
    ('Create Tasks - front end - storybook components - create form', None),
    ('Create Tasks - back end - endpoints', None),
    ('Create Tasks - front end - full implementation', None),

    ('Complete Tasks - front end - storybook components - complete button',
     "2023-09-13T12:59:05Z"),
    ('Complete Tasks - front end - storybook components - task text changes', None),
    ('Complete Tasks - front end - storybook components - move tasks to the bottom or hidden', None),
    ('Complete Tasks - front end - storybook components - completed tasks page', None),
    ('Complete Tasks - back end - endpoints', None),
    ('Complete Tasks - front end - full implementation - toggle complete button',
     "2023-09-13T14:38Z"),
    ('Complete Tasks - front end - full implementation - make text more faint when complete', None),
    ('Complete Tasks - front end - full implementation - move completed tasks to the bottom of the page', None),

    ('Delete Tasks - front end - storybook components - delete button', None),
    ('Delete Tasks - back end - endpoints', None),
    ('Delete Tasks - front end - full implementation', None),

    ('Update Tasks - front end - storybook components - edit button', None),
    ('Update Tasks - back end - endpoints', None),
    ('Update Tasks - front end - full implementation', None),

    ('Persisting Tasks', None),
    ('Task Events', None),
    ('Repeating Tasks', None),
    ('Parent Tasks', None),
]
demo_tasks = TaskList()
populate_demo_tasks(demo_tasks, demo_task_info)


# -- Tasks --
# Read
class GetTasksResponse(BaseModel):
    tasks: List[TaskModel]


@router.get("/tasks")
async def get_tasks() -> GetTasksResponse:
    return GetTasksResponse(
        tasks=[TaskModel(
            id=t.id,
            name=t.name,
            completed=t.completed,
        ) for t in demo_tasks.get_tasks()],
    )


# Update
class ToggleTaskCompleteRequest(BaseModel):
    task_id: UUID
    completed: Optional[datetime]


@router.post("/tasks/complete")
async def toggle_task_complete(
    request: ToggleTaskCompleteRequest,
) -> None:
    task = demo_tasks.get_task(request.task_id)
    if task is None:
        raise Exception
    task.completed = request.completed
