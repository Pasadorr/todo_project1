from pydantic import BaseModel

# Модель для доски
class Board(BaseModel):
    title: str