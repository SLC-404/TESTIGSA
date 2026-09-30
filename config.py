import os
from urllib.parse import quote_plus

from dotenv import load_dotenv

load_dotenv()


def database_uri():
    if os.getenv("DATABASE_URL"):
        return os.getenv("DATABASE_URL")

    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT")
    parts = [
        f"DRIVER={{{os.getenv('DB_DRIVER', 'ODBC Driver 17 for SQL Server')}}}",
        f"SERVER={host},{port}" if port else f"SERVER={host}",
        f"DATABASE={os.getenv('DB_DATABASE', 'examen')}",
        "TrustServerCertificate=yes",
    ]
    if os.getenv("DB_USERNAME"):
        parts.append(f"UID={os.getenv('DB_USERNAME')}")
        parts.append(f"PWD={os.getenv('DB_PASSWORD', '')}")
    else:
        parts.append("Trusted_Connection=yes")
    return "mssql+pyodbc:///?odbc_connect=" + quote_plus(";".join(parts) + ";")


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or "dev"
    SQLALCHEMY_DATABASE_URI = database_uri()
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_pre_ping": True}
    APP_NAME = "Tareas"
