import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# 1. Paint the image in a certain colour
blank[200:300, 300:400] = 0, 255, 0
# cv.imshow("Green", blank)

# 2. Draw a Rectangle
cv.rectangle(img= blank, pt1 = (0,0), pt2 = (250,500), color=(0,255,0), thickness=2)

# Filled Rectangle
cv.rectangle(img= blank, pt1 = (0,0), pt2 = (250,500), color=(0,255,0), thickness=cv.FILLED)

# or can be done by:-
cv.rectangle(img= blank, pt1 = (0,0), pt2 = (250,500), color=(0,255,0), thickness=-1)

# If pt1 and pt2 are to be defined in fractions of the whole image
cv.rectangle(img= blank, pt1 = (0,0), pt2 = (blank.shape[1]//2, blank.shape[0]//2), color=(0,255,0), thickness=2)

# 3. Draw a Circle
cv.circle(img=blank, center=(250,250), radius= 40, color=(0,0,255), thickness= 2)
# cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(img=blank, pt1= (220,220), pt2= (250,250), color= (0,150,150), thickness= 2)

# 5. Write text on an image
cv.putText(img=blank, text= 'Hello', org= (100,200), fontFace=cv.FONT_HERSHEY_TRIPLEX,
           fontScale= 1.5, color=(255,255,255))

cv.imshow('Rectangle', blank)



cv.waitKey(0)
