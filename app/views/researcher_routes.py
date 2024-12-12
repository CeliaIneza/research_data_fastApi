from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.researcher import ResearcherCreate, ResearcherUpdate, ResearcherOut
from app.controllers.researcher_controller import ResearcherController
from typing import List

router = APIRouter()

@router.post("/researchers/", response_model=ResearcherOut)
def create_researcher(researcher_data: ResearcherCreate, db: Session = Depends(get_db)):
    return ResearcherController.create_researcher(db, researcher_data)

@router.get("/researchers/{researcher_id}", response_model=ResearcherOut)
def get_researcher(researcher_id: int, db: Session = Depends(get_db)):
    return ResearcherController.get_researcher_by_id(db, researcher_id)

@router.get("/researchers/", response_model=List[ResearcherOut])
def list_researchers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return ResearcherController.get_all_researchers(db, skip, limit)

@router.put("/researchers/{researcher_id}", response_model=ResearcherOut)
def update_researcher(researcher_id: int, researcher_data: ResearcherUpdate, db: Session = Depends(get_db)):
    return ResearcherController.update_researcher(db, researcher_id, researcher_data)

@router.delete("/researchers/{researcher_id}")
def delete_researcher(researcher_id: int, db: Session = Depends(get_db)):
    if ResearcherController.delete_researcher(db, researcher_id):
        return {"detail": "Researcher deleted successfully"}
    raise HTTPException(status_code=404, detail="Researcher not found")
