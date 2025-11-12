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
        base_o2 = 21.0
        msg.data = base_o2 + random.uniform(-0.5, 0.5)  # simulate fluctuation
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing O2 level: {msg.data:.2f}%')

def main(args=None):
    rclpy.init(args=args)
    node = O2SensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
