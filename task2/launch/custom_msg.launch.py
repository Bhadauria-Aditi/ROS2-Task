from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='task2', executable='publisher.py'),
        Node(package='task2', executable='subscriber.py')
    ])
