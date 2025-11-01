import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    if not SECRET_KEY:
        raise RuntimeError("SECRET_KEY is missing in the environment.")

    db_url = os.getenv("DATABASE_URL")
    if db_url and db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql+psycopg2://")

    SQLALCHEMY_DATABASE_URI = db_url or "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
