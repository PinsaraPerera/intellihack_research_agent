from sqlalchemy.orm import Session
import app.models.agentConfiguration as agent
import app.models.user as user
from app.schemas import agentConfiguration_schema
from fastapi import HTTPException, status
from AgentFramework.main import run
from datetime import datetime

def get_all(user_id: int, db: Session):
    configurations = db.query(agent.Agent_Configurations).filter(agent.Agent_Configurations.user_id == user_id).all()
    return configurations

def create(request: agentConfiguration_schema.ConfigurationCreate, db: Session):
    existing_project = db.query(agent.Agent_Configurations).filter(agent.Agent_Configurations.project_name == request.project_name).first()
    check_user = db.query(user.User).filter(user.User.id == request.user_id).first()

    if not check_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {request.user_id} not found. Please register first."
        )

    if existing_project:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Project name already exists"
        )
    
    new_configuration = agent.Agent_Configurations(
        user_id=request.user_id,
        project_name=request.project_name,
        project_description=request.project_description,
        config_file=request.config_file.dict(),
    )

    db.add(new_configuration)
    db.commit()
    db.refresh(new_configuration)
    return new_configuration

def update_configuration(projectName: str, request: agentConfiguration_schema.ConfigurationCreate, db: Session):
    configuration = db.query(agent.Agent_Configurations).filter(agent.Agent_Configurations.project_name == projectName).first()
    if not configuration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Configuration with project name {projectName} not found"
        )

    configuration.project_description = request.project_description
    configuration.config_file = request.config_file.dict()

    db.commit()
    db.refresh(configuration)
    return configuration

def delete_configuration(projectName: str, db: Session):
    configuration = db.query(agent.Agent_Configurations).filter(agent.Agent_Configurations.project_name == projectName).first()
    if not configuration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Configuration with project name {projectName} not found"
        )

    db.delete(configuration)
    db.commit()
    return {"message": f"Configuration with project name {projectName} deleted successfully"}

def execute_configuration(projectName: str, db: Session):
    configuration = db.query(agent.Agent_Configurations).filter(agent.Agent_Configurations.project_name == projectName).first()
    if not configuration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Configuration with project name {projectName} not found"
        )

    response = run(configuration.config_file)

    return agentConfiguration_schema.CustomResponse(
        response=response,
        date_created=datetime.now()
    )
