from fastapi import FastAPI
from .views import research_projects_routes, researcher_routes
from .models import research_project, researcher
from .database import engine

# Initialize the FastAPI app
app = FastAPI(title="Research Data Management System")

# Create database tables for ResearchProjects and Researchers
def create_tables():
    research_project.Base.metadata.create_all(bind=engine)
    researcher.Base.metadata.create_all(bind=engine)

create_tables()

# Include routers for handling ResearchProjects and Researchers routes
app.include_router(research_projects_routes, prefix="/api/v1", tags=["researchprojects"])
app.include_router(researcher_routes, prefix="/api/v1", tags=["researchers"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

