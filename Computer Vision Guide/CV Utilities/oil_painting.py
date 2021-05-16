import cv2
img = cv2.imread('cat.jpg')


res = cv2.xphoto.oilPainting(img, 3, 1)

cv2.imshow("Oil Painting", res)
cv2.waitKey(0)