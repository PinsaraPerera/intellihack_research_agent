from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from datetime import datetime


class QuizCreate(BaseModel):
    user_id: int
    username: str
    no_of_questions: int
    topic: Optional[str] = None

class Question(BaseModel):
    question: str
    options: List[str]
    correct: str

class Response(BaseModel):
    questions: List[Question]

class Quiz(BaseModel):
    user_id: int
    response: Response
    date_created: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        protected_namespaces = ()
