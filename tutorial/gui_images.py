"""
ref:
https://docs.opencv.org/4.1.2/dc/d2e/tutorial_py_image_display.html
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


# img = cv.imread('messi5.jpg', cv.IMREAD_COLOR)
img = cv.imread('messi5.jpg', cv.IMREAD_GRAYSCALE)
# img = cv.imread('messi5.jpg', cv.IMREAD_UNCHANGED)

cv.imshow('image', img)

# cv.namedWindow('image', cv.WINDOW_NORMAL)
# cv.imshow('image', img)

k = cv.waitKey(0)
if k == 27:  # ESC
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('messigray.png', img)
    cv.destroyAllWindows()
elif k == ord('m'):
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()
