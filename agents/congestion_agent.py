import config

class CongestionAgent:
    def analyze(self, vehicle_count):
        if vehicle_count > config.CONGESTION_THRESHOLD:
            return "HIGH"
        return "NORMAL"