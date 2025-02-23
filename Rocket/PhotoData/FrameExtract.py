import cv2

# Opens the Video file
cap= cv2.VideoCapture('/home/pi/Desktop/Rocket/PhotoData/Targit3.avi')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('3'+str(i)+'.jpg',frame)
    i+=1

cap.release()
cv2.destroyAllWindows()