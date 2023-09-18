import uvicorn


if __name__ == "__main__":
    config = uvicorn.Config("app:app", host="localhost", port=8080, log_level="info")
    server = uvicorn.Server(config)
    server.run()
