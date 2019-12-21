"""
ref:
https://docs.opencv.org/master/d0/d86/tutorial_py_image_arithmetics.html
"""

import numpy as np
import cv2 as cv

x = np.uint8([250])
y = np.uint8([10])

# 250 + 10 = 260 => 255
print(cv.add(x, y))

# 250 + 10 = 260 % 256 = 4
print(x + y)

img1 = cv.imread("ml.jpg")
img2 = cv.imread("opencv-logo.png")

dst = cv.addWeighted(img1[0:80, 0:80], 0.7, img2[0:80, 0:80], 0.3, 0)

cv.imshow("dst", dst)
cv.waitKey(0)
cv.destroyAllWindows()