from fastapi import FastAPI , From
from typing import Annotated
from schema.User import User
app = FastAPI()

@app.get("/signin")
def signin(data: Annotated[User, From()]):
    return data

@app.post("/signup")
async def create_user():
    return {"status": "User created"}

@app.get("/tasks")
async def get_tasks():
    return {"tasks": []}

@app.post("/tasks")
async def create_task():
    return {"status": "Task created"}

@app.put("/tasks/{task_id}")
async def update_task(task_id: int):
    return {"status": f"Task {task_id} updated"}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    return {"status": f"Task {task_id} deleted"}