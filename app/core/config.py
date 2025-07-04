import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_PORT = int(os.getenv("APP_PORT", 8001))
    MSSQL_SERVER = os.getenv("MSSQL_SERVER")
    MSSQL_USER = os.getenv("MSSQL_USER")
    MSSQL_PASSWORD = os.getenv("MSSQL_PASSWORD")
    MSSQL_DB = os.getenv("MSSQL_DB")
    AUTH_SERVICE = os.getenv("AUTH_SERVICE")
    USER_SERVICE = os.getenv("USER_SERVICE")

settings = Settings()
