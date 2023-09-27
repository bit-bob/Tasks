import os


class Settings:
    host: str = os.getenv("HOST", default="127.0.0.1")
    port: str = os.getenv("PORT", default="8000")


settings = Settings()
