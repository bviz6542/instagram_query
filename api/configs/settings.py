from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRESQL_DATABASE_URL: str = "postgresql://developer:devpassword@127.0.0.1:25000/developer"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 25100

    class Config:
        case_sensitive = True

settings = Settings()