from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
from router import router
from fastapi.middleware.cors import CORSMiddleware

# App
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #TODO: Configurable
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include the router to the app
# n.b. needs to be after the routes are added but before the static front end
# is mounted for the docs site to work
app.include_router(router)


# Static Front End
# app.mount("/", StaticFiles(directory="dist", html=True), name="static")


def use_route_names_as_operation_ids(app: FastAPI):
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name


use_route_names_as_operation_ids(app)
