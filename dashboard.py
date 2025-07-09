from flask import Flask, render_template, send_from_directory
import sqlite3
import os

app = Flask(__name__)

DB_PATH = "face_tracker.db"
FACES_DIR = "faces"

def fetch_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name, timestamp FROM faces ORDER BY timestamp DESC")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    visitors = fetch_data()
    count = len(set([v[0] for v in visitors]))
    return render_template("index.html", visitors=visitors, count=count)

@app.route('/faces/<person>/<filename>')
def face_image(person, filename):
    return send_from_directory(os.path.join(FACES_DIR, person), filename)

if __name__ == '__main__':
    app.run(debug=True)
