
import cv2

im = cv2.imread("cats.jpg")

roi = cv2.selectROI(im)

print(roi)

im_cropped = im[int(roi[1]):int(roi[1] + roi[3]),
             int(roi[0]):int(roi[0] + roi[2])]

cv2.imshow("Cropped Image", im_cropped)
cv2.waitKey(0)
