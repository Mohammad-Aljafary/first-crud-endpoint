from fastapi import FastAPI
from tasks_route import router

app = FastAPI()

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}
    
@app.get("/health")
async def health_check():
    return {"status": "ok"}
