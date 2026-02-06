from pydantic import BaseModel
from typing import Optional

# Base Model (Shared properties)
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Model for Creation (Input)
class TaskCreate(TaskBase):
    pass

# Model for Reading (Output - includes ID)
class Task(TaskBase):
    id: int
    # For Pydantic v2: allow constructing from arbitrary objects/ORMs
    model_config = {"from_attributes": True}


# Quick demo when run directly
if __name__ == "__main__":
    # Create a Task instance and print JSON to demonstrate the module
    task = Task(id=1, title="Example Task", description="Demo", completed=False)
    # Use Pydantic v2 API
    print(task.model_dump_json(indent=2))