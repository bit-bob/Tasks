import uvicorn
from tasks import Task


tasks = [Task('test')]


if __name__ == "__main__":
    config = uvicorn.Config("app:app", port=3000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
