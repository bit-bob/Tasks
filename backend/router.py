from datetime import datetime
from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter
from pydantic import BaseModel

from models import TaskModel
from demo_tasks import demo_tasks
import logging


# App
router = APIRouter(
    prefix="",
    tags=["tasks"],
)


# -- Tasks --
# Create
class CreateTaskRequest(BaseModel):
    name: str


@router.post("/tasks/create")
async def create_task(
    request: CreateTaskRequest,
) -> None:
    logging.warn(f"\n\n ==== \n Creating Task with name = '{request.name}\n ==== \n")
    demo_tasks.create_task(request.name)


# Read
class GetTasksResponse(BaseModel):
    tasks: List[TaskModel]


@router.get("/tasks")
async def get_tasks() -> GetTasksResponse:
    logging.debug(f" == Get Tasks == ")
    return GetTasksResponse(
        tasks=[
            TaskModel(
                id=t.id,
                name=t.name,
                completed=t.completed,
            )
            for t in demo_tasks.get_tasks()
        ],
    )


# Update
class UpdateTaskRequest(BaseModel):
    task_id: UUID
    name: str


@router.post("/tasks/update")
async def update_task(
    request: UpdateTaskRequest,
) -> None:
    task = demo_tasks.get_task(request.task_id)
    if task is None:
        raise Exception
    logging.warn(
        f"\n\n ==== \n Updating Task with task_id={request.task_id}\n * old name = '{task.name}'\n * new name = '{request.name}'\n ==== \n"
    )
    task.name = request.name


class ToggleTaskCompleteRequest(BaseModel):
    task_id: UUID
    completed: Optional[datetime]


@router.post("/tasks/complete")
async def toggle_task_complete(
    request: ToggleTaskCompleteRequest,
) -> None:
    logging.warn(
        f"\n\n ==== \n Setting Task with task_id={request.task_id} to {'incomplete' if request.completed is None else 'complete'}\n ==== \n"
    )
    task = demo_tasks.get_task(request.task_id)
    if task is None:
        raise Exception
    task.completed = request.completed


# Delete
class DeleteTaskRequest(BaseModel):
    task_id: UUID


@router.post("/tasks/delete")
async def delete_task(
    request: DeleteTaskRequest,
) -> None:
    logging.warn(f"\n\n ==== \n Deleting Task with task_id={request.task_id}\n ==== \n")
    demo_tasks.delete_task(request.task_id)
