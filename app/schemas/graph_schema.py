from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class GraphBase(BaseModel):
    user_id : int
    username: str
    message: str
    difficulty: Optional[int] = None

    class Config:
        protected_namespaces = ()

class GraphResponse(BaseModel):
    user_id : int
    response: str
    date_created: datetime = Field(default_factory=datetime.now)

    class Config:
        protected_namespaces = ()