from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sensor_monitor',
            executable='sensor_pub',
            name='sensor_publisher',
            output='screen'
        ),
        Node(
            package='sensor_monitor',
            executable='sensor_sub',
            name='sensor_subscriber',
            output='screen'
        ),
    ])
