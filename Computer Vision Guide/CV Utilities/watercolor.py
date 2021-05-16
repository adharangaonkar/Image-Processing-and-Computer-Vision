import cv2

img = cv2.imread('cats.jpg')
res = cv2.stylization(img, sigma_s=150, sigma_r=0.6)
# sigma_s controls the size of the neighborhood. Range 1 - 200
# sigma_r controls the how dissimilar colors within the neighborhood will be averaged.
# A larger sigma_r results in large regions of constant color. Range 0 - 1


cv2.imshow("Watercolor Painting", res)
cv2.waitKey(0)