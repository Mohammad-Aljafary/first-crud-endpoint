from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db import Task as TaskDB, SessionLocal
from sqlalchemy import select, update, delete, text




router = APIRouter()

class Task(BaseModel):
    id: int 
    title: str 
    done: bool 

class TaskCreate(BaseModel):
    title: str

db = SessionLocal()

#-------------------------
@router.get("/tasks", response_model=list[Task], description="Get all tasks")
async def read_tasks() -> list[Task]:
    tasks = db.execute(text("SELECT * FROM tasks")).mappings().all()
    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found")
    return tasks

#-------------------------
@router.get("/tasks/{task_id}", description="Get a task by ID")
async def read_task(task_id: int) -> Task:
    task = db.execute(text("SELECT * FROM tasks WHERE id = :task_id"), {"task_id": task_id}).mappings().first()
    if task is not None:
        return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

#-------------------------
@router.post("/tasks", status_code=201, description="Create a new task")
async def create_task(task: TaskCreate) -> Task:
    if task.title == None or task.title.strip() == "":
        raise HTTPException(status_code=400, detail="Task title cannot be empty")
    new_task = TaskDB(title=task.title)
    db.add(new_task)
    db.commit()
    return new_task

#-------------------------
@router.put("/tasks/{task_id}", description="Update a task by ID")
async def update_task(task_id: int, task: Task) -> Task:
    if task.title == None or task.title.strip() == "":
        raise HTTPException(status_code=400, detail="Task title cannot be empty")
    if task.done not in [True, False]:
        raise HTTPException(status_code=400, detail="Task done must be a boolean value")
    task_to_update = db.execute(
        select(TaskDB).where(TaskDB.id == task_id)
    ).scalar_one_or_none()
    if task_to_update is None:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    db.execute(
        update(TaskDB).where(TaskDB.id == task_id).values(title=task.title, done=task.done)
    )
    db.commit()
    return task_to_update

#-------------------------
@router.delete("/tasks/{task_id}", status_code=204, description="Delete a task by ID")
async def delete_task(task_id: int):
    task_to_delete = db.execute(
        select(TaskDB).where(TaskDB.id == task_id)
    ).scalar_one_or_none()
    if task_to_delete is None:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    db.execute(
        delete(TaskDB).where(TaskDB.id == task_id)
    )
    db.commit()
    return task_to_delete