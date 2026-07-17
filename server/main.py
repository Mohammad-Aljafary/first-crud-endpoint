from fastapi import FastAPI
from tasks_route import router

app = FastAPI(
    title="Task Management API",
    description="A simple API for managing tasks",
    version="1.0.0",
)

app.include_router(router)

@app.get("/", description="Root endpoint")
async def root():
    return {"message": "Hello from FastAPI!"}

@app.get("/health", description="Health check endpoint")
async def health_check():
    return {"status": "ok"}
