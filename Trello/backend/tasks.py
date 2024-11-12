# routers/tasks.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Task
from schemas import TaskCreate, TaskResponse
router = APIRouter()
# Для создания зависимости для сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(**task.dict())  # создаем экземпляр Task из данных Pydantic
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task  # Возвращаем экземпляр Task
@router.get("/tasks/", response_model=list[TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks  # Возвращаем список задач