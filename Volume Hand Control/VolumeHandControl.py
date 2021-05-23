import cv2
import mediapipe as mp
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#########################
wCam, hCam = 640, 480
#########################


cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon= 0.7)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
volume.SetMasterVolumeLevel(-05.0, None)
minVol, maxVol = volRange[0], volRange[1]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img , draw = False)
    if len(lmList) != 0:
        # print(lmList[4], lmList[4])
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img, (x1, y1), 7, (220, 50, 220), cv2.FILLED)
        cv2.circle(img, (x2, y2), 7, (220, 50, 220), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (220, 50, 220), 3)
        cv2.circle(img, (cx, cy), 7, (220, 0, 220), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        # print(length)
        vol = np.interp(length, [50, 300], [minVol, maxVol])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(img, (cx, cy), 7, (0, 220, 0), cv2.FILLED)

    # cv2.rectangle(img, (50))

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255, 0, 0), 3)

    cv2.imshow("Img",img)
    cv2.waitKey(1)