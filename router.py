from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from tasks import TaskList, Task
from models import TaskModel


# App
router = APIRouter(
    prefix="/api",
    tags=["tasks"],
)


# Demo tasks
def populate_demo_tasks(task_list, names):
    for name in names:
        task_list.add_task(Task(name))


demo_task_names = [
    'Create Tasks - front end - storybook components - create button',
    'Create Tasks - front end - storybook components - create form',
    'Create Tasks - back end - endpoints',
    'Create Tasks - front end - full implementation',

    'Complete Tasks - front end - storybook components - complete button',
    'Complete Tasks - front end - storybook components - task text changes',
    'Complete Tasks - front end - storybook components - move tasks to the bottom or hidden',
    'Complete Tasks - front end - storybook components - completed tasks page',
    'Complete Tasks - back end - endpoints',
    'Complete Tasks - front end - full implementation',

    'Delete Tasks - front end - storybook components - delete button',
    'Delete Tasks - back end - endpoints',
    'Delete Tasks - front end - full implementation',

    'Update Tasks - front end - storybook components - edit button',
    'Update Tasks - back end - endpoints',
    'Update Tasks - front end - full implementation',

    'Persisting Tasks',
    'Task Events',
    'Repeating Tasks',
    'Parent Tasks',
]
demo_tasks = TaskList()
populate_demo_tasks(demo_tasks, demo_task_names)


# -- Tasks --
# Read
class GetTasksResponse(BaseModel):
    tasks: List[TaskModel]


@router.get("/tasks")
async def get_tasks() -> GetTasksResponse:
    return GetTasksResponse(tasks=[TaskModel(id=t.id, name=t.name) for t in demo_tasks.get_tasks()])
