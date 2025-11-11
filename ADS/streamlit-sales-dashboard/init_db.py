import sqlite3

conn = sqlite3.connect('data/users.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
''')
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'admin123'), ('user', 'user123')")
conn.commit()
conn.close()

print("✅ Database initialized successfully!")
