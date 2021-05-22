import cv2
import mediapipe as mp
import time
import numpy as np
import HandTrackingModule as htm


#########################
wCam, hCam = 640, 480
#########################


cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon= 0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img , draw = False)
    if len(lmList) != 0:
        print(lmList[4], lmList[4])
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        cv2.circle(img, (x1, y1), 7, (220, 50, 220), cv2.FILLED)
        cv2.circle(img, (x2, y2), 7, (220, 50, 220), cv2.FILLED)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255, 0, 0), 3)

    cv2.imshow("Img",img)
    cv2.waitKey(1)