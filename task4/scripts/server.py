#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from task4.action import Custom
import time

class Server(Node):
    def __init__(self):
        super().__init__('action_server')
        self.server = ActionServer(self,Custom,'server',self.send)

    def send(self, goal_handle):
        self.get_logger().info('Executing goal...')

        feedback=Custom.Feedback()
        for i in range(goal_handle.request.target,0,-1):
            feedback.current_count=i
            goal_handle.publish_feedback(feedback)
            time.sleep(1)

            
        goal_handle.succeed()
        result = Custom.Result()
        result.status="Done!"
        return result


def main(args=None):
    rclpy.init(args=args)
    obj=Server()
    rclpy.spin(obj)
    obj.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


