import cv2

cap = cv2.VideoCapture(0)
while True:
    
    ret, frame = cap.read()
    if ret:
        print(frame)
        cv2.waitKey(1)
    else:
        print("unable to open camera")
        break
cap.release()
