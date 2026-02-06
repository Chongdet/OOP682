from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session

# ✅ Import แบบแยกไฟล์ชัดเจน
from . import models   # สำหรับ Database (models.Task)
from . import schemas  # สำหรับ Pydantic (schemas.Task, schemas.TaskCreate)

class ITaskRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[schemas.Task]:
        pass
    
    @abstractmethod
    def get_by_title(self, title: str) -> Optional[schemas.Task]:
        pass

    @abstractmethod
    def create(self, task: schemas.TaskCreate) -> schemas.Task:
        pass
        
    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[schemas.Task]:
        pass

    @abstractmethod
    def update(self, task_id: int, task: schemas.Task) -> Optional[schemas.Task]:
        pass

# -----------------------------------------------------------
# ส่วนของ InMemory (ใช้ List เก็บข้อมูลชั่วคราว)
# -----------------------------------------------------------
class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self.tasks = []
        self.current_id = 1
    
    def get_by_title(self, title: str) -> Optional[schemas.Task]:
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def get_all(self) -> List[schemas.Task]:
        return self.tasks

    def create(self, task_in: schemas.TaskCreate) -> schemas.Task:
        # แปลงจาก Input เป็น Output Schema
        task = schemas.Task(
            id=self.current_id,
            title=task_in.title,
            description=task_in.description,
            is_completed=task_in.is_completed
        )
        self.tasks.append(task)
        self.current_id += 1
        return task

    def get_by_id(self, task_id: int) -> Optional[schemas.Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update(self, task_id: int, task: schemas.Task) -> Optional[schemas.Task]:
        for i, existing_task in enumerate(self.tasks):
            if existing_task.id == task_id:
                self.tasks[i] = task
                return task
        return None

# -----------------------------------------------------------
# ส่วนของ SQL (ใช้ Database จริง)
# -----------------------------------------------------------
class SqlTaskRepository(ITaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[schemas.Task]:
        # ดึงข้อมูลจาก DB (models.Task)
        db_tasks = self.db.query(models.Task).all()
        # แปลงเป็น Pydantic (schemas.Task)
        return [schemas.Task.model_validate(task) for task in db_tasks]
    
    def get_by_title(self, title: str) -> Optional[schemas.Task]:
        db_task = self.db.query(models.Task).filter(models.Task.title == title).first()
        if db_task:
            return schemas.Task.model_validate(db_task)
        return None

    def create(self, task_in: schemas.TaskCreate) -> schemas.Task:
        # สร้าง Object ลง DB
        db_task = models.Task(
            title=task_in.title,
            description=task_in.description,
            is_completed=task_in.is_completed
        )
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return schemas.Task.model_validate(db_task)

    def get_by_id(self, task_id: int) -> Optional[schemas.Task]:
        db_task = self.db.query(models.Task).filter(models.Task.id == task_id).first()
        if db_task:
            return schemas.Task.model_validate(db_task)
        return None

    def update(self, task_id: int, task: schemas.Task) -> Optional[schemas.Task]:
        db_task = self.db.query(models.Task).filter(models.Task.id == task_id).first()
        if db_task:
            db_task.title = task.title
            db_task.description = task.description
            db_task.is_completed = task.is_completed
            self.db.commit()
            self.db.refresh(db_task)
            return schemas.Task.model_validate(db_task)
        return None