#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import numpy as np
import os, sys

img = cv2.imread('apple_0000.png', cv2.IMREAD_UNCHANGED)
h, w, c = img.shape[:3]
alpha_array = np.zeros((h, w), dtype = 'uint8')
# len(img) => 70
# h => 70, w => 72, c => 4

for i in range(0, h):
    for j in range(0, w):
        alpha_array[i][j] = img[i][j][3]

print img[0][0]
print alpha_array[0]

print img.dtype
print alpha_array.dtype
