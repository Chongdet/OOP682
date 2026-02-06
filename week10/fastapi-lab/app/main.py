from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import models, schemas  
from .repositories import SqlTaskRepository
from .services import TaskService


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_task_service(db: Session = Depends(get_db)):
    repo = SqlTaskRepository(db)
    return TaskService(repo)

# GET: ใช้ schemas.Task (Pydantic)
@app.get("/tasks", response_model=List[schemas.Task])
def read_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_tasks()

# POST: รับ schemas.TaskCreate, ส่งกลับ schemas.Task
@app.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, service: TaskService = Depends(get_task_service)):
    return service.create_task(task)

# PUT: ใช้ schemas.Task
@app.put("/tasks/{task_id}/complete", response_model=schemas.Task)
def mark_task_complete(task_id: int, service: TaskService = Depends(get_task_service)):
    result = service.mark_complete(task_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return result