import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Graysacle', gray)

gray_hist = cv.calcHist([gray], channels = [0], mask = None, histSize= [256]
                        , ranges= [0,256])

# For histogram of a mask
blank = np.zeros(img.shape[0:2], dtype = 'uint8')


thickness = [-1, 1, 2, 3]
circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, thickness[0])
# cv.imshow('Mask', circle)

mask = cv.bitwise_and(gray, gray, mask= circle)
cv.imshow('Mask', mask)

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('Number of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# Color Histogram

colors = ('b', 'g', 'r')
plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i],  mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()


cv.waitKey(0)