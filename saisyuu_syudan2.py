import cv2
import numpy as np
import sys

cap = cv2.VideoCapture(2)

lower_yellow = np.array([20, 50, 30])
upper_yellow = np.array([100, 255, 255])

gaussian =7
num = 0

def video2frame(cap):
    ret, frame = cap.read()
    image = frame
    return image
    
def channels(image):
    if len(image.shape) == 3:
        height, width, channels = image.shape[:3]
        print channels
    else:
        height, width = image.shape[:2]
        channels = 1
        print channels

def masking(image, num):
    image = cv2.GaussianBlur(image, (gaussian, gaussian), 0)
    h, w = image.shape[:2]

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    aim2masking_color = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    mask = cv2.bitwise_not(image, image, mask=aim2masking_color)
    mask = cv2.bitwise_not(aim2masking_color)
    
    bgr = cv2.split(image)
    
    img_alpha = cv2.merge(bgr+[mask])
    print mask
    cv2.imshow("test", mask)
    cv2.imwrite("test_%d.png"%(num), img_alpha)
    
    cv2.waitKey(1)


def main(cap, num):
    masking(video2frame(cap), num)

while True:
    main(cap, num)
    num += 1

cap.release()
cv2.destroyAllWindows()
