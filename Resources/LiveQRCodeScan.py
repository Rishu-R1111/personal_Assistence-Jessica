import cv2
import numpy as np
import webbrowser
import pyzbar.pyzbar as pyzbar
import re

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
     frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        dat = obj.data
        print(str(dat))
        
        
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 0, 0), 3)

    cv2.imshow("QR Code Scanner", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break