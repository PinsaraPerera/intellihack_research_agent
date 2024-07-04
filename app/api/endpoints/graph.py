from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas import graph_schema
from app.db.session import get_db
from sqlalchemy.orm import Session
import app.crud.graph as graph

router = APIRouter(
    prefix="/graph",
    tags=["Graphs"],
)

@router.post("/generate", response_model=graph_schema.GraphResponse)
def generate_graph(request: graph_schema.GraphBase, db: Session = Depends(get_db)):
    return graph.create(request, db)