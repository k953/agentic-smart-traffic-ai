import config

class SignalAgent:
    def optimize(self, congestion_level):
        if congestion_level == "HIGH":
            return config.HIGH_SIGNAL
        return config.NORMAL_SIGNAL