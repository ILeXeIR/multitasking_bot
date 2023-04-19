from pydantic import BaseSettings


class Settings(BaseSettings):

    TG_BOT_TOKEN: str
    WEATHER_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
