from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from main import tasks


# Create the app
app = FastAPI()


@app.get("/api/tasks")
async def get_tasks():
    return tasks


app.mount("/", StaticFiles(directory="dist", html=True), name="static")
