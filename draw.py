import cv2

from utils.speed import estimate_speed
from agents.accident_agent import AccidentAgent

accident_agent = AccidentAgent()


def draw_boxes(frame, tracked_objects):
    for obj in tracked_objects:
        x1, y1, x2, y2, conf = obj["bbox"]
        vehicle_id = obj["id"]

        # speed estimate
        speed = estimate_speed(vehicle_id, x1, y1, x2, y2)

        # accident detection
        accident = accident_agent.detect(vehicle_id, speed)

        color = (0, 255, 0)

        if accident:
            color = (0, 0, 255)

        # bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

        # ID + Speed
        cv2.putText(
            frame,
            f"ID:{vehicle_id} Speed:{speed}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            color,
            2
        )

        # Accident alert
        if accident:
            cv2.putText(
                frame,
                "ACCIDENT ALERT",
                (x1, y2 + 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2
            )

    return frame