from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='task4', executable='server.py'),
        Node(package='task4', executable='client.py')
    ])
