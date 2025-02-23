

import cv2
import numpy as np
import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) #read the pin as board instead of BCM pin


LinearActuatorDir = 18
LinearActuatorStepPin = 16

LinearActuatorDir1 = 11
LinearActuatorStepPin1 = 13

GPIO.setwarnings(False)
GPIO.setup(LinearActuatorDir, GPIO.OUT)
GPIO.setup(LinearActuatorStepPin, GPIO.OUT)

GPIO.setup(LinearActuatorDir1, GPIO.OUT)
GPIO.setup(LinearActuatorStepPin1, GPIO.OUT)


#Change this depends on your stepper motor
Speed = 0.000000000045



recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'Zak', 'Aidan', 'Ilza', 'Z', 'W'] 

CamWidth = 640
CamHeight = 480
StepsPerRotation = 6400
HorizontalFieldOfVeiw = 62.2
VerticalFieldOfVeiw = 48.2

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_BUFFERSIZE, 1)
cam.set(3, CamWidth) # set video widht
cam.set(4, CamHeight) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
frame_rate = 60
prev = 0





StepsPerDegree = StepsPerRotation / 360
pixelsPerDegreeH = CamWidth / HorizontalFieldOfVeiw
pixelsPerDegreeV = CamHeight / VerticalFieldOfVeiw

JumpH = pixelsPerDegreeH / StepsPerDegree
JumpV = pixelsPerDegreeV / StepsPerDegree


while True:
    
    
    time_elapsed = time.time() - prev
    ret, img =cam.read()
    img = cv2.flip(img, -1) # Flip vertically

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    if time_elapsed > 1./frame_rate:
        prev =time.time()
        
        
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )
    
    
    
        for(x,y,w,h) in faces:
            
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            confidence = 100 - confidence
            
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            
            cv2.circle(img, (int(x+(w/2)),int(y)),3,(0,255,0), 5)
            cv2.circle(img, (int(x+w/2),int(y+h)),3,(0,255,0), 5)
            cv2.circle(img, (int(x+w),int(y+(h/2))),3,(0,255,0), 5)
            cv2.circle(img, (int(x),int(y+h/2)),3,(0,255,0), 5)
            
            cv2.line(img, (320,0), (int(x+(w/2)),int(y)),(0,255,0),2)
            cv2.line(img, (320,480), (int(x+w/2),int(y+h)),(0,255,0),2)
            cv2.line(img, (640,240), (int(x+w),int(y+(h/2))),(0,255,0),2)
            cv2.line(img, (0,240), (int(x),int(y+h/2)),(0,255,0),2)
            
            #top -
            AYdif = int(y)
            #bot +
            BYdif = int(y+h)-480
            YP = AYdif + BYdif
            cv2.putText(img, str(YP), (x+w+15,y+h +15), font, 1, (255,255,255), 2)
            
            #right
            CXdif = int(x+w)-640
            #left
            DXdif = int(x)
            XP = CXdif + DXdif
            cv2.putText(img, str(XP), (x+w+15,y+15), font, 1, (255,255,255), 2)
            
            
            
            if (confidence > 8)and(id > 0):    
                        if (XP > 10):
                            for i in range (int(XP*JumpH)):
                                GPIO.output(LinearActuatorDir, 0)
                                GPIO.output(LinearActuatorStepPin, 1)
                                time.sleep(Speed)
                                GPIO.output(LinearActuatorStepPin, 0)
                                time.sleep(Speed)
                        if (XP < -10):
                            for i in range (abs(int(XP*JumpH))):
                                GPIO.output(LinearActuatorDir, 1)
                                GPIO.output(LinearActuatorStepPin, 1)
                                time.sleep(Speed)
                                GPIO.output(LinearActuatorStepPin, 0)
                                time.sleep(Speed)
                        if (YP < -10):
                            for i in range (abs(int(YP*JumpV/2))):
                                GPIO.output(LinearActuatorDir1, 0)
                                GPIO.output(LinearActuatorStepPin1, 1)
                                time.sleep(Speed)
                                GPIO.output(LinearActuatorStepPin1, 0)
                                time.sleep(Speed)
                        if (YP > 10):
                            for i in range (abs(int(YP*JumpV/2))):
                                GPIO.output(LinearActuatorDir1, 1)
                                GPIO.output(LinearActuatorStepPin1, 1)
                                time.sleep(Speed)
                                GPIO.output(LinearActuatorStepPin1, 0)
                                time.sleep(Speed)
 

            # Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(confidence))
            
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
        cv2.imshow('camera',img) 

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
