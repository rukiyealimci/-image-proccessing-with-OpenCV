# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:25:25 2023

@author: rukiy
"""

import cv2 as cv

image= cv.imread('image.jpg')
# Histogram eşitleme
equalized_image = cv.equalizeHist(image)

cv.imshow("equalized_image",equalized_image)

cv.waitKey(0)
cv.destroyAllWindows()
