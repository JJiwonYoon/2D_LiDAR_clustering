#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
import rclpy
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup
from sensor_msgs.msg import LaserScan as LiDAR
import numpy as np
import math
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

class clustering(Node):
    def __init__(self):
        super().__init__('clustering_node')
        self.x_LiDAR        = 200 #mm
        self.y_LiDAR        = 300
        self.distance       = 0   #mm
        self.RC_group = ReentrantCallbackGroup()
        self.create_subscription(LiDAR,'/scan',self.LiDAR_callback,1, callback_group=self.RC_group)
        self.publisher_ = self.create_publisher(Marker, 'marker', 10)
        self.timer = self.create_timer(0.1, self.publish_marker)
        self.marker_id = 0
        self.marker_to_delete = None

    def publish_marker(self):
        if self.marker_to_delete is not None:
            delete_marker = Marker()
            delete_marker.header.frame_id = "map"
            delete_marker.header.stamp = self.get_clock().now().to_msg()
            delete_marker.id = self.marker_to_delete
            delete_marker.action = Marker.DELETE
            self.publisher_.publish(delete_marker)
            self.marker_to_delete = None
        if self.x_filter != 0.0 :
            marker = Marker()
            marker.header.frame_id = "map"
            marker.header.stamp = self.get_clock().now().to_msg()
            marker.id = self.marker_id
            marker.type = Marker.SPHERE
            marker.action = Marker.ADD
            marker.pose.position.x = round(self.x_filter/10,1)
            marker.pose.position.y = round(self.y_filter/10,1)
            marker.pose.position.z = 0.0
            marker.pose.orientation.x = 0.0
            marker.pose.orientation.y = 0.0
            marker.pose.orientation.z = 0.0
            marker.pose.orientation.w = 1.0
            marker.scale.x = 1.0
            marker.scale.y = 1.0
            marker.scale.z = 1.0
            marker.color.a = 1.0
            marker.color.r = 144.0
            marker.color.g = 238.0
            marker.color.b = 144.0
            self.publisher_.publish(marker)
            self.marker_to_delete = self.marker_id
            self.marker_id += 1

    def LiDAR_callback(self,msg):
        self.x_filter       = 0
        self.y_filter       = 0
        self.converted_data = []
        self.distance_data  = []
        self.lidar_data = msg.ranges
        self.lidar_angle_increment = msg.angle_increment
        for i in range(len(self.lidar_data)):
            angle = (self.lidar_angle_increment * i)
            x = -np.sin(angle) * self.lidar_data[i] * 1000
            y = np.cos(angle) * self.lidar_data[i] * 1000
            if (abs(x) < self.x_LiDAR) & (y > 0) & (y < self.y_LiDAR): #mm
                self.converted_data.append([x,y])
                self.distance = (math.sqrt(x*x + y*y))
                self.distance_data.append(self.distance)
                x_values = [item[0] for item in self.converted_data]
                y_values = [item[1] for item in self.converted_data]
                self.x_filter = sum(x_values) / len(x_values)
                self.y_filter = sum(y_values) / len(y_values)
                print("x_filter:", self.x_filter,"y_filter:", self.y_filter)

def main():
        rclpy.init()
        C = clustering()
        try:
            rclpy.spin(C)
        finally:
            C.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()