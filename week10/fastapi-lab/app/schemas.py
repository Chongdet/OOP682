# 📂 app/schemas.py
from pydantic import BaseModel
from typing import Optional

# 1. Base Schema (แม่แบบ)
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False

# 2. Input Schema (ตอนสร้าง Task)
class TaskCreate(TaskBase):
    pass

# 3. Output Schema (ตอนส่งข้อมูลกลับไปหน้าเว็บ)
class Task(TaskBase):
    id: int
    
    # คำสั่งนี้บอกให้ Pydantic อ่านข้อมูลจาก Database Model ได้
    class Config:
        from_attributes = True