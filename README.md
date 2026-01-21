# ROS 2 Sensor Monitoring System

##  Project Overview
This project is a ROS 2 (Robot Operating System 2) based sensor monitoring system developed using Python.
It demonstrates the publisher–subscriber communication model, 
where one node publishes simulated sensor data and another node monitors that data in real time.

The project is built using ROS 2 Humble and uses the `rclpy` client library.

---

##  System Architecture

- **Sensor Publisher Node**
  - Publishes temperature values every second
  - Simulates a real temperature sensor
  - Publishes data on the `/temperature` topic

- **Sensor Subscriber Node**
  - Subscribes to the `/temperature` topic
  - Logs normal temperature values
  - Raises warnings if temperature exceeds a threshold

- **Launch File**
  - Starts both nodes simultaneously using a single command

---

##  Technologies Used

- ROS 2 Humble
- Python (rclpy)
- ROS Topics
- ROS Launch System
- Linux / WSL

---

##  Project Structure

```
sensor_monitor/
├── sensor_monitor/
│   ├── __init__.py
│   ├── publisher.py
│   └── subscriber.py
├── launch/
│   └── sensor_launch.py
├── package.xml
├── setup.py
├── setup.cfg
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Build the package
```bash
cd ~/ros2_humble
colcon build --packages-select sensor_monitor
source install/setup.bash


### 2. Run using launch file
```bash
ros2 launch sensor_monitor sensor_launch.py


### Sample Output

- Publisher prints temperature values every second
- Subscriber prints:
  - INFO for normal temperature values
  - WARN for high temperature values

---


## Learning Outcomes

- Understanding ROS 2 nodes
- Publisher–Subscriber communication
- Topic-based message exchange
- Launching multiple nodes together
- Logging and runtime monitoring


---


# Author

Priyanshu Aryan
priyanshuaryan2411@gmail.com
