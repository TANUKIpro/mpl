#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
import cv2
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class PlotAlpha:
    def __init__(self, image):
        self.image = image
        self.img = img
        self.width = 0
        self.height = 0
        self.channels = 0
        self.alpha_max = 0.
        self.gamma = 2.

    def w_h_c(self, img):
        if len(img.shape) == 3:
            self.height, self.width, self.channels = img.shape[:3]
        else:
            self.height, self.width = img.shape[:2]
            self.channels = 1
        print self.width, self.height, self.channels
    
    def mpl(self):
        self.LookUpTable = np.zeros((256, 1), dtype = 'uint8')
        self.alpha_array = np.zeros((self.height, self.width))
        self.resize_array = np.zeros((self.height, self.width))
        max_org = np.max(alpha_c)
        print max_org
        print img[0]
        
        for i in range(0, self.height):
            for j in range(0, self.width):
                self.alpha_array[i][j] = ((float(img[i][j][3]))/max_org)**0.3
                img[i][j][3] = float(self.alpha_array[i][j])*255
                
        
        self.alpha_max = np.max(self.alpha_array)
        #cv2.imwrite('alpha_test_img.png', img)
        #-------------------------------------------------------------------#
        cv2.imwrite('alpha**0.3_test_img.png', img)
        
        
        '''#-------------------------------------------------------------------#
        
        for k in range(256):
            self.LookUpTable[k][0] = 255*pow(float(i)/255, 1.0/self.gamma)
        img_gamma = cv2.LUT(img, self.LookUpTable)
        
        cv2.imwrite('gamma_test_img.png', img_gamma)
        
        '''#-------------------------------------------------------------------#
        
def main():
    PA = PlotAlpha(image)
    PA.w_h_c(img)
    PA.mpl()
    
if __name__ == '__main__':
    image = sys.argv[1]
    #img = cv2.imread(image, -1)
    img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    blue_c, green_c, red_c, alpha_c = cv2.split(img)
    main()
