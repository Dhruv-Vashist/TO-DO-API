from pydantic import BaseModel
from enum import Enum

class Status(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class Task(BaseModel):
    title: str
    description: str | None = None
    completed: Status = Status.PENDING

class User(BaseModel):
    username: str| None = None
    email: str
    password: str
    model_config = {"extra": "forbid"}

class loginCredentials(BaseModel):
    username: str
    password: str