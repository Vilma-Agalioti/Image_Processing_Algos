import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_8U)
    sobelx = cv2.Sobel(frame, cv2.CV_8U, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_8U, 0, 1, ksize=5)
    edges = cv2.Canny(frame, 200, 100)

    cv2.imshow('frame', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('edges', edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()