import numpy as np
import cv2
import time


cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

out = cv2.VideoWriter('Targit3.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10.0, (1920,1080))




while 1:
    ret, img = cap.read()
    cv2.imshow('img',img)       
    #img = cv2.flip(img, -1)
    out.write(img)
    