import cv2

image = cv2.imread("cats.jpg")

# Window name in which image is displayed
window_name = 'Image'

# Using cv2.copyMakeBorder() method
image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[0,0,200])
# up, down, left, right
# Displaying the image


cv2.imshow(window_name, image)
cv2.waitKey(0)