from fastapi import FastAPI
import sqlite3

app = FastAPI()

conn = sqlite3.connect('test.db', check_same_thread=False)

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     age INTEGER NOT NULL)''')

conn.commit()

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the SQLite example with FastAPI!"
    }