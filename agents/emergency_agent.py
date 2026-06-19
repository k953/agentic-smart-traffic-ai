class EmergencyAgent:
    def check(self, detected_classes):
        if "ambulance" in detected_classes:
            return True
        return False