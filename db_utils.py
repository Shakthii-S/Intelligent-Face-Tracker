import sqlite3

def init_db():
    conn = sqlite3.connect("face_log.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS faces (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            embedding BLOB
        )
    ''')
    conn.commit()
    conn.close()

def insert_face(name, embedding):
    conn = sqlite3.connect("face_log.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO faces (name, embedding) VALUES (?, ?)", (name, embedding.tobytes()))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # Face already exists
    conn.close()

def get_all_faces():
    conn = sqlite3.connect("face_log.db")
    c = conn.cursor()
    c.execute("SELECT name, embedding FROM faces")
    data = c.fetchall()
    conn.close()
    return [(name, memoryview(embed)) for name, embed in data]
