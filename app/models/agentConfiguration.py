from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base
from app.models.user import User

class Agent_Configurations(Base):
    __tablename__ = "agent_configurations"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_name = Column(String, unique=True, index=True)
    project_description = Column(String)
    config_file = Column(JSON)
    date_created = Column(DateTime, default=func.now(), nullable=False)

    user = relationship("User")

    
