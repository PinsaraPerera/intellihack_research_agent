from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas import agentConfiguration_schema
from app.db.session import get_db
from sqlalchemy.orm import Session
import app.crud.agentConfiguration as agentConfiguration


router = APIRouter(
    prefix="/agentConfiguration",
    tags=["Agent Configuration"],
)

@router.post("/", response_model=agentConfiguration_schema.ConfigurationResponse)
def create_configuration(request: agentConfiguration_schema.ConfigurationBase, db: Session = Depends(get_db)):
    return agentConfiguration.create(request, db)

@router.get("/getAll/{user_id}", response_model=List[agentConfiguration_schema.ConfigurationResponse])
def get_all_configurations(user_id: int, db: Session = Depends(get_db)):
    return agentConfiguration.get_all(user_id, db)

@router.put("update/{projectName}", response_model=agentConfiguration_schema.ConfigurationResponse)
def update_configuration(projectName: str, request: agentConfiguration_schema.ConfigurationBase, db: Session = Depends(get_db)):
    return agentConfiguration.update_configuration(projectName, request, db)

@router.delete("delete/{projectName}")
def delete_configuration(projectName: str, db: Session = Depends(get_db)):
    return agentConfiguration.delete_configuration(projectName, db)

@router.get("/execute/{projectName}", response_model=agentConfiguration_schema.CustomResponse)
def execute_configuration(projectName: str, db: Session = Depends(get_db)):
    return agentConfiguration.execute_configuration(projectName, db)