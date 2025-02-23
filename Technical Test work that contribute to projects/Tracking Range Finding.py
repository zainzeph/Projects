''''
   



'''
import threading
import cv2
import numpy as np
import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) #read the pin as board instead of BCM pin

FIRE = 12
LinearActuatorDir = 11
LinearActuatorStepPin = 13

LinearActuatorDir1 = 18
LinearActuatorStepPin1 = 16

GPIO.setwarnings(False)
GPIO.setup(LinearActuatorDir, GPIO.OUT)
GPIO.setup(LinearActuatorStepPin, GPIO.OUT)

GPIO.setup(LinearActuatorDir1, GPIO.OUT)
GPIO.setup(LinearActuatorStepPin1, GPIO.OUT)

GPIO.setup(FIRE, GPIO.OUT)
GPIO.output(FIRE, GPIO.LOW)

#Change this depends on your stepper motor
Speed = 0.0006



recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "cascade.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX



#Global Variables
StepsPerRotation = 1600
StepsToDegree = StepsPerRotation/360
BoardR = 451
print ('What is the boards size(Normal is 451mm)')
ChangeBordSize = int(input())
A = BoardR/100
B = ChangeBordSize/100
SizeMod = B / A 


BordDiamiter = BoardR/2
CPosition = []
infoStore=[]

#this to add to
# Refrence eg 20, x distance mm , y distance mm
Positions = ['1',9,10,
             '1x2',2,19,
             '1x3',
             '2',
             '2x2',
             '2x3',
             '3',
             '3x2',
             '3x3',
             '4',
             '4x2',
             '4x3',
             '5',
             '5x2',
             '5x3',
             '6',
             '6x2',
             '6x3',
             '7',
             '7x2',
             '7x3',
             '8',
             '8x2',
             '8x3',
             '9',
             '9x2',
             '9x3',
             '10',
             '10x2',
             '10x3',
             '11',
             '11x2',
             '11x3',
             '12',
             '12x2',
             '12x3',
             '13',
             '13x2',
             '13x3',
             '14',
             '14x2',
             '14x3',
             '15',
             '15x2',
             '15x3',
             '16',
             '16x2',
             '16x3',
             '17',
             '17x2',
             '17x3',
             '18',
             '18x2',
             '18,3',
             '19',
             '19x2',
             '19x3',
             '20',
             '20x2',
             '20x3',
             
             20,21,22]
#Diffrence between cam and dart will ned changing
diffrence = 10


FinalSteps = []

CamWidth = 640
CamHeight = 480

CentureY = True
CentureX = True
Ysteps = 0
Xsteps = 0

frame_rate = 60
prev = 0

global Di
Di = 0
newXP = 0
newYP = 0
T1=0

Targits = []

print("Input targit 1")
Targit0 = input()
Targits.append(Targit0)
print("Input targit 2")
Targit1 = input()
Targits.append(Targit1)
print("Input targit 3")
Targit2 = input()
Targits.append(Targit2)

while True:
    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    #cam.set(cv2.CAP_PROP_BUFFERSIZE, -1)
    cam.set(3, CamWidth) # set video widht
    cam.set(4, CamHeight) # set video height
        
    # Define min window size to be recognized an object
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    
    
    time_elapsed = time.time() - prev
    ret, img =cam.read()
    #img = cv2.flip(img, -1) # Flip vertically

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    if time_elapsed > 1./frame_rate:
        prev =time.time()
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )
        
        cam.release()
    
    

        def XAXIS(XP):
            global Xsteps
            global CentureX
            global Di
            Xsteps = 0
            if (XP >= 1):
                for i in range (int(1)):
                    GPIO.output(LinearActuatorDir, 0)
                    GPIO.output(LinearActuatorStepPin, 1)
                    time.sleep(Speed)
                    GPIO.output(LinearActuatorStepPin, 0)
                    time.sleep(Speed)
            if (XP <= -1):
                for i in range (abs(int(1))):
                    GPIO.output(LinearActuatorDir, 1)
                    GPIO.output(LinearActuatorStepPin, 1)
                    time.sleep(Speed)
                    GPIO.output(LinearActuatorStepPin, 0)
                    time.sleep(Speed)
            if (XP==0):
                CentureX = False
                Di = Di + 0.5                                                    
        def YAXIS(YP):
            global Ysteps
            global CentureY
            global Di
            print(YP)
            Ysteps = 0
            if (YP <= -1):
                for i in range (abs(int(1))):
                    GPIO.output(LinearActuatorDir1, 1)
                    GPIO.output(LinearActuatorStepPin1, 1)
                    time.sleep(Speed)
                    GPIO.output(LinearActuatorStepPin1, 0)
                    time.sleep(Speed)
            if (YP >= 1):
                for i in range (abs(int(1))):
                    GPIO.output(LinearActuatorDir1, 0)
                    GPIO.output(LinearActuatorStepPin1, 1)
                    time.sleep(Speed)
                    GPIO.output(LinearActuatorStepPin1, 0)
                    time.sleep(Speed)
            if (YP==0):
                CentureY = False
                Di = Di + 0.5
        
        
        def Info(Steps,T):
            #CPosition = []
            #var = -1
           # for i in Positions:
               # var = var + 1
               # if(i == Targit1) :
                 #   re = 0
                #    while (re < 2) :
                #        CPosition.append((Positions[var + 1]))
                  #      var = var + 1
                  #      re = re + 1
                        
           # X,Y = CPosition
           # print(X)
           ## print(Y)

            #Steps calculation
            #TDistance = int(X)
            StepsToEdge = Steps
            Angle = StepsToEdge / StepsToDegree 
            DistancePerDegree = BordDiamiter / Angle
           # DegreesNeeded = TDistance / DistancePerDegree
           # StepsToTake = StepsToDegree * DegreesNeeded
            
            Distance = (180*BordDiamiter)/(Angle*3.14)
            DistanceTraveledPerStep = BordDiamiter/StepsToEdge
           # StepstoTake2 = TDistance / DistanceTraveledPerStep
            print ('Stepps To Degrees:' , StepsToDegree)#not neede out of function 
            print ('Angle:' , Angle)#
            print ('Distance traveled per step', DistanceTraveledPerStep)
            print ('Distance traveled per degree:' , DistancePerDegree)#not needed out of function
           # print ('Degrees needed to reach targit:' , DegreesNeeded)#not neede out of function
           # print ('Steps to take using angle data:', StepsToTake)# steps needed to hit targit without offsets
           # print ('steps to take using Setp data:',  StepstoTake2)
            print ('Distance to edge of bord:', Distance) # used in balistic calc
            infoStore.append(DistanceTraveledPerStep)
            infoStore.append(Distance)
            
            
        def StepfindL(x,y):
            global Xsteps
            global Ysteps
            global CentureX
            global CentureY
            global Di
            if (y > x) :
                for i in range (int(1)):
                    GPIO.output(LinearActuatorDir, 1)
                    GPIO.output(LinearActuatorStepPin, 1)
                    time.sleep(Speed)
                    GPIO.output(LinearActuatorStepPin, 0)
                    time.sleep(Speed)      
                    Xsteps = Xsteps + 1
            if (y < x) :
                for i in range (int(1)):
                    GPIO.output(LinearActuatorDir, 0)
                    GPIO.output(LinearActuatorStepPin, 1)
                    time.sleep(Speed)
                    GPIO.output(LinearActuatorStepPin, 0)
                    time.sleep(Speed)      
                    Xsteps = Xsteps - 1        
            if (x == y):
                Info(Xsteps,Di)
                Di = Di + 1
                CentureX = True
                CentureY = True
                Xsteps = 0
        def StepfindU(x,y):
            global CentureX
            global CentureY
            global Xsteps
            global Ysteps
            global Di                        
            if (y > x) :
                for i in range (int(1)):
                    GPIO.output(LinearActuatorDir1, 1)
                    GPIO.output(LinearActuatorStepPin1, 1)
                    time.sleep(Speed)
                    GPIO.output(LinearActuatorStepPin1, 0)
                    time.sleep(Speed)      
                    Xsteps = Xsteps + 1
            if (y < x) :
                for i in range (int(1)):
                    GPIO.output(LinearActuatorDir1, 0)
                    GPIO.output(LinearActuatorStepPin1, 1)
                    time.sleep(Speed)
                    GPIO.output(LinearActuatorStepPin1, 0)
                    time.sleep(Speed)      
                    Xsteps = Xsteps - 1    
            if (x == y):
                Info(Xsteps,Di)                   
                Di = Di + 1            
                CentureX = True  
                CentureY = True
                Xsteps = 0
            
        def CordanateAdjust():
            
            #LDTP,LD,RDTP,RD,UDTP,UD,DDTP,DD = infoStore
            #LeftDistanceTraveledPerStep
            
            
            #Relevent Data is taken from a pre set list of positions
            CPosition = []
            for I in range(3):       
                var = -1
                for i in Positions:
                    var = var + 1
                    C = Targits[I]
                    if(i == C) :
                        re = 0
                        while (re < 2) :
                            CPosition.append((Positions[var + 1]))
                            var = var + 1
                            re = re + 1
            
            print(CPosition)
            
            
            #Relevent data is matched with its direction and data modifyed to steps needed
            C = 0
            
            for i in CPosition:
                            Data = CPosition[C]
                            print(Data)
                            if (Data > 0 and i%2==0):
                                Data = Data / infoStore[0]
                                Data = Data * SizeMod
                                FinalSteps.append(Data)
                                
                            if (Data < 0 and i%2==0):
                                Data = Data / infoStore[4]
                                Data = Data * SizeMod
                                FinalSteps.append(Data)
                                
                            if (Data > 0 and i%2==1):
                                Data = Data / infoStore[2]
                                #Cam distance to Barrel
                                Data = Data + (diffrence/infoStore[2])
                                #Balistic calc
                                balisticCalc(Data)
                                Data = balisticCalc()
                                print(Data)
                                #Scall according to bord size
                                Data = Data * SizeMod
                                FinalSteps.append(Data)
                                
                            if (Data < 0 and i%2==1):
                                Data = Data / infoStore[6]
                                Data = Data + (diffrence/infoStore[2])
                                
                            C = C + 1
                            print(Data)    
                
                
          
            #Balistic calc to counter gravity
            
            
            #Adjust 1 step if there is a repete of a number
            #Adjust X and y if diffrent bord dimessions are added
           
        def balisticCalc(Data):
            print (Data)
            Data = Data + 10
            
            return Data
            
           
        def prime():
            
            #spring Primer
            #GPIO.output(12, GPIO.HIGH)
            #time.sleep(10)
            #GPIO.output(12, GPIO.LOW)
            
            #Dart loader
            #GPIO.output(14, GPIO.HIGH)
            #time.sleep(10)
            #GPIO.output(14, GPIO.LOW)
        
        
        for(x,y,w,h) in faces:
                
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            confidence = 100 - confidence
                
                #top -
            AYdif = int(y)
                #bot +
            BYdif = int(y+h)-480
            YP = AYdif + BYdif
                
                #right
            CXdif = int(x+w)-640
                #left
            DXdif = int(x)
            XP = CXdif + DXdif
               
            CX = int(x+(w/2))
            CY = int(y+(h/2))
            print(Di)
                
                
            if (confidence > -10):
                Di
                CentureX
                CentureY
                print(CentureY)
                print(CentureX)
                #if (Di <= 0.5 or Di == 2 or Di == 4 or Di == 6):
                if (CentureX == True):
                    XAXIS(XP)
                    CTX = CX
                if (CentureY == True):
                    YAXIS(YP)
                    CTY = CY
                        
                    
                if (CentureX == False and CentureY == False and Di == 1):           
                    StepfindL(x,int(CTX))
                    #print(Xsteps)
                    #print(CTX)
                    #print(x)
                if (CentureX == False and CentureY == False and Di == 3):
                    StepfindL((x+w),int(CTX))
                    #print(Xsteps)
                    #print(CTX)
                    #print(x+w)
                if (CentureX == False and CentureY == False and Di == 5):
                    StepfindU((y),int(CTY))
                    #print(Xsteps)
                    #print(CTX)
                    #print(x)
                if (CentureX == False and CentureY == False and Di == 7):
                    StepfindU((y+h),int(CTY))
                    #print(Xsteps)
                if (CentureX == False and CentureY == False and Di >= 9 ):
                    Z = threading.Thread(target=prime())
                    Z.start()
                    CordanateAdjust()
                    
                    print(FinalSteps)
                    X = FinalSteps.pop(0)
                    print(FinalSteps)
                    Y = FinalSteps.pop(0)
                    print(X)
                    print(Y)
                    if (X < 0):                        
                        for i in range (abs(int(X))):
                            GPIO.output(LinearActuatorDir1, 1)
                            GPIO.output(LinearActuatorStepPin1, 1)
                            time.sleep(Speed)
                            GPIO.output(LinearActuatorStepPin1, 0)
                            time.sleep(Speed)
                    if (X > 0):                        
                        for i in range (abs(int(X))):
                            GPIO.output(LinearActuatorDir1, 0)
                            GPIO.output(LinearActuatorStepPin1, 1)
                            time.sleep(Speed)
                            GPIO.output(LinearActuatorStepPin1, 0)
                            time.sleep(Speed)                                               
                    if (Y < 0):
                        for i in range (abs(int(Y))):
                            GPIO.output(LinearActuatorDir1, 1)
                            GPIO.output(LinearActuatorStepPin1, 1)
                            time.sleep(Speed)
                            GPIO.output(LinearActuatorStepPin1, 0)
                            time.sleep(Speed)
                    if (Y > 0):
                        for i in range (abs(int(Y))):
                            GPIO.output(LinearActuatorDir1, 0)
                            GPIO.output(LinearActuatorStepPin1, 1)
                            time.sleep(Speed)
                            GPIO.output(LinearActuatorStepPin1, 0)
                            time.sleep(Speed)
                    time.sleep(2)
                    #GPIO.output(12, GPIO.HIGH)
                    time.sleep(3)
                    #GPIO.output(12, GPIO.LOW)
                    CentureX = True  
                    CentureY = True

                       
                        
                        

