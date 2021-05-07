import cv2 as cv
import numpy as np

img = cv.imread('cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype= 'uint8')
cv.imshow('Blank Image', blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2 + 45) , 100, 255, -1)
cv.imshow("Mask", mask)

masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow("Masked", masked)



print(img.shape)



cv.waitKey(0)