#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from task4.action import Custom

class Client(Node):
    def __init__(self):
        super().__init__('client')
        self.client=ActionClient(self,Custom,'server')

    def send_goal(self, target):

        goal_msg = Custom.Goal()
        goal_msg.target = target

        self.client.wait_for_server()

        future = self.client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback)

        rclpy.spin_until_future_complete(self, future)
        
        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return

        self.get_logger().info('Goal accepted')

        result_future = goal_handle.get_result_async()
    
        rclpy.spin_until_future_complete(self, result_future)

        result = result_future.result().result

        self.get_logger().info(f'Result: {result.status}')

    def feedback_callback(self, feedback_msg):

        feedback = feedback_msg.feedback

        self.get_logger().info(
            f'Countdown: {feedback.current_count}')


def main(args=None):
    rclpy.init(args=args)

    obj =Client()
    obj.send_goal(10)
    rclpy.spin(obj)
    obj.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
