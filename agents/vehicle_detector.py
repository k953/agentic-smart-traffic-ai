from ultralytics import YOLO
import config

class VehicleDetector:
    def __init__(self):
        self.model = YOLO(config.MODEL_PATH)

    def detect(self, frame):
        results = self.model(frame)

        detections = []

        for result in results:
            for box in result.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])

                if cls in config.VEHICLE_CLASSES and conf > config.CONFIDENCE:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    detections.append([x1, y1, x2, y2, conf])

        return detections