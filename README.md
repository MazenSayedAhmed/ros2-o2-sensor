# ROS2 O₂ Sensor Simulator

This project implements a **ROS2 node** that simulates a basic O₂ (oxygen) sensor.  
The node publishes dummy oxygen concentration data at a fixed rate and is **containerized with Docker** for easy deployment.
## 📂 Folder Structure

ros2_ws/
├── src/
│ └── o2_sensor_pkg/
│ ├── package.xml
│ ├── setup.py
│ ├── setup.cfg
│ ├── resource/
│ ├── test/
│ └── o2_sensor_pkg/
│ ├── init.py
│ └── o2_sensor_node.py
├── Dockerfile
├── run_docker.sh
└── README.md

## ⚙️ ROS2 Node Overview

- **Node Name:** `o2_sensor_node`  
- **Topic:** `/o2_sensor/data`  
- **Message Type:** `std_msgs.msg.Float32`  
- **Publish Rate:** 1 Hz  
- **Behavior:**  
  - Publishes random O₂ concentration values around 21% to simulate real sensor fluctuations.  
  - Prints a warning if O₂ is below 19% or above 23%.
## 🛠 Installation & Local Run

### 1. Create ROS2 workspace (if not already):

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
