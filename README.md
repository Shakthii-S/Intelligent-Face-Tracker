# 👁️ Intelligent Face Tracker

An AI-powered real-time face detection, recognition, and logging system built using **YOLOv8**, **InsightFace**, and **Flask**. The system tracks and logs every unique visitor’s **entry and exit** with cropped snapshots, timestamps, and visitor ID. It features a lightweight **SQLite** backend and a **visual web dashboard** for real-time monitoring.

---

## 📌 Key Features

- 🔍 **YOLOv8 Face Detection**: Accurate detection of faces in live or recorded streams.
- 🧠 **InsightFace Recognition**: Generates 512-D facial embeddings and performs cosine similarity for ID matching.
- 🔁 **Real-Time Visitor Logging**: Logs unique entry/exit per visitor with timestamps and snapshots.
- 🖼️ **Snapshot Storage**: Cropped images are saved in `logs/entry/` and `logs/exit/` directories.
- 🗃️ **SQLite + CSV Logging**: Saves logs to both `face_tracker.db` and `visitor_log.csv`.
- 🌐 **Flask Dashboard**: Visual overview of all entry/exit events, with visitor count and snapshots.
- 🧾 **Configurable Detection**: Skips frames as defined in `config.json`.

---

## ⚙️ Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/your-username/intelligent-face-tracker.git
cd intelligent-face-tracker

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python main.py
🧠 Assumptions Made
Each new face is treated as unique unless matched using cosine similarity.

A face is considered exited if not detected for a few consecutive frames.

The system uses config.json for flexible tuning during dev/interview (e.g., detection skip).

This solution works on both video files and live RTSP streams (for demo/test).

🛠️ Sample config.json
json
Copy
Edit
{
  "skip_frames": 3,
  "similarity_threshold": 0.5,
  "video_source": "video.mp4"
}



🧾 Log Structure
📁 logs/entry/YYYY-MM-DD/: Cropped images of face entries.

📁 logs/exit/YYYY-MM-DD/: Cropped images of face exits.

🗃️ face_tracker.db: Stores all face IDs, timestamps, and embeddings.


🛡️ Technologies Used
Face Detection: YOLOv8

Face Recognition: InsightFace

Backend: Python + Flask

Tracking: OpenCV

Database: SQLite

Config: JSON (config.json)

🙋‍♀️ Author
Shakthi S




