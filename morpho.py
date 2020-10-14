import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    #hue stauration and value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    

    lower_yellow = np.array([30,60,100])
    upper_yellow = np.array([80,255,255])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations = 1)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # tophat -->i/p img  -  open(i/p img)
    # blackhat -->close(i/p img)  -  i/p img

    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap. release()
cv2.destroyAllWindows()