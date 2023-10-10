import logging

import uvicorn
from settings import settings

if __name__ == "__main__":
    # setup logs
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%Y %b %d, %H:%M",
        handlers=[
            logging.FileHandler("task_events.log"),
        ],
    )

    # run api server
    config = uvicorn.Config(
        "app:app",
        host=settings.host,
        port=int(settings.port),
        log_level="info",
    )
    server = uvicorn.Server(config)
    server.run()
