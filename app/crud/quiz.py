from sqlalchemy.orm import Session
from app.schemas import quiz_schema
from datetime import datetime
from fastapi import HTTPException, status
from app.quizGeneratingAgent.main import main
import json


def create(request: quiz_schema.QuizCreate):
    response = main(
        no_of_questions=request.no_of_questions, user_email=request.username
    )

    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Response not found. Try again later.",
        )

    if isinstance(response, str):
        response = json.loads(response)

    questions_data = response.get("questions", [])

    response_model = quiz_schema.Response(questions=questions_data)

    questions = quiz_schema.Quiz(
        user_id=request.user_id, response=response_model, date_created=datetime.utcnow()
    )

    return questions
