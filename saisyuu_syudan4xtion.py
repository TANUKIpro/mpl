#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
import cv2
import numpy as np
import os, sys
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from message_filters import Subscriber, ApproximateTimeSynchronizer, TimeSynchronizer

CAPTURE_RATE = 5.

class Capture_color:
    def __init__(self, path):
        self.bridge = CvBridge()        
        image_sub = Subscriber('image', Image)
        self.sub = ApproximateTimeSynchronizer([image_sub], 10, .5)        
        
        self.path = path
        self.count = 0
        dirname = os.path.dirname(path)
        basename = os.path.basename(path)
        files = filter(lambda x: x.startswith(basename) and x.endswith('.png'), os.listdir(dirname))
        if files:
            nums = [f.strip('.png').split('_')[-1] for f in files if '_' in f]
            nums = [int(num) for num in nums if num.isdigit()]
            if nums:
                self.count = max(nums) + 1
    
    def image_save(self, image):
        filename = self.path + '_%04d.png'%self.count
        cv2.imwrite(filename, image)
        self.count += 1
        
    def start(self):
        self.sub.callbacks.clear()
        self.rate = rospy.Rate(CAPTURE_RATE)
        self.sub.registerCallback(self.callback)
        
    def color_trim(self, image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        lower_blue = np.array([])
        upper_blue = np.array([])
        
        img_mask = cv2.inRange(hsv, lower_blue, upper_blue)
        img_color = cv2.bitwise_and(image, image, mask=img_mask)
        
    def callback(self, image):
        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(image, 'bgr8')
        except CvBridgeError as e:
            rospy.logerr(e)
        
        #self.image_save(self.cv_image)
        image = color_trim(self.cv_image)
        print "callback"
        cv2.imshow("image", image)
        cv2.waitKey(1)
    
if __name__ == '__main__':
    path = sys.argv[1]
    rospy.init_node('capture_image')
    cap_color = Capture_color(path)
    rospy.loginfo('Images will be saved as "{}_xxxx.png."'.format(path))
    while not rospy.is_shutdown():
        cap_color.start()
    rospy.spin()
