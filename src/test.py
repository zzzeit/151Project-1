import sqlite3 as sql
import csv
from data_management import DataManager

# Database and table setup
db_path = "./database/database.db"  # Path to your SQLite database
table_name = "students"

# Connect to the database
connection = sql.connect(db_path)
cursor = connection.cursor()

# Create the table if it doesn't exist
cursor.execute(f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    sex TEXT NOT NULL,
    id INTEGER PRIMARY KEY,
    year_level TEXT NOT NULL,
    college TEXT NOT NULL,
    program_code TEXT NOT NULL
)
""")
connection.commit()

# Initialize DataManager
data_manager = DataManager(connection, cursor)

# Read data from the CSV file
csv_path = "./database/students.csv"  # Adjust the path if necessary
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    data = [tuple(row) for row in reader]

# Write data to the database
data_manager.write_data(table_name, data)

# Close the connection
connection.close()

print("Data has been successfully written to the database.")