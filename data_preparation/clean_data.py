import pandas as pd

# Load the final cohort data from CSV or other file formats
cohort_data = pd.read_csv('data/cohort_filtered.csv')
# print(cohort_data.head())

cohort_data.isnull().sum()  # Check for missing values
cohort_data = cohort_data.dropna()  # Drop rows with missing values if necessary

cohort_data['anchor_age'] = pd.to_numeric(cohort_data['anchor_age'], errors='coerce')  # Ensure anchor_age is numeric
cohort_data['admittime'] = pd.to_datetime(cohort_data['admittime'], errors='coerce')  # Ensure admittime is datetime
cohort_data['dischtime'] = pd.to_datetime(cohort_data['dischtime'], errors='coerce')  # Ensure dischtime is datetime
cohort_data = cohort_data.dropna(subset=['anchor_age', 'drug', 'icd_code'])

print(cohort_data.head())