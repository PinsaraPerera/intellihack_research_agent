from sqlalchemy.orm import Session
from app.schemas import graph_schema
from fastapi import HTTPException, status
from graphingAgent.main import main
from datetime import datetime


def create(request: graph_schema.GraphBase, db: Session):
    try:
        result = main(request.message)
        
        return graph_schema.GraphResponse(
            user_id = request.user_id,
            response = result,
            date_created = datetime.now()
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )