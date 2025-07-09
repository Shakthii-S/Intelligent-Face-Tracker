# face_recognizer.py
import cv2
import numpy as np
from insightface.app import FaceAnalysis
from datetime import datetime
from db import init_db, save_face_entry, get_all_embeddings, update_exit_time
import os
import time

VIDEO_PATH = "sample_video/video_sample1.mp4"

os.makedirs("logs/entry", exist_ok=True)
os.makedirs("logs/exit", exist_ok=True)
os.makedirs("static", exist_ok=True)

init_db()
cap = cv2.VideoCapture(VIDEO_PATH)
app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0, det_size=(640, 640))

known_faces = get_all_embeddings()
active_faces = {}
face_timeout = 20  # seconds

def save_image(face_img, name, folder):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.jpg"
    path = os.path.join(folder, filename)
    cv2.imwrite(path, face_img)
    static_path = os.path.join("static", filename)
    cv2.imwrite(static_path, face_img)
    return filename

def get_face_crop(frame, bbox):
    x1, y1, x2, y2 = bbox.astype(int)
    return frame[y1:y2, x1:x2]

def is_same_face(embedding):
    for name, known_embedding in known_faces:
        dist = np.linalg.norm(embedding - known_embedding)
        if dist < 0.58:
            return name
    return None

person_count = len(known_faces)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    current_time = time.time()
    detections = app.get(frame)
    seen_now = set()

    for face in detections:
        name = is_same_face(face.embedding)
        if name is None:
            person_count += 1
            name = f"Person{person_count}"
            known_faces.append((name, face.embedding))
            face_crop = get_face_crop(frame, face.bbox)
            snapshot_path = save_image(face_crop, name, "logs/entry")
            save_face_entry(name, face.embedding, snapshot_path)
            print(f"[ENTRY] {name}")

        seen_now.add(name)
        active_faces[name] = current_time

        bbox = face.bbox.astype(int)
        cv2.rectangle(frame, tuple(bbox[:2]), tuple(bbox[2:]), (0, 255, 0), 2)
        cv2.putText(frame, name, tuple(bbox[:2] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    for tracked_name in list(active_faces):
        if tracked_name not in seen_now:
            last_seen = active_faces[tracked_name]
            if current_time - last_seen > face_timeout:
                print(f"[EXIT] {tracked_name}")
                snapshot_path = save_image(np.zeros_like(frame), tracked_name, "logs/exit")
                update_exit_time(tracked_name, snapshot_path)
                del active_faces[tracked_name]

    cv2.imshow("Face Tracker", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
