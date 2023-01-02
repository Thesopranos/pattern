# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:10:38 2021

@author: Mertcan
"""
import sys
import cv2
import numpy as np

aRRAYH = 250

ball = {"x":20, "y":3, "xIncreasing":2, "yIncreasing":3, "updown":False, "leftright":False}

"""
    x: x coordinate of the ball
    y: y coordinate of the ball
    xIncreasing: x coordinate of the ball will increase by this value
    yIncreasing: y coordinate of the ball will increase by this value
    updown: reverses whether the ball is going down or up
    leftright: reverses whether the ball is going left or right
"""

for i in sys.argv:
    if i == "-size":
        aRRAYH = int(sys.argv[sys.argv.index(i)+1])
    elif i == "-s":
        aRRAYH = int(sys.argv[sys.argv.index(i)+1])
    elif i == "-x":
        ball["x"] = int(sys.argv[sys.argv.index(i)+1])
    elif i == "-y":
        ball["y"] = int(sys.argv[sys.argv.index(i)+1])
    elif i == "--xIncreasing":
        ball["xIncreasing"] = int(sys.argv[sys.argv.index(i)+1])
    elif i == "-xI":
        ball["xIncreasing"] = int(sys.argv[sys.argv.index(i)+1])
    elif i == "--yIncreasing":
        ball["yIncreasing"] = int(sys.argv[sys.argv.index(i)+1])
    elif i == "-yI":
        ball["yIncreasing"] = int(sys.argv[sys.argv.index(i)+1])
    elif i == "--updown":
        ball["updown"] = sys.argv[sys.argv.index(i)+1]
    elif i == "-uD":
        ball["updown"] = sys.argv[sys.argv.index(i)+1]
    elif i == "--leftright":
        ball["leftright"] = sys.argv[sys.argv.index(i)+1]
    elif i == "-lR":
        ball["leftright"] = sys.argv[sys.argv.index(i)+1]
    elif i == "--help" or i == "-h":
        print("Usage: python line.py [options]")
        print("Example: python line.py -s 500 -x 20 -y 3 --xIncreasing 2 --yIncreasing 3")
        print("Options:")
        print("  -size or -s: size of the window")
        print("  -x: x coordinate of the ball")
        print("  -y: y coordinate of the ball")
        print("  --xIncreasing or xI: x coordinate of the ball will increase by this value")
        print("  --yIncreasing or yI: y coordinate of the ball will increase by this value")
        print("  --help or -h: show this help message and exit")
        sys.exit(0)

img = np.ones((aRRAYH,aRRAYH),np.uint8)

def videoLoop():
    if ball["x"] <= 0 or ball["x"] >= aRRAYH:
        ball["leftrigth"] = not ball["leftright"]
        ball["xIncreasing"] = -ball["xIncreasing"]
        
    if ball["y"] <= 0 or ball["y"] >= aRRAYH:
        ball["updown"] = not ball["updown"]
        ball["yIncreasing"] = -ball["yIncreasing"]
    
    ball["x"] = ball["x"] + ball["xIncreasing"]
    ball["y"] = ball["y"] + ball["yIncreasing"]
    
    cv2.circle(img,(ball["x"], ball["y"]),1,255,-1)
    
    cv2.imshow("window",img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        return 0
    
    return videoLoop()

videoLoop()
cv2.destroyAllWindows()
