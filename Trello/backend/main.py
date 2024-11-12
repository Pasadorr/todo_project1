from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Модель доски
class Board(BaseModel):
    name: str

# Список созданных досок
boards = []

@app.post("/boards/", response_model=Board)
def create_board(board: Board):
    boards.append(board)
    return board

# Подключение статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

# Корневая страница
@app.get("/")
def read_root():
    return {"message": "Welcome to the Trello-like app!"}