import cv2
cam =cv2.VideoCapture(1)
while True:
    a, frame=cam.read()
    cv2.imshow('mycam',frame)
    cv2.waitKey(1)