import sqlite3
import csv
import database

# Function to convert table to CSV
def table_to_csv(table_name, conn, output_folder):
    # Query to select all rows from the table
    query = f"SELECT * FROM {table_name};"
    
    try:
        # Create a cursor from the connection
        cursor = conn.cursor()
        
        # Execute the query using the cursor
        cursor.execute(query)
        
        # Fetch all rows from the query result
        rows = cursor.fetchall()

        # Get column names (for the header in the CSV)
        column_names = [description[0] for description in cursor.description]

        # Define the CSV file path
        csv_file_path = f"{output_folder}/{table_name}.csv"

        # Write data to CSV
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(column_names)  # Write header (column names)
            writer.writerows(rows)  # Write table data

        print(f"Table '{table_name}' exported successfully to {csv_file_path}.")

        # Close the cursor
        cursor.close()

    except Exception as e:
        print(f"Error exporting table '{table_name}' to CSV: {e}")

# Attach the database and create connection
try:
    database.conn = sqlite3.connect('cohort_analysis.db')
    print("Database connected successfully.")
except sqlite3.OperationalError as e:
    print(f"Error connecting to database: {e}")

# Specify the folder where you want to save the CSV files
output_folder = "csv_exports"  # Ensure this folder exists

# List of tables to export (if you want to export all tables, use the tables you identified previously)
tables_to_export = [
    "cohort_acetaminophen",
    "cohort_lorazepam",
    "cohort_atorvastatin",
    "cohort_length_of_stay",
    "cohort_discharge_location",
    "cohort_final",
    "cohort_filtered"
]

# Loop through each table and export it to CSV
for table in tables_to_export:
    table_to_csv(table, database.conn, output_folder)

# Close the database connection after exporting
database.conn.close()
