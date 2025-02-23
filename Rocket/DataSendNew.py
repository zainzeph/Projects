from serial import Serial
import time
#import numpy as np
import cv2 
from cv2 import cvtColor
from cv2 import CascadeClassifier
from cv2 import VideoCapture

Tick = 0
avrage =  0
face_cascade = CascadeClassifier('Models/1_1_25.xml')
#cap = VideoCapture("output2.avi")
cap = cv2.VideoCapture(0)
#out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), 20.0, (640,480))
#ser = Serial('/dev/ttyUSB0', 115200, timeout=1)




def CodeBlock(A):
    
    ser = Serial('/dev/ttyUSB' + A, 115200, timeout=1)
    ser.flush()
    while 1:
    #T1 = time.time()
        ret, img = cap.read()
        gray = cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        #img = cv2.flip(img, -1)
        for (x,y,w,h) in faces:                
            ser.write ( (str(x+w/2)+','+ str(y+h/2) + '\n') .encode('utf-8'))
            print (str(x+w/2))
            print (str(y+h/2))


try:
    CodeBlock("0")
except:
    CodeBlock("1")



        
        
        
 
#out.release()
#cv2.destroyAllWindows()
