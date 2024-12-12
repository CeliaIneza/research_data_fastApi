import requests
import pandas as pd
from datetime import datetime

# Function to fetch data from the API
def fetch_data(api_url, limit=500000):
    response = requests.get(f"{api_url}/researchprojects/", params={"limit": limit})
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")

api_url = "http://localhost:8000/api/v1"
df = fetch_data(api_url)

# Function to describe the dataset
def describe_dataset(df):
    print("Dataset Summary:")
    print(df.info())
    print("\nSample Rows:")
    print(df.head())
    print("\nDataset Shape:")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    print("\nDataset Description (Numerical Columns):")
    print(df.describe())
    print("\nDataset Description (All Columns):")
    print(df.describe(include='all'))

describe_dataset(df)

# Function to find and replace null values
def find_null_values(df):
    print("Null Values Summary:")
    print(df.isnull().sum())
    print("\nPercentage of Null Values:")
    print((df.isnull().sum() / len(df)) * 100)

# Function to replace null values with defaults
def replace_null_values(df):
    # Replace missing 'title' with 'Untitled Project'
    if 'title' in df.columns:
        df['title'].fillna('Untitled Project', inplace=True)
    
    # Replace missing 'description' with a placeholder
    if 'description' in df.columns:
        df['description'].fillna('No description provided.', inplace=True)
    
    # Replace missing 'start_date' with a placeholder date
    if 'start_date' in df.columns:
        df['start_date'].fillna('2000-01-01', inplace=True)
    


    return df

# Replace null values in the dataset
find_null_values(df)  # Check for nulls before replacing
df = replace_null_values(df)
find_null_values(df)  # Check for nulls after replacing

def preprocess_data(df):
    # Convert 'start_date' and 'end_date' to datetime format
    df['start_date'] = pd.to_datetime(df['start_date'], errors='coerce').dt.strftime('%d-%m-%Y')
    df['end_date'] = pd.to_datetime(df['end_date'], errors='coerce').dt.strftime('%d-%m-%Y')
    
    # Convert 'title' and 'description' to lowercase
    df['title'] = df['title'].str.lower()
    df['description'] = df['description'].str.lower()
    

    return df

# Preprocess the data
df = preprocess_data(df)

# Print first few rows of preprocessed data
print("\nPreprocessed Data:")
print(df.head())
