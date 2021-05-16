import cv2
import numpy as np

img = cv2.imread('cats.jpg')
dst = cv2.detailEnhance(img, sigma_s=20, sigma_r=0.50)
# sigma_s controls how much the image is smoothed - the larger its value,
# the more smoothed the image gets, but it's also slower to compute.
# sigma_r is important if you want to preserve edges while smoothing the image.
# Small sigma_r results in only very similar colors to be averaged (i.e. smoothed),
# while colors that differ much will stay intact.
kernel_sharpening = np.array([[-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]])
dst2 = cv2.filter2D(img, -1, kernel_sharpening)
cv2.imshow("Image", img)
cv2.imshow("Detail_Enhance", dst)
cv2.imshow("Kernel", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
