import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3

class ProNode(Node):
    def __init__(self):
        super().__init__('processor_node')
        self.sub=self.create_subscription(Vector3,'encoder_data',self.pro,10)
        self.publisher=self.create_publisher(Vector3,'processed_data',10)

    def pro(self,msg):
        avg=(msg.x+msg.y+msg.z)/3
        leng=(msg.x**2+msg.y**2+msg.z**2)**0.5
        msg2=Vector3()
        msg2.x=leng
        msg2.y=avg

        self.publisher.publish(msg2)
        self.get_logger().info(f"procsessor= {msg2.x},{msg2.y}")

def main(args=None):
    rclpy.init(args=args)
    procssor=ProNode()
    rclpy.spin(procssor)
    procssor.destory_node()
    rclpy.shutdown()
    
if __name__=="__main__":
    main()
