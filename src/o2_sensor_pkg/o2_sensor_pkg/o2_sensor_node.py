#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class O2SensorNode(Node):
    def __init__(self):
        super().__init__('o2_sensor_node')  # Node name
        # Publisher: topic name, message type, queue size
        self.publisher_ = self.create_publisher(Float32, 'o2_sensor/data', 10)
        # Timer: publish every 1 second
        self.timer = self.create_timer(1.0, self.publish_o2_data)

    def publish_o2_data(self):
        msg = Float32()
        msg.data = random.uniform(18.0, 23.0)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing O2 level: {msg.data:.2f}%')

# 🆕 Add this warning section
        if msg.data < 19.0 or msg.data > 23.0:
            self.get_logger().warn(f'⚠️ Abnormal O2 level detected: {msg.data:.2f}%')


def main(args=None):
    rclpy.init(args=args)
    node = O2SensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
