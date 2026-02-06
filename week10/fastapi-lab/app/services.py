from typing import List, Optional
from fastapi import HTTPException
from . import schemas 
from .repositories import ITaskRepository

class TaskService:
    def __init__(self, task_repository: ITaskRepository):
        self.task_repository = task_repository

    def get_tasks(self) -> List[schemas.Task]:
        return self.task_repository.get_all()

    def create_task(self, task: schemas.TaskCreate) -> schemas.Task:
        existing_task = self.task_repository.get_by_title(task.title)
        if existing_task:
            raise HTTPException(status_code=400, detail="Task with this title already exists")
            
        return self.task_repository.create(task)

    def mark_complete(self, task_id: int) -> Optional[schemas.Task]:
        # 1. หา Task เก่ามาก่อน
        task = self.task_repository.get_by_id(task_id)
        
        # 2. ถ้าเจอ ให้แก้สถานะเป็น True แล้วบันทึก
        if task:
            task.is_completed = True
            return self.task_repository.update(task_id, task)
            
        return None