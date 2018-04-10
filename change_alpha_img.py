#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys, time
import cv2
import numpy as np
from tqdm import tqdm
n = 0

def change_img(image, count):
    save_name = save_path + image[:image.find('_')] + '_%04d.png'%count
    img = cv2.imread(image_path + image, cv2.IMREAD_UNCHANGED)
    h, w, c  = img.shape[:3]
    
    blue_c, green_c, red_c, alpha_c = cv2.split(img)
    max_org = np.max(alpha_c)
    alpha_array = np.zeros((h, w))
    
    for i in range(0, h):
            for j in range(0, w):
                alpha_array[i][j] = ((float(img[i][j][3]))/max_org)**0.6
                img[i][j][3] = float(alpha_array[i][j])*255
    
    cv2.imwrite(save_name, img)

image_path = sys.argv[1]
save_path = sys.argv[2]

lng = len(os.listdir(image_path))
for i in tqdm(os.listdir(image_path)):
    change_img(i, n)
    #print i + ' was reshaped (%d/%d)'%(n+1, lng)
    n += 1
    time.sleep(.01)
