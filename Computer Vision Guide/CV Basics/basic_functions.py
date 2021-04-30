import cv2 as cv

img = cv.imread('park.jpg')

cv.imshow('Park', img)

# Converting to grayscale
gray = cv.cvtColor(src=img, code= cv.COLOR_BGR2GRAY)
# cv.imshow("Grayscale", gray)

# Blur an image (to remove the noise in the image)
blur = cv.GaussianBlur( img, (3,3),cv.BORDER_DEFAULT)
# ksize has to be an odd number, more the ksize more the blur
# cv.imshow("Gaussian Blur", blur)

# Edge Cascade (to find the edges in the image)
canny = cv.Canny(blur, 125, 175)
# cv.imshow("Canny", canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations= 1)
# cv.imshow("Dilated", dilated)

# Eroding (to convert the dilated image back to Canny)
eroded = cv.erode(dilated, (3,3), iterations =1)
# cv.imshow("Eroded", dilated)


# Resize
resize = cv.resize(img, (500,500), interpolation= cv.INTER_AREA)
"""
INTER_LINEAR
INTER_CUBIC
for interpolation to bigger image. 
Cubic is slowest,but tends to give the best image quality
"""
cv.imshow("Resized", resize)


# Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)


cv.waitKey(0)