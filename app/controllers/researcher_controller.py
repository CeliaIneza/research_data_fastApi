from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.researcher import Researcher
from app.schemas.researcher import ResearcherCreate, ResearcherUpdate
from typing import List

class ResearcherController:
    @staticmethod
    def create_researcher(db: Session, researcher_data: ResearcherCreate) -> Researcher:
        researcher = Researcher(**researcher_data.dict())
        db.add(researcher)
        db.commit()
        db.refresh(researcher)
        return researcher

    @staticmethod
    def get_researcher_by_id(db: Session, researcher_id: int) -> Researcher:
        researcher = db.query(Researcher).filter(Researcher.id == researcher_id).first()
        if not researcher:
            raise HTTPException(status_code=404, detail="Researcher not found")
        return researcher

    @staticmethod
    def get_all_researchers(db: Session, skip: int = 0, limit: int = 100) -> List[Researcher]:
        return db.query(Researcher).offset(skip).limit(limit).all()

    @staticmethod
    def update_researcher(db: Session, researcher_id: int, researcher_data: ResearcherUpdate) -> Researcher:
        researcher = db.query(Researcher).filter(Researcher.id == researcher_id).first()
        if not researcher:
            raise HTTPException(status_code=404, detail="Researcher not found")
        
        for field, value in researcher_data.dict(exclude_unset=True).items():
            setattr(researcher, field, value)

        db.commit()
        db.refresh(researcher)
        return researcher

    @staticmethod
    def delete_researcher(db: Session, researcher_id: int) -> bool:
        researcher = db.query(Researcher).filter(Researcher.id == researcher_id).first()
        if not researcher:
            raise HTTPException(status_code=404, detail="Researcher not found")
        
        db.delete(researcher)
        db.commit()
        return True

