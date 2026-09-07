#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from task3.srv import AddTwoInts

class client(Node):
    def __init__(self):
        super().__init__('client')
        self.client = self.create_client(AddTwoInts, 'add')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        
    def send_request(self, a, b):
        req = AddTwoInts.Request()
        req.a = a
        req.b = b
        return self.client.call_async(req)

def main(args=None):
    rclpy.init(args=args)
    obj =client()
    future = obj.send_request(60,7)
    
    rclpy.spin_until_future_complete(obj, future)
    
    response = future.result()
    obj.get_logger().info(f'Response: {response.sum}')
    
    obj.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
