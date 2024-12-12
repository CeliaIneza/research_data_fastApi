from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Researcher(Base):
    __tablename__ = "researchers"

    id = Column(Integer, primary_key=True, index=True)
    research_project_id = Column(Integer, ForeignKey("research_projects.id"), nullable=False)
    name = Column(String, nullable=False)  # Name of the researcher
    email = Column(String, unique=True, nullable=False)  # Researcher's email
    role = Column(String, nullable=False)  # Role in the project (e.g., Lead, Analyst)
    phone = Column(String, nullable=True)  # Optional phone number
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    research_project = relationship("ResearchProject", back_populates="researchers")

