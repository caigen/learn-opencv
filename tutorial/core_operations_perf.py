"""
ref:
https://docs.opencv.org/master/dc/d71/tutorial_py_optimization.html
"""

import numpy as np
import cv2 as cv
from timeit import timeit

e1 = cv.getTickCount()
e2 = cv.getTickCount()
t = (e2 - e1) / cv.getTickFrequency()
print(t)

img1 = cv.imread('messi5.jpg')
e1 = cv.getTickCount()
for i in range(5,49,2):
    img1 = cv.medianBlur(img1,i)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print(t)

print(cv.useOptimized())
e1 = cv.getTickCount()
cv.medianBlur(img1, 49)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print(t)

cv.setUseOptimized(False)
print(cv.useOptimized())
e1 = cv.getTickCount()
cv.medianBlur(img1, 49)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print(t)

