#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from frenet_1 import QuarticPolynomial

class Node1(Node):
    def __init__(self):
        super().__init__('node1')
        self.subscription = self.create_subscription(Float32,'topic1',self.callback1,10)

    def callback1(self, msg):
        self.get_logger().info(f'callback1 received: {msg.data}')

def main():
    rclpy.init()

    node1 = Node1()
    try:
        rclpy.spin(node1)

    finally:
        node1.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()