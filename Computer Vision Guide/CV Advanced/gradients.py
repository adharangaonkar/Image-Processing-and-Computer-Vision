import cv2 as cv
import numpy as np


img = cv.imread('cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Graysacle', gray)

# Laplacian Edges
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobelX = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelX, sobelY)

cv.imshow('Sobel X', sobelX)
cv.imshow('Sobel Y', sobelY)
cv.imshow('Combined Sobel', combined_sobel)





cv.waitKey(0)
