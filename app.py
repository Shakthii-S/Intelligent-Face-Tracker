from flask import Flask, render_template
from db import fetch_all_faces

app = Flask(__name__)

@app.route("/")
def dashboard():
    faces = fetch_all_faces()
    total = len(faces)
    return render_template("index.html", faces=faces, total=total)

if __name__ == "__main__":
    app.run(debug=True)
