from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter()

class Task(BaseModel):
    id: int 
    title: str 
    done: bool 

class TaskCreate(BaseModel):
    title: str

tasks = []

#-------------------------
@router.get("/tasks", response_model=list[Task], description="Get all tasks")
async def read_tasks() -> list[Task]:
    return tasks

#-------------------------
@router.get("/tasks/{task_id}", description="Get a task by ID")
async def read_task(task_id: int) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

#-------------------------
@router.post("/tasks", status_code=201, description="Create a new task")
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

#-------------------------
@router.put("/tasks/{task_id}", description="Update a task by ID")
async def update_task(task_id: int, task: Task) -> Task:
    if task.title == None or task.title.strip() == "":
        raise HTTPException(status_code=400, detail="Task title cannot be empty")
    if task.done not in [True, False]:
        raise HTTPException(status_code=400, detail="Task done must be a boolean value")
    for i, t in enumerate(tasks):
        if t.id == task_id:
            tasks[i] = task
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

#-------------------------
@router.delete("/tasks/{task_id}", status_code=204, description="Delete a task by ID")
async def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            temp = tasks[i]
            del tasks[i]
            return temp
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")