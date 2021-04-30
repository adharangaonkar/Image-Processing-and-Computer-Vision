import cv2 as cv
import numpy as np

img = cv.imread('park.jpg')

cv.imshow('Park', img)


# Translation
def translation(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translation(img, 100, 100)
cv.imshow("Translated", translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, scale=1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 15)
cv.imshow("Rotated", rotated)


# Resizing
resized = cv.resize(src=img, dsize=(700,700), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

resized1 = cv.resize(src=img, dsize=(700,700), interpolation=cv.INTER_LINEAR)
cv.imshow("Resized1", resized1)

#Flipping
flipped = cv.flip(img, 1)
cv.imshow("Flipped", flipped)
# flipcodes
# 0: vertically
# 1: horizontally
# -1 : on both axes

# Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)



cv.waitKey(0)
