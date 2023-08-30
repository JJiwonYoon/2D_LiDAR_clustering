#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
import rclpy
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup
from sensor_msgs.msg import LaserScan as LiDAR
import numpy as np
import math

class clustering(Node):
    def __init__(self):
        super().__init__('clustering_node')
        self.x_LiDAR        = 200 #mm
        self.y_LiDAR        = 300
        self.distance       = 0   #mm
        self.RC_group = ReentrantCallbackGroup()
        self.create_subscription(LiDAR,'/scan',self.LiDAR_callback,1, callback_group=self.RC_group)

    def split_into_pairs(self,lst):
        pairs = [lst[i:i+2] for i in range(0, len(lst) - 1, 2)]
        if len(lst) % 2 == 1:
            pairs[-1:1].append([lst[-1]])
        return pairs

    def LiDAR_callback(self,msg):
        self.converted_data = []
        self.distance_data  = []
        self.filtered_data  = []
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
                pairs = self.split_into_pairs(self.distance_data)
                if len(pairs) > 0:
                    for i in range(len(pairs)):
                        if abs(pairs[i][0] - pairs[i+1][1]) > 0.5:
                            print("!") 

                # for i in range(len(self.distance_data)):

                #     if abs(self.distance_data[i] - self.distance_data[i-1]) > 100:
                #         print(f'{self.distance_data}')
                #     else:
                #         pass
                # 

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