import cv2
from detection.face_detector import FaceDetector

# Load video
video_path = "sample_video/sample.mp4"  # Make sure sample.mp4 exists
cap = cv2.VideoCapture(video_path)

# Load face detector
detector = FaceDetector()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = detector.detect_faces(frame)

    for (x1, y1, x2, y2) in faces:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()

