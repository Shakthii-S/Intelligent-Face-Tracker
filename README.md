# 👁️ Intelligent Face Tracker

A real-time AI-powered system for detecting, tracking, and identifying unique faces using **YOLOv8** and **InsightFace**. Designed for secure and smart visitor monitoring, it logs **entry and exit events** with accurate timestamps, saves cropped face snapshots, and stores all data in a lightweight **SQLite database** with a visual **Flask dashboard**.

---

## 📌 Key Features

- 🔍 **Real-Time Detection**: Uses YOLOv8 to detect faces in live video streams or sample footage.
- 🧠 **Face Recognition**: Matches incoming faces with InsightFace embeddings to identify individuals.
- 🧾 **Entry & Exit Logging**: Accurately logs both **entry** and **exit** events per person, only once each.
- 🖼️ **Snapshot Saving**: Saves cropped face images for both events in `logs/entry/` and `logs/exit/`.
- 🗃️ **SQLite Database**: Stores face embeddings, timestamps, and person ID in `face_tracker.db`.
- 📊 **Web Dashboard**: Visualizes all activity — entry/exit logs, total unique visitors, and images.
- 📂 **CSV Export**: Automatically logs to `visitor_log.csv` for backup and analysis.

---

## 📽️ Demo Video

👉 [Click here to watch the demo on Loom](https://www.loom.com/share/a57ebbc759194f9789f420a18d0d647e?sid=29243393-b9b3-41fe-a48c-8fcede20e6f6)

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

```
## 🛠️ Sample config.json
**json
**Edit
**{
**"skip_frames": 3,**"similarity_threshold": 0.5,
**"video_source": "video.mp4"
**}

 “This project is a part of a hackathon run by https://katomaran.com ”
