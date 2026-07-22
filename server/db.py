import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, Column, Integer, String, Boolean, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    done = Column(Boolean, server_default=text("false"), nullable=False)

Base.metadata.create_all(bind=engine)


db = SessionLocal()

def seed_tasks():
    if db.query(Task).count() == 0:
        db.add_all([
            Task(title="Task 1"),
            Task(title="Task 2"),
            Task(title="Task 3"),
        ])
        db.commit()

seed_tasks()

db.close()
