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

        existing_task = self.task_repository.get_by_title(task.title.strip())

        if existing_task:
            raise HTTPException(
                status_code=400,
                detail=f"ภารกิจ '{task.title}' มันซ้ำ! ทรงเดชไม่ปลื้ม เปลี่ยนชื่อใหม่ซะ",
            )
            
        print(f"--- [Songdej Log] กำลังสร้างภารกิจ: {task.title} ---")
        return self.task_repository.create(task)

    def mark_complete(self, task_id: int) -> Optional[schemas.Task]:
        task = self.task_repository.get_by_id(task_id)

        if task:
            task.is_completed = True
            return self.task_repository.update(task_id, task)

        return None