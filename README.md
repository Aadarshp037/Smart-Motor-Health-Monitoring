# Smart Motor Health Monitoring & Predictive Maintenance System

## Overview
This project implements an end-to-end motor monitoring system that integrates a
simulated microcontroller data source with a Python-based backend and a web-based
dashboard. The system is designed to resemble industrial motor monitoring software
used for condition tracking and maintenance decision support.

An ESP32-like data stream is simulated to generate realistic motor operating
parameters, which are processed and visualized through a browser-based dashboard.

---

## Objective
The objective of this project is to:
- Simulate microcontroller-based motor data acquisition
- Monitor key motor operating parameters
- Assess motor health using deterministic logic
- Present insights through a web-based dashboard
- Enable maintenance-oriented decision making

---

## System Architecture
The system follows a modular, layered architecture:

1. **Simulated Microcontroller Layer**  
   Emulates ESP32 firmware behavior by generating motor sensor data.

2. **Data Interface Layer**  
   Streams generated data into a CSV file that acts as a data buffer.

3. **Backend Processing Layer**  
   Evaluates motor condition and computes health indicators.

4. **Web Dashboard Layer**  
   Displays live values, trends, and maintenance status through a browser interface.

---

## Data Flow
Simulated ESP32 Firmware
↓
motor_data.csv
↓
Backend Health Logic
↓
Web Dashboard


---

## Workflow
1. The system initializes with an empty CSV file containing only column headers.
2. The simulated microcontroller module starts generating motor data periodically.
3. Each data sample (voltage, current, RPM, temperature) is appended to the CSV file.
4. The backend logic reads the latest motor data and evaluates motor health.
5. A health score and maintenance status are derived using predefined thresholds.
6. The web dashboard reads updated data continuously.
7. Live metrics, trends, and health indicators are displayed to the user.
8. The system runs continuously, enabling real-time monitoring.

---

## Motor Parameters Monitored
- Voltage
- Current
- Rotational Speed (RPM)
- Temperature

---

## Deployment
The dashboard is designed for cloud-based execution and does not require local
setup.

Recommended platforms:
- Streamlit Community Cloud
- Google Colab
- GitHub Codespaces

The simulated data source enables full system validation without physical hardware.

---

## Implementation Notes
- The ESP32 behavior is simulated using a Python-based firmware emulator.
- This approach enables software-in-the-loop testing before hardware integration.
- The simulator can be replaced with a real ESP32 streaming live sensor data
  without changing the dashboard or backend logic.
- The system prioritizes modularity, clarity, and explainable decision logic.

---

## Future Scope
- Integration with a physical ESP32 microcontroller
- Communication using MQTT or HTTP protocols
- Advanced predictive maintenance models
- Support for multiple motors and dashboards
