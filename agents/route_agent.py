class RouteAgent:
    def suggest(self, accident):
        if accident:
            return "Route B Activated"
        return "Normal Route"