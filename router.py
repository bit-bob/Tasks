from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from tasks import TaskList
from models import TaskModel


# App
router = APIRouter(
    prefix="/api",
    tags=["tasks"],
)


# Demo tasks
demo_tasks = TaskList()
demo_tasks.add_task('Create Tasks - front end - storybook components - create button')
demo_tasks.add_task('Create Tasks - front end - storybook components - create form')
demo_tasks.add_task('Create Tasks - back end - endpoints')
demo_tasks.add_task('Create Tasks - front end - full implementation')

demo_tasks.add_task('Complete Tasks - front end - storybook components - complete button')
demo_tasks.add_task('Complete Tasks - front end - storybook components - task text changes')
demo_tasks.add_task('Complete Tasks - front end - storybook components - move tasks to the bottom or hidden')
demo_tasks.add_task('Complete Tasks - front end - storybook components - completed tasks page')
demo_tasks.add_task('Complete Tasks - back end - endpoints')
demo_tasks.add_task('Complete Tasks - front end - full implementation')

demo_tasks.add_task('Delete Tasks - front end - storybook components - delete button')
demo_tasks.add_task('Delete Tasks - back end - endpoints')
demo_tasks.add_task('Delete Tasks - front end - full implementation')

demo_tasks.add_task('Update Tasks - front end - storybook components - edit button')
demo_tasks.add_task('Update Tasks - back end - endpoints')
demo_tasks.add_task('Update Tasks - front end - full implementation')

demo_tasks.add_task('Persisting Tasks')
demo_tasks.add_task('Task Events')
demo_tasks.add_task('Repeating Tasks')
demo_tasks.add_task('Parent Tasks')

# -- Tasks --
# Read
class GetTasksResponse(BaseModel):
    tasks: List[TaskModel]


@router.get("/tasks")
async def get_tasks() -> GetTasksResponse:
    return GetTasksResponse(tasks=[TaskModel(id=t.id, name=t.name) for t in demo_tasks.get_tasks()])
