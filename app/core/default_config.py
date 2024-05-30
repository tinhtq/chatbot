import os
from typing import List

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

ENV: str = ""


class Configs(BaseSettings):
    # base
    ENV: str = os.getenv("ENV")
    BASEMODEL_URL: str = os.getenv("BASEMODEL_URL")

    class Config:
        case_sensitive = True


class TestConfigs(Configs):
    ENV: str = "dev"


configs = Configs()

if ENV == "prod":
    pass
elif ENV == "stage":
    pass
elif ENV == "dev":
    setting = TestConfigs()
