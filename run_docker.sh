#!/bin/bash
# =========================================================
# Script: run_docker.sh
# Purpose: Build and run the ROS2 O2 sensor Docker container
# Usage:
#   chmod +x run_docker.sh
#   ./run_docker.sh
# =========================================================

# Stop script on any error
set -e

# Variables
IMAGE_NAME="o2_sensor_image"
CONTAINER_NAME="o2_sensor_container"

echo "🛠️  Building Docker image: $IMAGE_NAME ..."
docker build -t $IMAGE_NAME .

echo "🚀 Running container: $CONTAINER_NAME ..."
docker run --rm -it --name $CONTAINER_NAME $IMAGE_NAME
