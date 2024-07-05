from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from datetime import datetime

class ResearchCreate(BaseModel):
    user_id: int
    username: str
    query: str
    

class ResearchResponse(BaseModel):
    response: str