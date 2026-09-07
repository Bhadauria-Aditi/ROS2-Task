from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='task1',executable='sensor'),
        Node(package='task1',executable='processor'),
        Node(package='task1',executable='logger')
        
    ])
