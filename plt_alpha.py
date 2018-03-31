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

    def w_h_c(self, img):
        if len(img.shape) == 3:
            self.height, self.width, self.channels = img.shape[:3]
        else:
            self.height, self.width = img.shape[:2]
            self.channels = 1
        print self.width, self.height, self.channels
    
    def mpl(self):
        self.alpha_array = np.zeros((self.height, self.width))
        self.resize_array = np.zeros((self.height, self.width))
        max_org = np.max(alpha_c)
        
        x = np.arange(0, self.width, 1)
        y = np.arange(0, self.height, 1)
        
        for i in range(0, self.height):
            for j in range(0, self.width):
                #self.alpha_array[i][j] = float(img[i][j][3])/max_org
                self.alpha_array[i][j] = float(img[i][j][3])
                
        #TODO:cv2.split(img)で楽にチャンネルを分解できたでござるよ
        self.alpha_max = np.max(self.alpha_array)
        
        #空の配列「resize_array」に、「alpha_array」の最大値「alpha_max」で割った値をfor文でソート
        for k in range(0, self.height):
            for l in range(0, self.width):
                self.resize_array[k][l] = self.alpha_array[k][l]/self.alpha_max
        
        X, Y = np.meshgrid(x, y)
        Z1 = self.alpha_array
        #Z2 = self.resize_array
        
        fig = plt.figure()
        
        ax1 = Axes3D(fig)
        #ax2 = Axes3D(fig)
        
        ax1.contourf3D(X,Y,Z1)
        #ax2.contourf3D(X,Y,Z2)
        
        ax1.set_title(image)
        #ax2.set_title(image + '-(2)')
        plt.show()
        
    def save_img(self):
        change_channel = np.uint8(np.dstack([img, self.resize_array*255]))
        cv2.imwrite('change_channel.png', change_channel)
        cv2.waitKey(0)
        
def main():
    PA = PlotAlpha(image)
    PA.w_h_c(img)
    PA.mpl()
    #PA.save_img()
    
if __name__ == '__main__':
    image = sys.argv[1]
    #img = cv2.imread(image, -1)
    img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    blue_c, green_c, red_c, alpha_c = cv2.split(img)

    main()
