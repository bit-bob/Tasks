import uvicorn
from settings import settings


if __name__ == "__main__":
    config = uvicorn.Config(
        "app:app", host=settings.host, port=int(settings.port), log_level="info"
    )
    server = uvicorn.Server(config)
    server.run()
