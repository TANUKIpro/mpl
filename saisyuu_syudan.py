#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np
import time

cap = cv2.VideoCapture(2)
num = 0
while True:
	ret, frame = cap.read()
	print frame
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	lower_yellow = np.array([20, 50, 50])
	upper_yellow = np.array([100, 255, 255])
	
	img_mask = cv2.inRange(hsv, lower_yellow, upper_yellowc)
	
	img_color = cv2.bitwise_not(frame, frame, mask=img_mask)
	mask_rgb = cv2.cvtColor(img_color, cv2.COLOR_GRAY2RGB)
	
	
	
	cv2.imshow("test", mask_rgb)
	#cv2.imwrite("test_%d.png"%(num), img_color)
	cv2.waitKey(1)
	
	num += 1

cap.release()
cv2.destroyAllWindows()
