vehicle_stop_frames = {}

class AccidentAgent:
    def detect(self, vehicle_id, speed):
        if speed < 2:
            if vehicle_id not in vehicle_stop_frames:
                vehicle_stop_frames[vehicle_id] = 1
            else:
                vehicle_stop_frames[vehicle_id] += 1

            if vehicle_stop_frames[vehicle_id] > 5:
                return True
        else:
            vehicle_stop_frames[vehicle_id] = 0

        return False