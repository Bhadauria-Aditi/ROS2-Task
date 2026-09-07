#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from task2.msg import RoboStatus

class publisher(Node):
    def __init__(self):
        super().__init__("publisher")
        self.publisher=self.create_publisher(RoboStatus,'Status',10)
        self.declare_parameter('publish_rate',1)
        f=self.get_parameter('publish_rate').value
        t=1/f
        self.timer=self.create_timer(t,self.send)

    def send(self):
        msg=RoboStatus()
        msg.robot_name="Chithi"
        msg.battery_level=67.67
        msg.is_moving=True
        msg.error_code=0
        self.publisher.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    obj=publisher()
    rclpy.spin(obj)
    obj.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
