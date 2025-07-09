# db.py
import sqlite3
import numpy as np
import datetime

DB_PATH = "face_tracker.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS faces (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        embedding BLOB,
                        entry_time TEXT,
                        exit_time TEXT,
                        entry_snapshot TEXT,
                        exit_snapshot TEXT)''')
    conn.commit()
    conn.close()

def save_face_entry(name, embedding, snapshot_path):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO faces (name, embedding, entry_time, entry_snapshot) VALUES (?, ?, ?, ?)",
                   (name, embedding.tobytes(), now, snapshot_path))
    conn.commit()
    conn.close()

def update_exit_time(name, snapshot_path):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE faces SET exit_time = ?, exit_snapshot = ? WHERE name = ?", (now, snapshot_path, name))
    conn.commit()
    conn.close()

def get_all_embeddings():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name, embedding FROM faces")
    rows = cursor.fetchall()
    conn.close()
    return [(name, np.frombuffer(embedding, dtype=np.float32)) for name, embedding in rows]

def fetch_all_faces():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name, entry_time, exit_time, entry_snapshot, exit_snapshot FROM faces")
    data = cursor.fetchall()
    conn.close()
    return data
