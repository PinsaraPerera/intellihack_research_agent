from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException, Request
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.schemas import research_schema, user_schema
import app.crud.research as research

router = APIRouter(
    prefix="/research",
    tags=["Research"],
)

@router.post("/", response_model=research_schema.ResearchResponse)
def create_research(research_create: research_schema.ResearchCreate, db: Session = Depends(get_db)):
    return research.create_research(research_create)

