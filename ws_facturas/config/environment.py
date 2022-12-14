from pydantic import BaseSettings

class Settings(BaseSettings):
    PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_SERVER: str
    DB_PORT: int
    DB_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()
