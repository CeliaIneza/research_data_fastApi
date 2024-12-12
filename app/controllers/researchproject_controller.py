from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.research_project import ResearchProject
from app.schemas.research_project import ResearchProjectCreate, ResearchProjectUpdate
from typing import List

class ResearchProjectController:
    @staticmethod
    async def create_research_project(db: Session, project_data: ResearchProjectCreate) -> ResearchProject:
        db_project = ResearchProject(
            title=project_data.title,
            description=project_data.description,
            start_date=project_data.start_date,
            end_date=project_data.end_date,
            status="active"
        )
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project

    @staticmethod
    async def update_research_project(db: Session, id: int, project_data: ResearchProjectUpdate) -> ResearchProject:
        db_project = db.query(ResearchProject).filter(ResearchProject.id == id).first()
        if not db_project:
            raise HTTPException(status_code=404, detail="Research project not found")
        
        db_project.title = project_data.title
        db_project.description = project_data.description
        db_project.start_date = project_data.start_date
        db_project.end_date = project_data.end_date
        db_project.researchers = project_data.researchers
        db_project.status = project_data.status or db_project.status

        db.commit()
        db.refresh(db_project)
        return db_project

    @staticmethod
    async def get_research_projects(db: Session, skip: int = 0) -> List[ResearchProject]:
        return db.query(ResearchProject).offset(skip).all()

    @staticmethod
    async def get_research_project(db: Session, project_id: int) -> ResearchProject:
        project = db.query(ResearchProject).filter(ResearchProject.id == project_id).first()
        if not project:
            raise HTTPException(status_code=404, detail="Research project not found")
        return project

    @staticmethod
    async def delete_research_project(db: Session, id: int) -> bool:
        db_project = db.query(ResearchProject).filter(ResearchProject.id == id).first()
        if not db_project:
            raise HTTPException(status_code=404, detail="Research project not found")
        
        db.delete(db_project)
        db.commit()
        return True
