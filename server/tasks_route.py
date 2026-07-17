from fastapi import APIRouter


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_tasks():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"],
    }