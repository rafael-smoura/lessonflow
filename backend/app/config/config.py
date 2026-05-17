import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

    # If DATABASE_URL exists (cloud/docker), use it. 
    # Otherwise, fall back to the default local SQLite database.
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///lessonflow.db")

    # Fix required by newer SQLAlchemy versions for cloud platforms like Render
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_TRACK_MODIFICATIONS = False