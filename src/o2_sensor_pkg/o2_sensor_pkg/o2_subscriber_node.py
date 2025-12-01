#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class O2Subscriber(Node):
    def __init__(self):
        super().__init__("o2_subscriber")

        # Subscribe to the SAME topic as your publisher
        self.subscription = self.create_subscription(
            Float32,
            'o2_sensor/data',
            self.callback,
            10
        )

    def callback(self, msg):
        print(f'✅ o2 sensor data: {msg.data:.2f}%')
        # 🔥 Subscriber also prints warnings
        if msg.data < 19.0 or msg.data > 23.0:
            print(f'⚠️  warn o2 sensor data: {msg.data:.2f}%')

def main(args=None):
    rclpy.init(args=args)
    node = O2Subscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
