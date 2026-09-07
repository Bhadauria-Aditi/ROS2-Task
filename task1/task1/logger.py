import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3

class LogNode(Node):
    def __init__(self):
        super().__init__('logger_node')
        self.sub=self.create_subscription(Vector3,'processed_data',self.dis,10)

    def dis(self,msg2):
        self.get_logger().info(f"Logged= {msg2.x},{msg2.y}")

def main(args=None):
    rclpy.init(args=args)
    log=LogNode()
    rclpy.spin(log)
    log.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()
