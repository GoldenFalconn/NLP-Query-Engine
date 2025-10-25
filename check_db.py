@'
import sqlite3
import os

if os.path.exists("employee.db"):
    print("✅ employee.db file exists")
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()
    tables = c.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    print(f"📊 Tables found: {tables}")
    if tables:
        try:
            count = c.execute("SELECT COUNT(*) FROM employees").fetchone()[0]
            print(f"👥 Employee count: {count}")
            sample = c.execute("SELECT * FROM employees LIMIT 1").fetchone()
            print(f"📝 Sample row: {sample}")
        except Exception as e:
            print(f"❌ Error querying employees: {e}")
    else:
        print("❌ No tables found in database!")
    conn.close()
else:
    print("❌ employee.db file does NOT exist!")
'@ | Out-File -FilePath "check_db.py" -Encoding UTF8
