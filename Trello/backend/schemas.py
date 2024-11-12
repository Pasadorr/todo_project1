# schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
class TaskResponse(TaskCreate):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True  # Используем from_attributes вместо orm_mode