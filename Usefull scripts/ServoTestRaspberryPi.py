import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)



LinearActuatorDir = 40
LinearActuatorStepPin = 38

LinearActuatorDir1 = 16
LinearActuatorStepPin1 = 18

GPIO.setwarnings(False)
GPIO.setup(LinearActuatorDir, GPIO.OUT)
GPIO.setup(LinearActuatorStepPin, GPIO.OUT)

GPIO.setup(LinearActuatorDir1, GPIO.OUT)
GPIO.setup(LinearActuatorStepPin1, GPIO.OUT)




while True:
    
    GPIO.output(LinearActuatorDir1, 0)
    GPIO.output(LinearActuatorStepPin1, 1)
    time.sleep(0.01)
    GPIO.output(LinearActuatorStepPin1, 0)
    time.sleep(0.01)
    print("done")
    

    




