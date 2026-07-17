from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)

class Task(BaseModel):
    id: int 
    title: str 
    done: bool 

class TaskCreate(BaseModel):
    title: str

tasks = []


@router.get("/")
async def read_tasks() -> list[Task]:
    return tasks

@router.get("/{task_id}")
async def read_task(task_id: int) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@router.post("/", status_code=201)
async def create_task(task: TaskCreate) -> Task:
    if task.title == None or task.title.strip() == "":
        raise HTTPException(status_code=400, detail="Task title cannot be empty")
    new_task = Task(
        id=len(tasks) + 1,
        title=task.title,
        done=False
    )
    tasks.append(new_task)
    return new_task