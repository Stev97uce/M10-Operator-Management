import pyodbc
from app.core.config import settings

def get_connection():
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={settings.MSSQL_SERVER};"
        f"UID={settings.MSSQL_USER};"
        f"PWD={settings.MSSQL_PASSWORD};"
        f"DATABASE={settings.MSSQL_DB}"
    )
    return pyodbc.connect(conn_str)
