from typing import Dict, Optional, List
from pydantic import BaseModel, Field
from app.schemas.user_schema import User
from datetime import datetime

class CustomResponse(BaseModel):
    response: str
    date_created: datetime = Field(default_factory=datetime.now)

    class Config:
        protected_namespaces = ()

class AgentSchema(BaseModel):
    agent_name: str
    model_name: str
    temperature: float
    role: str
    goal: str
    backstory: str
    allow_delegation: bool
    tools: Optional[List[str]] = []

    class Config:
        protected_namespaces = ()

class TaskSchema(BaseModel):
    agent: str
    description: str
    expected_output: str

    class Config:
        protected_namespaces = ()

class ConfigFileSchema(BaseModel):
    agents: List[AgentSchema]
    tasks: List[TaskSchema]

    class Config:
        protected_namespaces = ()

class ConfigurationBase(BaseModel):
    user_id: int
    project_name: str
    project_description: str
    config_file: ConfigFileSchema

    class Config:
        protected_namespaces = ()

class ConfigurationCreate(ConfigurationBase):
    pass

class ConfigurationResponse(BaseModel):
    id: int
    user_id: int
    project_name: str
    project_description: str
    config_file: ConfigFileSchema
    date_created: datetime
    user: User  # Nested User object

    class Config:
        from_attributes = True
        protected_namespaces = ()
        json_schema_extra = {
            "example": {
                "id": 1,
                "user_id": 1,
                "project_name": "Project 1",
                "project_description": "Description 1",
                "config_file": {
                    "agents": [
                        {
                            "agent_name": "Agent 1",
                            "model_name": "gpt-3.5-turbo",
                            "temperature": 0.3,
                            "role": "Senior Research Assistance",
                            "goal": "Research",
                            "backstory": "I am a senior research assistant at a prestigious university.",
                            "allow_delegation": False,
                            "tools": [
                                "search_tool"
                            ]
                        }
                    ],
                    "tasks": [
                        {
                            "agent": "Agent 1",
                            "description": "I need to do a research on Mental health chatbots and need the resources",
                            "expected_output": "Existing Mental health chatbots and their pros, cons, and the resource links to the papers."
                        }
                    ]
                },
                "user": {
                    "id": 1,
                    "name": "John Doe",
                    "email": "johndoe@example.com",
                    "vectorstore": False
                }
            }
        }
