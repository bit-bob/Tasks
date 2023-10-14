import logging
from datetime import datetime
from typing import List, Optional
from uuid import UUID

from demo_tasks import demo_tasks
from fastapi import APIRouter
from models import TaskModel
from pydantic import BaseModel

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
    logging.warn(f"Creating '{request.name}'")
    demo_tasks.create_task(request.name)


# Read
class GetTasksResponse(BaseModel):
    tasks: List[TaskModel]


@router.get("/tasks")
async def get_tasks() -> GetTasksResponse:
    logging.debug(f"Getting Tasks")
    return GetTasksResponse(
        tasks=[
            TaskModel(
                id=t.id,
                name=t.name,
                created_date=t.created_date,
                completed_date=t.completed_date,
            )
            for t in demo_tasks.get_tasks()
        ],
    )


# Update
class UpdateTaskNameRequest(BaseModel):
    task_id: UUID
    name: str


@router.post("/tasks/update/name")
async def update_task_name(
    request: UpdateTaskNameRequest,
) -> None:
    task = demo_tasks.get_task(request.task_id)
    if task is None:
        raise Exception

    logging.warn(f"Updating '{task.name}' to '{request.name}'")
    task.name = request.name


class ToggleTaskCompleteRequest(BaseModel):
    task_id: UUID
    completed_date: Optional[datetime]


@router.post("/tasks/complete")
async def toggle_task_complete(
    request: ToggleTaskCompleteRequest,
) -> None:
    task = demo_tasks.get_task(request.task_id)
    if task is None:
        raise Exception

    logging.warn(
        f"Setting '{task.name}' to {'incomplete' if request.completed_date is None else 'complete'}"
    )
    task.completed_date = request.completed_date


# Delete
class DeleteTaskRequest(BaseModel):
    task_id: UUID


@router.post("/tasks/delete")
async def delete_task(
    request: DeleteTaskRequest,
) -> None:
    task = demo_tasks.get_task(request.task_id)
    if task is None:
        raise Exception

    logging.warn(f"Deleting '{task.name}'")
    demo_tasks.delete_task(request.task_id)
