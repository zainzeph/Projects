
import time
import RPi.GPIO as GPIO
import numpy as np
import cv2



#GPIO.setmode(GPIO.BOARD)
#LinearActuatorDir = 12
#GPIO.setup(LinearActuatorDir, GPIO.OUT)
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('cascade.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
#out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), 20.0, (640,480))
Loopcount = 0
T4 = 0


while 1:
    T1 = time.time()
    ret, img = cap.read()
    #img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #out.write(img)
    #GPIO.output(LinearActuatorDir, GPIO.LOW)
    
    x = 80
    while x < 640:
        
        img = cv2.line(img, (x,0), (x,480), (0,0,0), 5)
        x = x + 80
        
    y = 80
    while y < 480:
        
        img = cv2.line(img, (0,y), (640,y), (0,0,0), 5)
        y = y + 80

        
    for (x,y,w,h) in faces:
        cv2.circle(img, (int(x+(w/2)),int(y+h/2)),3,(0,255,0), 5)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        print (int(x+w/2), int(y+h/2))
        
        
        #GPIO.output(LinearActuatorDir, GPIO.HIGH)
        
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
            #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    #imgR = cv2.flip(img, 1)
    Loopcount = Loopcount + 1
    print (Loopcount)
    T2 = time.time()
    T3 = T2 - T1
    T4 = T4 + T3
    T5 = T4 / Loopcount
    print("Time it took this loop")
    print(T3)
    print("Avrage so far")
    print(T5)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
    
GPIO.output(LinearActuatorDir, GPIO.LOW)
cap.release()
out.release()
cv2.destroyAllWindows()
