import cv2
import config
import numpy as np
from supervision import Detections

from agents.vehicle_detector import VehicleDetector
from agents.tracker import Tracker
from agents.congestion_agent import CongestionAgent
from agents.signal_agent import SignalAgent
from utils.draw import draw_boxes
from utils.counter import line_counter

detector = VehicleDetector()
tracker = Tracker()
congestion_agent = CongestionAgent()
signal_agent = SignalAgent()

cap = cv2.VideoCapture(config.VIDEO_PATH)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Vehicle detection
    detections = detector.detect(frame)

    # Tracking
    tracked_objects = tracker.assign_ids(detections)

    vehicle_count = len(tracked_objects)

    # Congestion analysis
    congestion_level = congestion_agent.analyze(vehicle_count)

    # Signal optimization
    signal_time = signal_agent.optimize(congestion_level)

    # Draw vehicle boxes
    frame = draw_boxes(frame, tracked_objects)

    # Draw counting line
    cv2.line(frame, (400, 400), (1200, 400), (0, 0, 255), 3)

    # Line Counter Logic
    if len(tracked_objects) > 0:
        xyxy = np.array([obj["bbox"][:4] for obj in tracked_objects])
        tracker_ids = np.array([obj["id"] for obj in tracked_objects])

        detections_sv = Detections(
            xyxy=xyxy,
            tracker_id=tracker_ids
        )

        line_counter.trigger(detections_sv)

    # Display text
    cv2.putText(frame, f"Vehicles: {vehicle_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.putText(frame, f"Congestion: {congestion_level}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.putText(frame, f"Signal Time: {signal_time}s", (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.putText(frame, f"IN: {line_counter.in_count}", (20, 160),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(frame, f"OUT: {line_counter.out_count}", (20, 200),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    cv2.imshow("Smart Traffic AI", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()