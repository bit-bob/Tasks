from fastapi import FastAPI, APIRouter
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles

from tasks import TaskList


# Create the app
app = FastAPI()
router = APIRouter(
    prefix="/api",
    tags=["tasks"],
)

tasks = TaskList()
tasks.add_task('Demo task from the backend')


# -- Tasks --
# Read
@router.get("/tasks")
async def get_tasks():
    return [t.name for t in tasks.get_tasks()]


# Include the router to the app
# n.b. needs to be after the routes are added but before the static front end
# is mounted for the docs site to work
app.include_router(router)


# Static Front End
app.mount("/", StaticFiles(directory="dist", html=True), name="static")


def use_route_names_as_operation_ids(app: FastAPI):
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name


use_route_names_as_operation_ids(app)
