from os import getenv

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


class Settings:
    DB_URL = f"postgresql://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}/{getenv('DB_NAME')}"


settings = Settings()
