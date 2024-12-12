from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..controllers.researchproject_controller import ResearchProjectController
from ..schemas.research_project import ResearchProjectCreate, ResearchProject, ResearchProjectUpdate
from typing import Any, List

router = APIRouter()

@router.post("/researchprojects/", response_model=ResearchProject)
async def create_research_project(
    research_project: ResearchProjectCreate,
    db: Session = Depends(get_db)
):
    return await ResearchProjectController.create_research_project(db, research_project)

@router.put("/researchprojects/{id}", response_model=ResearchProject)
async def update_research_project(
    id: int,
    research_project: ResearchProjectUpdate,
    db: Session = Depends(get_db)
) -> Any:
    updated_project = await ResearchProjectController.update_research_project(db, id, research_project)
    if not updated_project:
        raise HTTPException(status_code=404, detail="Research Project not found")
    return updated_project

@router.get("/researchprojects/", response_model=List[ResearchProject])
async def list_research_projects(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return await ResearchProjectController.get_research_projects(db, skip)

@router.delete("/researchprojects/{id}", response_model=ResearchProject)
async def delete_research_project(
    id: int,
    db: Session = Depends(get_db)
) -> Any:
    deleted_project = await ResearchProjectController.delete_research_project(db, id)
    if not deleted_project:
        raise HTTPException(status_code=404, detail="Research Project not found")
    return deleted_project
