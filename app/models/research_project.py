from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class ResearchProject(Base):
    __tablename__ = "research_projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)  # Title of the research project
    description = Column(String)  # Detailed description of the project
    start_date = Column(DateTime, nullable=False)  # Start date of the project
    end_date = Column(DateTime, nullable=True)  # End date of the project
    status = Column(String, default="active")  # active, completed, paused
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    researchers = relationship("Researcher", back_populates="research_project")
