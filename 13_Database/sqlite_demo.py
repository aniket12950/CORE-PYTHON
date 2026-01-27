import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

# Insert data
cursor.execute("INSERT INTO student (name, marks) VALUES (?, ?)", ("Aniket", 85))
conn.commit()

# Fetch data
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close connection
conn.close()
