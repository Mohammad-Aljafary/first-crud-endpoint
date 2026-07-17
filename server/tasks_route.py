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
    description: str
    done: bool

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