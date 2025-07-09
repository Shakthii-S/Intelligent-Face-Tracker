import sqlite3

def get_unique_visitor_count():
    conn = sqlite3.connect("face_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM faces")
    count = cursor.fetchone()[0]
    conn.close()
    return count

if __name__ == "__main__":
    total = get_unique_visitor_count()
    print(f"✅ Total Unique Visitors: {total}")
