from ultralytics import YOLO
import cv2

class FaceDetector:
    def __init__(self, model_path="detection/yolov8n-face.pt"):
        self.model = YOLO(model_path)

    def detect_faces(self, frame):
        results = self.model.predict(source=frame, verbose=False, conf=0.5)
        faces = []
        if results:
            boxes = results[0].boxes.xyxy.cpu().numpy()  # x1, y1, x2, y2
            for box in boxes:
                x1, y1, x2, y2 = map(int, box[:4])
                faces.append((x1, y1, x2, y2))
        return faces
