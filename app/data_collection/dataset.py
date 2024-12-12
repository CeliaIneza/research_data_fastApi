import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Number of records for research projects and researchers
num_research_projects = 500000
num_researchers = 500000

# Output files
research_projects_file = "research_projects_dataset.csv"
researchers_file = "researchers_dataset.csv"

# Generate research projects data
research_projects_data = [
    {
        "id": i + 1,
        "title": fake.catch_phrase(),
        "description": fake.text(max_nb_chars=200),
        "start_date": fake.date_between(start_date='-5y', end_date='-1y'),
        "end_date": fake.date_between(start_date='-1y', end_date='today') if random.choice([True, False]) else None,
        "status": random.choice(["active", "completed", "paused"]),
        "created_at": fake.date_time_this_year(),
    }
    for i in range(num_research_projects)
]

# Save research projects to CSV
with open(research_projects_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "title", "description", "start_date", "end_date", "status", "created_at"])
    writer.writeheader()
    writer.writerows(research_projects_data)

print(f"Dataset with {num_research_projects} research projects saved to {research_projects_file}.")

# Generate researchers data
researchers_data = [
    {
        "id": i + 1,
        "research_project_id": random.randint(1, num_research_projects),
        "name": fake.name(),
        "email": fake.unique.email(),
        "role": random.choice(["Lead", "Analyst", "Assistant"]),
        "phone": fake.phone_number(),
        "created_at": fake.date_time_this_year(),
    }
    for i in range(num_researchers)
]

# Save researchers to CSV
with open(researchers_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "research_project_id", "name", "email", "role", "phone", "created_at"])
    writer.writeheader()
    writer.writerows(researchers_data)

print(f"Dataset with {num_researchers} researchers saved to {researchers_file}.")
