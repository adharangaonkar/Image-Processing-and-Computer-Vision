import cv2
import numpy as np

img = cv2.imread('cats.jpg')
original = img.copy()
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert image to HSV color space
hsv = np.array(hsv, dtype = np.float64)
hsv[:,:,1] = hsv[:,:,1]*1.50 # scale pixel values up for channel 1
hsv[:,:,1][hsv[:,:,1]>255]  = 255
hsv[:,:,2] = hsv[:,:,2]*1.50 # scale pixel values up for channel 2
hsv[:,:,2][hsv[:,:,2]>255]  = 255
hsv = np.array(hsv, dtype = np.uint8)
img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # converting back to BGR used by OpenCV

cv2.imshow("original", original)
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()