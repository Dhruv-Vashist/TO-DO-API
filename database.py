from pydantic import BaseModel
from enum import Enum

class Status(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: Status = Status.PENDING

class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True

class loginCredentials(BaseModel):
    username: str
    password: str