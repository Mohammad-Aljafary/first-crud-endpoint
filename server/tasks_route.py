from fastapi import APIRouter


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_tasks():
    return {"message": "Hello from tasks route!"}