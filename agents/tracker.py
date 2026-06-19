from supervision import ByteTrack, Detections
import numpy as np

class Tracker:
    def __init__(self):
        self.tracker = ByteTrack()

    def assign_ids(self, detections):
        if len(detections) == 0:
            return []

        xyxy = []
        confidence = []

        for det in detections:
            x1, y1, x2, y2, conf = det
            xyxy.append([x1, y1, x2, y2])
            confidence.append(conf)

        # Convert into numpy arrays
        xyxy = np.array(xyxy)
        confidence = np.array(confidence)

        detections_sv = Detections(
            xyxy=xyxy,
            confidence=confidence
        )

        tracked = self.tracker.update_with_detections(detections_sv)

        tracked_objects = []

        for i in range(len(tracked.xyxy)):
            tracked_objects.append({
                "id": int(tracked.tracker_id[i]),
                "bbox": [
                    int(tracked.xyxy[i][0]),
                    int(tracked.xyxy[i][1]),
                    int(tracked.xyxy[i][2]),
                    int(tracked.xyxy[i][3]),
                    float(tracked.confidence[i])
                ]
            })

        return tracked_objects