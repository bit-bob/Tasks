from fastapi import APIRouter

from tasks import TaskList


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
@router.get("/tasks")
async def get_tasks():
    return [t.name for t in demo_tasks.get_tasks()]
