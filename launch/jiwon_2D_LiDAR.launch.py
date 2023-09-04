
import os

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package='2D_clustering',
                executable='jiwon_2D_LiDAR_clustering',
                name='jiwon_2D_LiDAR_clustering',
                output='screen',
                emulate_tty=True,
                parameters=[
                    {"x_LiDAR": 50},
                    {"y_LiDAR": 300},
                ],
            ),
        ]
    )