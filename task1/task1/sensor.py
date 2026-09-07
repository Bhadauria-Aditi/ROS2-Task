
import rclpy
from rclpy.node import Node
from geometry_msgs.msg  import Vector3
class SenNode(Node):
    def __init__(self):
        super().__init__("sensor")
        self.publisher=self.create_publisher(Vector3, 'encoder_data', 10)
        self.declare_parameter('publish_rate',2)
        f=self.get_parameter('publish_rate').value
        t=1/f
        self.timer=self.create_timer(t, self.send)
    def send(self):
        msg=Vector3()
        msg.x=1.0;
        msg.y=2.0
        msg.z=3.0
        self.publisher.publish(msg)
        self.get_logger().info(f"Sensor data={msg.x},{msg.y},{msg.z}")
        
    
def main(args=None):
    rclpy.init(args=args)
    obj=SenNode()
    rclpy.spin(obj)
    obj.destroy_node()
    rclpy.shutdown()
    
if __name__=="__main__":
    main()
