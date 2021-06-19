import cv2
img = cv2.imread('cat.jpg')
dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=100, sigma_r=0.07, shade_factor=0.1)
# sigma_s and sigma_r are the same as in stylization.
# shade_factor is a simple scaling of the output image intensity.
# The higher the value, the brighter is the result. Range 0 - 0.1


cv2.imshow("Black and White Sketch", dst_gray)
# cv2.imshow("Color Sketch", dst_color)


# Pencil Sketch from scratch
"""
1. Convert the RGB color image to grayscale.
2. Invert the grayscale image to get a negative.
3. Apply a Gaussian blur to the negative from step 2.
4. Blend the grayscale image from step 1 with the 
   blurred negative from step 3 using a color dodge.
   
"""

# To grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the image
inverted_gray_image = 255 - gray_image

# Gaussian Blur
blurred_image = cv2.GaussianBlur(inverted_gray_image, (41,41), 0)

# Invert the blurred image
inverted_blurred_image = 255 - blurred_image

# Create the pencil sketch image
pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale = 256.0)

cv2.imshow("Scratch Pencil Image", pencil_sketch_image)

cv2.imshow("Original Image", img)

cv2.waitKey(0)