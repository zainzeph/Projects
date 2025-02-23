import serial
import time
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascade.xml')
cap = cv2.VideoCapture('Test2.mp4')
#cap = cv2.VideoCapture(0)
#out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), 20.0, (640,480))
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
ser.flush()

while True:
    T1 = time.time()
    ret, img = cap.read()
    #img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #out.write(img)
    
    for (x,y,w,h) in faces:
        #cv2.circle(img, (int(x+(w/2)),int(y+h/2)),3,(0,255,0), 5)
        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = img[y:y+h, x:x+w]
        #X = x+w/2
        #Y = y+h/2
        
        #print (int(x+w/2), int(y+h/2))
        #X = (str(X)+','+ str(Y) + '\n')
        #ser.write ( (str(X)+','+ str(Y) + '\n') .encode('utf-8'))
        
        ser.write ( (str(x+w/2)+','+ str(y+h/2) + '\n') .encode('utf-8'))
        #line = ser.readline().decode('utf-8').rstrip()
        #print(line)

        
        
    #cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    T2 = time.time()
    T3 = T2 - T1
    print(T3)
    if k == 27: # press 'ESC' to quit
        break

cap.release()
out.release()
cv2.destroyAllWindows()
