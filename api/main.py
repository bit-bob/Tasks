import uvicorn


if __name__ == "__main__":
    config = uvicorn.Config("app:app", host="localhost", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
