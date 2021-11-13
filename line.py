# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:10:38 2021

@author: Mertcan
"""

import cv2
import numpy as np

hl = 250

img = np.ones((hl,hl),np.uint8)

# x is the x value of the ball's starting point
x = 2
# y is the y value of the ball's starting point
y = 3

# n is the increment of x
n = 3
# m is the increment of y
m = 2

# These four variables represent the state of hitting a wall.
ust = 0
alt = 0
sag = 0
sol = 0

while True:
  
    if x <= 0:
        sol = not sol
    
    if x >= hl:
        sag = not sag
        
    if y <= 0:
        ust = not ust
        
    if y >= hl:
        alt = not alt

    if ust == 1 or alt == 1:
        n = -n

    if sag == 1 or sol == 1:
        m = -m

    x  = x + m
    y = y + n
    print(n, alt)
    cv2.circle(img,(x,y),1,255,-1)
    
    cv2.imshow("window",img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
