import cv2 as cv
import numpy as np

img = cv.imread('cats.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow('Blank', blank)

# Convert to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Graysacle", gray)

# Blur Image
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("Gaussian Blur", blur)

# Canny Edges
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

# Thresholding is an another way to get contours
# Thresholding
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Threshold", thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# mode: RETR_TREE to find all the hierarchical contours
#       RETR_EXTERNAL to find only the external contours
#       RETR_LIST to get the list of all the contours in the image
print(len(contours))

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

# Draw the contours on a blank image
cv.drawContours(blank, contours, -1, (0, 0, 255), thickness=1)
# -1 : as we want all the contours
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
