# auth.py (with SQLite database)
import hashlib
import sqlite3

DB_FILE = "users.db"  # SQLite database file

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_users_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            hashed_password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def authenticate_user(username, password):
    create_users_table()  # Ensure table exists
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT hashed_password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result:
        hashed_password = hash_password(password)
        return result[0] == hashed_password
    return False

def signup_user(username, password):
    create_users_table()  # Ensure table exists
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    if result:
        conn.close()
        return False  # Username already exists
    hashed_password = hash_password(password)
    cursor.execute("INSERT INTO users (username, hashed_password) VALUES (?, ?)",
                   (username, hashed_password))
    conn.commit()
    conn.close()
    return True