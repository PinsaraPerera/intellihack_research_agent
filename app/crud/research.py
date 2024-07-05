from sqlalchemy.orm import Session
from app.schemas import research_schema
from datetime import datetime
from fastapi import HTTPException, status
from app.ResearchAgent.agent import research_chain


def create_research(request: research_schema.ResearchCreate):
    response = research_chain(
        query=request.query
    )

    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Response not found. Try again later.",
        )

    result = research_schema.ResearchResponse(response=response)

    return result