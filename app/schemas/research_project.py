from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional

class ResearchProjectBase(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: Optional[datetime]  # End date can be optional if the project is ongoing.

    @validator("start_date", "end_date", pre=True)
    def parse_dates(cls, value):
        if isinstance(value, str):
            try:
                # Support DD.MM.YYYY format
                return datetime.strptime(value, "%d.%m.%Y")
            except ValueError:
                raise ValueError("Date must be in format DD.MM.YYYY or ISO 8601")
        return value

class ResearchProjectCreate(BaseModel):
    title: str
    description: Optional[str] = None
    start_date: datetime
    end_date: Optional[datetime] = None
    status: Optional[str] = "active"


class ResearchProjectUpdate(ResearchProjectBase):
    title: Optional[str]
    description: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]

class ResearchProjectOut(ResearchProjectBase):
    id: int
    status: str  # e.g., active, paused, completed
    created_at: datetime

    class Config:
        orm_mode = True

# Add this class to resolve the import error
class ResearchProject(ResearchProjectOut):
    pass
