import cv2

# Opens the Video file
cap= cv2.VideoCapture('output2.avi')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('1'+str(i)+'.jpg',frame)
    i+=1

cap.release()
cv2.destroyAllWindows()
