import pandas as pd
import os

patients = pd.read_csv('data/patients.csv')
admissions = pd.read_csv('data/admissions.csv')

# Basic data inspection

print(patients.info())
print(admissions.info())

print(patients.head())
print(admissions.head())


