from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session as SQLASession
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True, future=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()

def get_db() -> SQLASession: # type: ignore
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
