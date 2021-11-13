# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:10:38 2021

@author: Mertcan
"""

import cv2
import numpy as np

hl = 250

img = np.ones((hl,hl),np.uint8)

x = 2
y = 3
n = 3
m = 2

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