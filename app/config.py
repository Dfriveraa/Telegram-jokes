from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    TOKEN: str = Field(...)


settings = Settings()
