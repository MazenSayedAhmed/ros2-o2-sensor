# ============================
# Dockerfile for O2 Sensor Node
# ============================

# 1. Use an official ROS2 image as base
FROM ros:humble-ros-base

# 2. Set working directory inside container
WORKDIR /ros2_ws

# 3. Copy your ROS2 package source code into container
COPY src ./src

# 4. Install dependencies and build the workspace
RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

# 5. Build ROS2 workspace
RUN . /opt/ros/humble/setup.sh && colcon build

# 6. Source environment automatically when container starts
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "source /ros2_ws/install/setup.bash" >> ~/.bashrc

# 7. Default command when container runs
CMD ["bash", "-c", "source /opt/ros/humble/setup.bash && source install/setup.bash && ros2 run o2_sensor_pkg o2_sensor_node"]
