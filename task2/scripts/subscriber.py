#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from task2.msg import RoboStatus

class subscriber(Node):
    def __init__(self):
        super().__init__('status_subscriber')
        self.subscription= self.create_subscription(RoboStatus, 'Status', self.get, 10)

    def get(self,msg):
        self.get_logger().info(f"Robot Name = {msg.robot_name},  Battery= {msg.battery_level}%, Moving= {msg.is_moving}, Err= {msg.error_code}")

def main(args=None):
    rclpy.init(args=args)
    obj=subscriber()
    rclpy.spin(obj)
    obj.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
