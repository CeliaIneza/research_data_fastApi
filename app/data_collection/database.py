import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.research_project import ResearchProject
from app.models.researcher import Researcher
from datetime import datetime

# Initialize Faker and Database Connection for SQLite
fake = Faker()
DATABASE_URL = "sqlite:///research_data_fast_api.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
db = Session()

# Generate Research Projects
def generate_research_projects(num_projects):
    projects = []
    for _ in range(num_projects):
        # Generate random start and end dates
        start_date = fake.date_this_decade()
        end_date = fake.date_this_decade() if random.choice([True, False]) else None
        
        # Create ResearchProject object
        project = ResearchProject(
            title=fake.sentence(nb_words=5),
            description=fake.text(max_nb_chars=200),
            start_date=start_date,
            end_date=end_date
        )

        # Generate a list of researchers for this project
        num_researchers = random.randint(1, 5)  # Random number of researchers per project
        researchers = []
        for _ in range(num_researchers):
            researcher = Researcher(
                name=fake.name(),
                email=fake.email(),
                role=random.choice(["Lead", "Analyst", "Assistant"]),
                phone=fake.phone_number(),
                research_project=project  # Set the relationship
            )
            researchers.append(researcher)
        
        # Add the researchers to the project
        project.researchers = researchers
        
        # Add the project to the list
        projects.append(project)

    return projects

# Insert Data in Batches
def insert_data_in_batches(session, data, batch_size=1000):
    for i in range(0, len(data), batch_size):
        session.bulk_save_objects(data[i:i + batch_size])
        session.commit()

# Main Function
def main():
    print("Generating research projects...")
    projects = generate_research_projects(100000)
    insert_data_in_batches(db, projects)
    print(f"Inserted {len(projects)} research projects.")

    print("Data population completed!")

if __name__ == "__main__":
    main()


