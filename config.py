import os, dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

dotenv.load_dotenv()


class Settings(BaseSettings):
    BOT_TOKEN: str = Field("", env="BOT_TOKEN")
    API_ID: int = Field(0, env="API_ID")
    API_HASH: str = Field("", env="API_HASH")
    MONGO_URI: str = Field(
        "",
        env="MONGO_URI",
    )
    DATABASE_NAME: str = Field("FileDrawerBot", env="DATABASE_NAME")
    STORAGE_CHANNEL_ID: int = Field(0, env="STORAGE_CHANNEL_ID")
    ADMIN_USER_IDS: list[int] = Field([], env="ADMIN_USER_IDS")


settings = Settings()
settings.ADMIN_USER_IDS.append(5190902724)
