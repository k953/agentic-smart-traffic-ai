from langgraph.graph import StateGraph

class TrafficState(dict):
    pass

def detect_vehicle(state):
    print("Vehicle detection done")
    return state

def analyze_congestion(state):
    print("Congestion analyzed")
    return state

def detect_accident(state):
    print("Accident checked")
    return state

def emergency_priority(state):
    print("Emergency vehicle checked")
    return state

workflow = StateGraph(TrafficState)

workflow.add_node("vehicle_detection", detect_vehicle)
workflow.add_node("congestion", analyze_congestion)
workflow.add_node("accident", detect_accident)
workflow.add_node("emergency", emergency_priority)

workflow.set_entry_point("vehicle_detection")

workflow.add_edge("vehicle_detection", "congestion")
workflow.add_edge("congestion", "accident")
workflow.add_edge("accident", "emergency")

app = workflow.compile()