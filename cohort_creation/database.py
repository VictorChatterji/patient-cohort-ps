import sqlite3
import pandas as pd
import os


# Define the folder containing CSV files
csv_folder = 'data/'

# Initialize an in-memory SQLite database
conn = sqlite3.connect('cohort_analysis.db')  # Use ':memory:' for in-memory DB or 'database.db' for persistent DB

# Load all CSV files into SQLite tables
csv_files = [f for f in os.listdir(csv_folder) if f.endswith('.csv')]
for file in csv_files:
    table_name = os.path.splitext(file)[0]  # Use filename (without extension) as table name
    file_path = os.path.join(csv_folder, file)

    # Load CSV into a DataFrame
    df = pd.read_csv(file_path)

    # Write the DataFrame to SQLite as a table
    df.to_sql(table_name, conn, if_exists='replace', index=False)

print(f"Loaded {len(csv_files)} CSV files into SQLite database.")


# Example query: List all tables
tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = conn.execute(tables_query).fetchall()
print("Tables in the database:", [table[0] for table in tables])

