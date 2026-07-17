from fastapi import FastAPI
from tasks_route import router

app = FastAPI()

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello World!"}

