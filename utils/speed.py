import math

previous_positions = {}

def estimate_speed(vehicle_id, x1, y1, x2, y2):
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2

    if vehicle_id in previous_positions:
        prev_x, prev_y = previous_positions[vehicle_id]

        distance = math.sqrt((center_x - prev_x)**2 + (center_y - prev_y)**2)

        speed = distance * 0.5   # scaling factor

        previous_positions[vehicle_id] = (center_x, center_y)

        return round(speed, 2)

    previous_positions[vehicle_id] = (center_x, center_y)

    return 0