from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class ResearcherBase(BaseModel):
    research_project_id: int
    name: str
    email: EmailStr
    role: str  # Role in the research project (e.g., Lead, Analyst).
    phone: Optional[str] = None  # Optional phone number.


class ResearcherCreate(BaseModel):
    name: str
    email: str
    role: str
    phone: Optional[str] = None
    research_project_id: int  # Foreign key to associate with a project

class ResearcherUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    role: Optional[str]
    phone: Optional[str]

class ResearcherOut(ResearcherBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

