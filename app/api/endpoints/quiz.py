from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException, Request
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.schemas import quiz_schema, user_schema
import app.crud.quiz as quiz

router = APIRouter(
    prefix="/quiz",
    tags=["Quiz"],
)

@router.post("/", response_model=quiz_schema.Quiz)
def create_quiz(request: quiz_schema.QuizCreate, db: Session = Depends(get_db)):
    return quiz.create(request)