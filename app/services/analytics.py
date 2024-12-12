from ..models.researchers import Researcher
from sqlalchemy.orm import Session
import pandas as pd

class AnalyticsService:
    @staticmethod
    def calculate_project_performance(db: Session, research_project_id: int):
        # Fetch all researchers associated with the given research project
        researchers = db.query(Researcher).filter(Researcher.research_project_id == research_project_id).all()

        # Create a DataFrame to analyze researcher contributions
        df = pd.DataFrame([{
            'name': r.name,
            'role': r.role,
            'created_at': r.created_at
        } for r in researchers])

        # Example analysis (customize based on available data and requirements)
        return {
            'total_researchers': len(df),
            'roles_distribution': df['role'].value_counts().to_dict(),
            'earliest_joined': df['created_at'].min(),
            'latest_joined': df['created_at'].max(),
        }
