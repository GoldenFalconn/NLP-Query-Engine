import sqlite3

# Create connection
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# Create employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT,
    salary REAL,
    position TEXT,
    email TEXT
)
''')

# Insert sample data
employees = [
    (1, 'John Doe', 'Engineering', 75000, 'Software Engineer', 'john@company.com'),
    (2, 'Jane Smith', 'Marketing', 65000, 'Marketing Manager', 'jane@company.com'),
    (3, 'Bob Johnson', 'Engineering', 85000, 'Senior Developer', 'bob@company.com'),
    (4, 'Alice Williams', 'HR', 60000, 'HR Specialist', 'alice@company.com'),
    (5, 'Charlie Brown', 'Sales', 70000, 'Sales Representative', 'charlie@company.com'),
    (6, 'David Lee', 'Engineering', 90000, 'Tech Lead', 'david@company.com'),
    (7, 'Emma Davis', 'Finance', 72000, 'Financial Analyst', 'emma@company.com'),
    (8, 'Frank Wilson', 'Marketing', 68000, 'Content Manager', 'frank@company.com'),
    (9, 'Grace Taylor', 'Engineering', 78000, 'Backend Developer', 'grace@company.com'),
    (10, 'Henry Moore', 'Sales', 75000, 'Account Manager', 'henry@company.com')
]

cursor.executemany('INSERT OR REPLACE INTO employees VALUES (?, ?, ?, ?, ?, ?)', employees)

conn.commit()
conn.close()

print("✅ Sample database created successfully: employee.db")
print("📊 10 employees added to the database")
