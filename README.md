# 🚦 Agentic AI Powered Smart Traffic Monitoring and Emergency Response System

An intelligent real-time traffic monitoring system built using **YOLOv8, ByteTrack, OpenCV, and LangGraph** for vehicle detection, traffic congestion analysis, accident detection, ambulance prioritization, adaptive signal optimization, and emergency route management.

This project simulates a smart-city traffic control system where multiple AI agents collaborate to make autonomous decisions.

---

## 📌 Features

- Real-time vehicle detection using YOLOv8
- Multi-object tracking using ByteTrack
- Vehicle counting with line crossing logic
- Traffic congestion analysis
- Dynamic traffic signal optimization
- Vehicle speed estimation
- Accident detection using speed and stop-frame analysis
- Ambulance detection and priority signal handling
- Emergency route diversion
- Multi-agent orchestration using LangGraph

---

## 🧠 Agentic AI Workflow

```text
Video Input
   ↓
YOLO Vehicle Detection Agent
   ↓
ByteTrack Tracking Agent
   ↓
Congestion Analysis Agent
   ↓
Accident Detection Agent
   ↓
Emergency Vehicle Agent
   ↓
Route Management Agent
   ↓
Signal Optimization Agent
```

---

## ⚙️ Tech Stack

- Python
- YOLOv8
- ByteTrack
- OpenCV
- NumPy
- Supervision
- LangGraph

---

## 📂 Project Structure

```text
SmartTrafficAI/
│── main.py
│── config.py
│── requirements.txt
│── highway.mp4
│
├── agents/
│   ├── vehicle_detector.py
│   ├── tracker.py
│   ├── congestion_agent.py
│   ├── signal_agent.py
│   ├── accident_agent.py
│   ├── emergency_agent.py
│   ├── route_agent.py
│
├── utils/
│   ├── draw.py
│   ├── counter.py
│   ├── speed.py
│
├── models/
│   └── yolov8n.pt
│
├── agentic_brain.py
```

---

## 🚀 Installation

Clone repository:

```bash
git clone https://github.com/your-username/SmartTrafficAI.git
cd SmartTrafficAI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

```bash
python main.py
```

Run agent orchestration:

```bash
python agentic_brain.py
```

---

## 📊 System Modules

### Vehicle Detection Agent

Detects vehicles in real-time using YOLOv8.

### Tracking Agent

Tracks vehicles across frames using ByteTrack.

### Congestion Agent

Analyzes traffic density.

### Accident Agent

Detects abnormal stopping vehicles.

### Emergency Agent

Detects ambulance and provides priority.

### Route Agent

Activates alternative routes.

### Signal Agent

Optimizes signal timing.

---

## 📈 Future Scope

- Number plate recognition
- Wrong lane detection
- Red light violation
- Helmet detection
- IoT smart signal integration
- Cloud deployment

---

## 🎯 Applications

- Smart city traffic management
- Emergency vehicle prioritization
- Accident monitoring
- Urban traffic optimization

---

## 👨‍💻 Author

**Kuldeep Kumar**
M.Tech in Artificial Intelligence
IIT Guwahati

---

## 📜 License

MIT License
